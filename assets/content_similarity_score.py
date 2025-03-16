## Content Similarity Score

# importing libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import seaborn as sns
from prettytable import PrettyTable

# loading the data
course_df = pd.read_csv("./datasets/course.csv")
# print(course_df)

# initialize the Tf-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words='english', min_df = 1, max_df = 0.50)
# print(tfidf)

# Transform courese description into Tf-IDF Vectors
tfidf_matrix = tfidf.fit_transform(course_df['Description'])
# print(tfidf_matrix)

# Convert to DataFrame for easy viewing
tfidf_df = pd.DataFrame(
    tfidf_matrix.toarray(),
    index = course_df['course_id'],
    columns = tfidf.get_feature_names_out()
)

# Compute Cosine Similarity Matrix
cosine_similarity_df = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Convert to DataFrame
cosine_similarity_df = pd.DataFrame(
    cosine_similarity_df,
    index = course_df['Course_title'],
    columns = course_df['Course_title']
)

print(cosine_similarity_df.loc['Introduction to Python'].sort_values(ascending = False)[:5])

# Show top 5 Course - For Each Course
def top_course(course_title, top_n):
    similar_courses = cosine_similarity_df.loc[course_title].sort_values(ascending = False)[1:top_n+1].index
    return similar_courses

# Print top course for 'Getting Started with Large Language Models'
print("Please Enter the Course Name: ")
course_title = input()
print("Please Enter the Course you wanted to look out :")
top_n = int(input())
print(f"Top {top_n} courses for {course_title} are : {top_course(course_title, top_n)}")
