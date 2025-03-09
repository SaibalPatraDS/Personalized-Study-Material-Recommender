import pandas as pd
import numpy as np
import random
import sqlite3

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# 1. generate Users DataFrame
num_users = 10000
user_ids = list(range(1, num_users + 1))
user_names = [f"person_{i}" for i in user_ids]
study_levels = random.choices(["Beginner", "Intermediate", "Advanced"], k=num_users)

users_df = pd.DataFrame({"user_id": user_ids, "name": user_names, "study_level": study_levels})

# 2. Generate Study Materials DataFrame
num_materials = 50
material_ids = list(range(1, num_materials + 1))
topics = ["Python", "SQL", "Machine Learning", "Data Science", "Deep Learning"]
difficulty_levels = ["Beginner", "Intermediate", "Advanced"]
content_types = ["Video", "PDF", "Article", "Quiz"]

materials_df = pd.DataFrame({
    "material_id": material_ids,
    "title": [f"{random.choice(topics)} - {random.choice(content_types)}" for _ in range(num_materials)],
    "course_topic": [random.choice(topics) for _ in range(num_materials)],
    "difficulty": [random.choice(difficulty_levels) for _ in range(num_materials)],
    "content_type": [random.choice(content_types) for _ in range(num_materials)]
})

# 3. Generate User Interactions DataFrame
num_interactions = 75000
interaction_user_ids = random.choices(user_ids, k=num_interactions)
interaction_material_ids = random.choices(material_ids, k=num_interactions)
time_spent = np.random.randint(1, 60, size=num_interactions)
ratings = np.random.randint(1, 6, size=num_interactions)
progress_percent = np.random.randint(0, 101, size=num_interactions)

interactions_df = pd.DataFrame({
    "user_id": interaction_user_ids,
    "material_id": interaction_material_ids,
    "time_spent": time_spent,
    "rating": ratings,
    "progress_percent": progress_percent
})

## Storing the data sqlite

# Create an in-memory database
conn = sqlite3.connect(":memory:")

# Store data
users_df.to_sql("users", conn, if_exists="replace", index=False)
materials_df.to_sql("materials", conn, if_exists="replace", index=False)
interactions_df.to_sql("interactions", conn, if_exists="replace", index=False)

## Saving the connection details Global
db_connection = conn
