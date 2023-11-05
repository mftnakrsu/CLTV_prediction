# CLTV Customer Life Time Value Prediction 

Project Title: CLTV Customer Lifetime Value Analysis

## Introduction:

Customer loyalty and customer value are crucial factors for any business. These factors help businesses make strategic decisions by understanding their customers' future behaviors. Customer Lifetime Value (CLTV) is a vital metric that assists businesses in predicting the future value of their customers.

This project includes a Python tool for conducting CLTV analysis and prediction. Based on customers' past shopping behavior, this tool helps each customer's future value prediction. Additionally, it incorporates advanced statistical methods, such as the BG/NBD model and the Gamma Gamma Submodel, for CLTV prediction.

By using this project, you can find answers to the following questions:

What will be the future purchase predictions for each customer?
Which customers are more valuable, and which are less valuable?
How can you optimize your marketing strategies?



The BG/NBD (Beta Geometric/Negative Binomial Distribution) model is a statistical model used to model customer purchase behavior. This model encompasses the fundamental principles for predicting customers' future purchases. The model consists of two main processes: the Transaction Process and the Dropout Process.

**Transaction Process:**
- The Transaction Process models continuous shopping behavior over a customer's lifetime.
- As long as the customer is "alive," the model predicts the probability of making a purchase in a given time period using the "transaction rate." This probability is calculated using the Poisson distribution.
- Each customer has their own "transaction rate" parameter, and they continue to make purchases randomly around this rate.

**Dropout Process:**
- The Dropout Process models the probability of customers leaving (or "dropping out") with a certain probability.
- After making a purchase, customers have a certain probability of leaving the business and not returning, which signifies "dropout."
- Each customer is defined by their "dropout rate" parameters, which are estimated using the beta distribution.

**Expected Value Formula:**
- The BG/NBD model is used to predict customers' future purchases and total values.
- The expected value formula includes individual-level parameters such as x, tx, T, r, alfa, and population-level parameters a and h.
- This expected value formula is used to predict a customer's future purchases during the analysis period. Each component is essential for understanding a customer's past shopping behavior and the model's prediction capabilities.

The BG/NBD model is crucial for businesses with customer bases, such as the retail and e-commerce sectors. This model helps businesses predict their customers' future behaviors and optimize their marketing strategies. Additionally, it aids in developing strategies for customer loyalty and acquisition. The expected value formula enables businesses to predict their customers' future purchases and total values, allowing for the optimization of marketing efforts.

## BG/NBD Model Expected Value Formula

The expected value formula of the BG/NBD model is as follows:

$$E[x,tx,T,r,alfa,a,h] = x * (1 - ((1 + alfa) / (r + T + alfa))) + a * h / (r + T + alfa)$$

This formula is used to predict a customer's future purchases and total value during the analysis period. Each component is essential for understanding a customer's past shopping behavior and the model's prediction capabilities.

- **x:** The number of purchase transactions a customer made during the analysis period.
- **tx:** Represents the customer's lifetime. It is the time from the customer's first purchase to their last purchase.
- **T:** The total time period within the analysis.
- **r:** The rate at which a customer makes purchases over their lifetime (transaction rate).
- **alfa:** Represents the distribution of r values within the population.
- **a:** One parameter of the beta distribution that influences the distribution of customer dropout probabilities.
- **h:** Another parameter of the beta distribution that represents fluctuations in customer dropout probabilities.

This formula assists businesses in predicting their customers' future purchases and total values. Additionally, businesses can use the BG/NBD model to enhance customer loyalty strategies and optimize their marketing efforts.

## Gamma Gamma Submodel and Its Use

- **What is the Gamma Gamma Submodel?** The Gamma Gamma Submodel is a statistical model used for predicting Customer Lifetime Value (CLTV). It is used in conjunction with the BG/NBD model to enhance the precision of CLTV predictions. While the BG/NBD model analyzes customers' shopping behaviors, the Gamma Gamma Submodel assists in estimating the average profit per transaction for each customer.

- **Calculating CLTV:** When calculating CLTV, the BG/NBD model predicts the number of future transactions for each customer, and the Gamma Gamma Submodel estimates the average profit per transaction. By combining these two predictions, the total future value of each customer is calculated. As a result, businesses obtain customer-specific CLTV predictions.

## Gamma Gamma Expected Value Formula and Its Use

- **Gamma Gamma Expected Value Formula:** The expected value formula for the Gamma Gamma Submodel is expressed as E(M|p,q,gamma,mx,x). This formula is used to estimate a customer's future average profit per transaction. Here are the components and explanations of the formula:

  - **p:** The first parameter of the beta distribution representing the average profit per transaction for a customer.
  - **q:** The second parameter of the beta distribution representing the average profit per transaction for a customer.
  - **gamma:** The stability parameter, indicating fluctuations in transactions.
  - **mx:** The total monetary value of a customer, which represents the total value of all transactions made by the customer.
  - **x:** The lifetime of the customer.

- **Its Use:** The Gamma Gamma Submodel helps businesses estimate the future average profit per transaction for each customer. These predictions are used in CLTV calculations to develop customer-specific marketing strategies and services. Additionally, these predictions are used in making strategic decisions such as customer segmentation and product pricing.

In addition to your notes, the term "mx" represents the total monetary value of a customer, signifying the total value of all transactions they have made.
### Gamma Gamma Expected Value Formula

The expected value formula for the Gamma Gamma Submodel is:

$$
E(M|p,q,\gamma,mx,x) = p \cdot \left(1 - \frac{{1 + \gamma}}{{q + x + \gamma}}\right) + q \cdot \frac{{mx}}{{x + \gamma}}
$$


