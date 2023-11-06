"""
Customer Lifetime Value (CLTV) Prediction

This script calculates CLTV using the BG/NBD and Gamma-Gamma submodels. It preprocesses the data, fits the BG/NBD model,
fits the Gamma-Gamma model, and calculates CLTV for each customer. The results are saved in a CSV file.

Usage:
1. Prepare your transaction data in a CSV file.
2. Update the 'data.csv' file path.
3. Run the script.

Make sure to install the required libraries: pandas, lifetimes

Author: MEF
"""

import pandas as pd
import datetime as dt
from lifetimes import BetaGeoFitter, GammaGammaFitter

class CLTVPredictor:
    
    def __init__(self, dataframe, month=3):
        
        """
        Initialize the CLTVPredictor.

        Args:
            dataframe (pd.DataFrame): A pandas DataFrame containing customer transaction data.
            month (int, optional): Number of months for CLTV calculation. Default is 3.
        """
        
        self.dataframe = dataframe
        self.month = month

    def preprocess_data(self):
        
        """
        Preprocess the data by cleaning and structuring it for CLTV calculation.
        """
        
        self.dataframe.dropna(inplace=True)
        self.dataframe = self.dataframe[~self.dataframe["Invoice"].str.contains("C", na=False)]
        self.dataframe = self.dataframe[self.dataframe["Quantity"] > 0]
        self.dataframe = self.dataframe[self.dataframe["Price"] > 0]
        self.dataframe["TotalPrice"] = self.dataframe["Quantity"] * self.dataframe["Price"]
        today_date = dt.datetime(2011, 12, 11)

        cltv_df = self.dataframe.groupby('Customer ID').agg(
            {'InvoiceDate': [lambda InvoiceDate: (InvoiceDate.max() - InvoiceDate.min()).days,
                             lambda InvoiceDate: (today_date - InvoiceDate.min()).days],
             'Invoice': lambda Invoice: Invoice.nunique(),
             'TotalPrice': lambda TotalPrice: TotalPrice.sum()})

        cltv_df.columns = cltv_df.columns.droplevel(0)
        cltv_df.columns = ['recency', 'T', 'frequency', 'monetary']
        cltv_df["monetary"] = cltv_df["monetary"] / cltv_df["frequency"]
        cltv_df = cltv_df[(cltv_df['frequency'] > 1)]
        cltv_df["recency"] = cltv_df["recency"] / 7
        cltv_df["T"] = cltv_df["T"] / 7

        self.dataframe = cltv_df

    def fit_bgf_model(self):
        
        """
        Fit the BG/NBD model to the preprocessed data and calculate expected purchase predictions.

        Returns:
            pd.DataFrame: Updated DataFrame with BG/NBD model results.
        """
        
        bgf = BetaGeoFitter(penalizer_coef=0.001)
        bgf.fit(self.dataframe['frequency'], self.dataframe['recency'], self.dataframe['T'])

        self.dataframe["expected_purc_1_week"] = bgf.predict(1, self.dataframe['frequency'],
                                                          self.dataframe['recency'], self.dataframe['T'])

        self.dataframe["expected_purc_1_month"] = bgf.predict(4, self.dataframe['frequency'],
                                                           self.dataframe['recency'], self.dataframe['T'])

        self.dataframe["expected_purc_3_month"] = bgf.predict(12, self.dataframe['frequency'],
                                                           self.dataframe['recency'], self.dataframe['T'])

    def fit_ggf_model(self):
        
        """
        Fit the Gamma-Gamma model to the preprocessed data and calculate expected average profit predictions.

        Returns:
            pd.DataFrame: Updated DataFrame with Gamma-Gamma model results.
        """
        
        ggf = GammaGammaFitter(penalizer_coef=0.01)
        ggf.fit(self.dataframe['frequency'], self.dataframe['monetary'])
        self.dataframe["expected_average_profit"] = ggf.conditional_expected_average_profit(
            self.dataframe['frequency'], self.dataframe['monetary'])

    def calculate_cltv(self):
        
        """
        Calculate Customer Lifetime Value (CLTV) for each customer.

        Returns:
            pd.DataFrame: DataFrame with CLTV results.
        """
        
        cltv = ggf.customer_lifetime_value(bgf, self.dataframe['frequency'], self.dataframe['recency'],
                                          self.dataframe['T'], self.dataframe['monetary'],
                                          time=self.month, freq="W", discount_rate=0.01)
        cltv = cltv.reset_index()
        cltv_final = self.dataframe.merge(cltv, on="Customer ID", how="left")
        cltv_final["segment"] = pd.qcut(cltv_final["clv"], 4, labels=["D", "C", "B", "A"])

        return cltv_final

    def run(self):
        """
        Run CLTV predictions by preprocessing data, fitting models, and calculating CLTV.

        Returns:
            pd.DataFrame: DataFrame with CLTV predictions.
        """
        self.preprocess_data()
        self.fit_bgf_model()
        self.fit_ggf_model()
        cltv_result = self.calculate_cltv()

        return cltv_result

if __name__ == "__main__":
    df = pd.read_csv('data.csv')  # Load data from a CSV file
    cltv_predictor = CLTVPredictor(df)
    cltv_result = cltv_predictor.run()
    cltv_result.to_csv("cltv_prediction.csv")
