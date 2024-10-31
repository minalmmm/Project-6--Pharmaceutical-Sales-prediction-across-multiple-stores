# Pharmaceutical Sales Prediction

## Project Overview
Rossman Pharmaceuticals operates multiple stores across various cities. This project aims to forecast sales across all stores six weeks in advance. The prediction model considers factors such as promotions, competition, holidays, seasonality, and locality.

## Data and Features
The dataset consists of several fields that are crucial for predicting sales:
- **Id**: Unique identifier for each (Store, Date) pair in the test set.
- **Store**: Unique ID for each store.
- **Sales**: Daily turnover (target variable).
- **Customers**: Number of customers on a given day.
- **Open**: Indicator of whether the store was open (0 = closed, 1 = open).
- **StateHoliday**: Indicates state holidays (a = public holiday, b = Easter, c = Christmas, 0 = none).
- **SchoolHoliday**: Indicates if public school closures affected the day.
- **StoreType**: Differentiates among four store models (a, b, c, d).
- **Assortment**: Assortment levels (a = basic, b = extra, c = extended).
- **CompetitionDistance**: Distance in meters to the nearest competitor.
- **CompetitionOpenSince[Month/Year]**: Approximate opening date of the nearest competitor.
- **Promo**: Indicates if a promotion is running (1 = yes, 0 = no).
- **Promo2**: Ongoing promotions (1 = participating, 0 = not).
- **Promo2Since[Year/Week]**: Start date of Promo2 participation.
- **PromoInterval**: Months when Promo2 restarts (e.g., "Feb,May,Aug,Nov").

## Models Used
The project employs several machine learning techniques to predict sales:
1. **Linear Regression**: A linear approach to modeling the relationship between features and the target variable.
2. **Lasso Regression**: A linear regression method that includes L1 regularization to prevent overfitting.
3. **Ridge Regression**: Similar to Lasso, but uses L2 regularization to minimize the complexity of the model.
4. **K-Neighbors Regressor**: A non-parametric method that predicts values based on the average of the k-nearest neighbors.
5. **Decision Tree Regressor**: A model that makes predictions by learning simple decision rules inferred from the data features.
6. **Random Forest Regressor**: An ensemble learning method that constructs multiple decision trees for improved accuracy.
7. **XGBRegressor**: An efficient implementation of gradient boosting for regression tasks.
8. **AdaBoost Regressor**: A boosting technique that combines the outputs of several weak learners to create a strong predictive model.

## Streamlit App
A Streamlit application was developed to serve the trained models. Users can upload their data as a CSV file, and the app will return sales predictions.

### Output Display
![Output Image 1](https://github.com/minalmmm/Project-6--Pharmaceutical-Sales-prediction-across-multiple-stores/blob/main/Notebook/image1.png)  
![Output Image 2](https://github.com/minalmmm/Project-6--Pharmaceutical-Sales-prediction-across-multiple-stores/blob/main/Notebook/image2.png)  
![Output Image 3](https://github.com/minalmmm/Project-6--Pharmaceutical-Sales-prediction-across-multiple-stores/blob/main/Notebook/image3.png)  
![Output Image 4](https://github.com/minalmmm/Project-6--Pharmaceutical-Sales-prediction-across-multiple-stores/blob/main/Notebook/image4.png)  
![Output Image 5](https://github.com/minalmmm/Project-6--Pharmaceutical-Sales-prediction-across-multiple-stores/blob/main/Notebook/image5.png)  
![Output Image 6](https://github.com/minalmmm/Project-6--Pharmaceutical-Sales-prediction-across-multiple-stores/blob/main/Notebook/image6.png)  

