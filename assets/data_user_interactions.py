import pandas as pd
import random

# Load users and courses data
users_df = pd.read_csv("./datasets/users.csv")
courses_df = pd.read_csv("./datasets/course.csv")

# Ensure course_id column has no null values
courses_df = courses_df.dropna(subset=["course_id"])

# Convert course_id to a list for efficient random selection
course_ids = courses_df["course_id"].dropna().tolist()
user_ids = users_df["user_id"].tolist()

# Generate synthetic user-course interactions
def generate_interactions(users, courses, num_interactions=50000):
    interactions = []
    
    for _ in range(num_interactions):
        user_id = random.choice(users)
        course_id = random.choice(courses)

        rating = round(random.uniform(1, 5), 1)  # Rating between 1 and 5
        watch_time = round(random.uniform(0, 100), 2)  # Percentage of course completed
        clicked = 1 if rating > 2.5 else random.choice([0, 1])  # Whether the user clicked (1 = Yes, 0 = No)

        interactions.append({
            "user_id": user_id,
            "course_id": course_id,
            "rating": rating,
            "watch_time": watch_time,
            "clicked": clicked
        })
    
    return pd.DataFrame(interactions)

# Generate interactions data
interactions_df = generate_interactions(user_ids, course_ids)

# Save interactions as CSV
interactions_df.to_csv("./datasets/interactions.csv", index=False)

print("User-Course Interactions dataset saved successfully!")