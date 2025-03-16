## Collaborative Filtering

# loading libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from scipy.sparse.linalg import svds

# Loading the data 
course_df = pd.read_csv("./datasets/course.csv")
interactions_df = pd.read_csv("./datasets/interactions.csv")
# print(interactions_df.head())

# Flagging the features
features = ['rating', 'watch_time', 'clicked']

# normalize the data 
scaler = MinMaxScaler()
interactions_df[features] = scaler.fit_transform(
    interactions_df[features]
)

# Calculating the Enagagement Score [Coefficents from Previous Calculation]
alpha, beta, gamma = [0.35948793, 0.00087622, 0.63963586]
interactions_df['engagement_score'] = (
    alpha* interactions_df['rating'] + beta * interactions_df['watch_time'] + gamma * interactions_df['clicked']
)
# print(interactions_df.head())

# Create User-Item Interaction Matrix 
user_item_matrix = interactions_df.pivot(
    index = 'user_id',
    columns = 'course_id',
    values = 'engagement_score'
).fillna(0)

# Convert to numpy matrix
user_item_matrix_np = user_item_matrix.values

# print(user_item_matrix.notnull().sum()/user_item_matrix.size) # always less than 1%

# print(user_item_matrix_np)

# Checking Sparsity
# print(f"Sparsity: {1 - np.count_nonzero(user_item_matrix_np) / user_item_matrix_np.size:.4f}")

# Apply Matrix Factorization (SVD)
"""
Singular Value decomposition to factorize the matrix into user preference and course preference
"""

# Perform SVD
U, sigma, Vt = svds(user_item_matrix_np, k=10) ## k - Number of Latent Features
# print(U.shape, sigma.shape, Vt.shape)

# Convert sigma into a diagonal matrix
sigma = np.diag(sigma)

# Compute Predicted Ratings
predicted_ratings = np.dot(np.dot(U, sigma), Vt)
print(predicted_ratings)
# Convert to DataFrame 
predicted_ratings_df = pd.DataFrame(
    predicted_ratings,
    index = user_item_matrix.index,
    columns = user_item_matrix.columns
)

# looking into the data
# print(predicted_ratings_df.head())

# Get Course Recommendation for a User
# Get the top 5 course recommendations for a user
def recommend_courses(user_id, top_n):
    user_id = int(user_id)
    user_ratings = predicted_ratings_df.loc[user_id].sort_values(ascending = False)[:top_n]
    recommended_courses = course_df[course_df['course_id'].isin(user_ratings.index)]
    return recommended_courses[['course_id', 'Course_title']]

# Looking into recommendation
print(recommend_courses(3,5))
