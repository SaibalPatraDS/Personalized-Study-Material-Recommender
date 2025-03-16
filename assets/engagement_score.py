## Caalculation of Engagement Score

# importing libraries
import pandas as pd
import numpy as np
from pandas.io.pickle import pc
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

# loading the data
interactions_df = pd.read_csv("./datasets/interactions.csv")
# print(interactions_df.head())

## Data Cleaning and Normalization

# Select columns to normalize
columns = ['rating', 'watch_time', 'clicked']

# Apply MinMaxScaler
scaler = MinMaxScaler()
interactions_df[columns] = scaler.fit_transform(interactions_df[columns])

# Looking into the data
print(interactions_df.head())

## Optimal Weights of 𝛼, 𝛽, 𝛾 - Perform PCA and Linear Regression and Logistic Regressions

# PCA Implementation
pca = PCA(n_components=1)
principle_component = pca.fit_transform(interactions_df[columns])

# Extract the weights 
pca_weights = pca.components_[0]

# Normalize the weights 
pca_weights /= abs(pca_weights).sum()

# pca weights
print("PCA Weights (α, β, γ):",pca_weights)

# Linear Regression Implementations
interactions_df_lr = interactions_df.copy()

# Create Engagement Score 
interactions_df_lr['engagement_score'] = interactions_df_lr['rating'] + interactions_df_lr['watch_time'] + interactions_df_lr['clicked']

# Define X and y variable
X = interactions_df_lr[['rating', 'watch_time', 'clicked']]
y = interactions_df_lr['engagement_score']

# Fit the Linear Model
lr_model = LinearRegression()
lr_model.fit(X,y)

# Extract Weights
lr_weights = lr_model.coef_

# Normalize the Weights
lr_weights /= abs(lr_weights).sum()

# looking into the weights
print("Linear Regression Weights (α, β, γ):",lr_weights)

# Logistics Regressions Implementation
interactions_df_lgr = interactions_df.copy()

# Engage Variable [If watch-time > median(watch-time) -> True Engagement]
interactions_df_lgr['engage'] = (interactions_df_lgr['watch_time'] > interactions_df_lgr['watch_time'].median()).astype('int')

# Train Logistic Regressions Model
X_lgr = interactions_df_lgr[['rating', 'watch_time', 'clicked']]
y_lgr = interactions_df_lgr['engage']

log_reg = LogisticRegression()
log_reg.fit(X_lgr,y_lgr)

# Extract Coefficients
log_reg_weights = log_reg.coef_[0]
# Normalize the weights
log_reg_weights /= abs(log_reg_weights).sum()

print("Logistic Regression Weights (α, β, γ):",log_reg_weights)

# Moving forward with PCA given Weights
alpha, beta, gamma = pca_weights
interactions_df['engagement_score'] = (alpha* interactions_df['rating'] + beta * interactions_df['watch_time'] + gamma * interactions_df['clicked'])


# looking into final results
print(interactions_df.describe())
