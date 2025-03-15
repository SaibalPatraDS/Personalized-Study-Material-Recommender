import pandas as pd
import random

# Define possible categories and topics
COURSE_CATEGORIES = ["Data Science", "Web Development", "Machine Learning", "Cybersecurity", "Cloud Computing"]
TOPICS = {
    "Data Science": ["Python", "Statistics", "SQL", "Tableau", "Big Data"],
    "Web Development": ["JavaScript", "React", "HTML & CSS", "Node.js", "Django"],
    "Machine Learning": ["Neural Networks", "Deep Learning", "Computer Vision", "NLP", "Reinforcement Learning"],
    "Cybersecurity": ["Network Security", "Ethical Hacking", "Malware Analysis", "Cryptography", "Risk Management"],
    "Cloud Computing": ["AWS", "Azure", "Google Cloud", "Docker", "Kubernetes"]
}

# Generate synthetic users
def generate_users(num_users=100000):
    users = []
    for user_id in range(1, num_users + 1):
        name = f"User{user_id}"
        age = random.randint(18, 50)
        interests = ", ".join(random.sample(COURSE_CATEGORIES, k=2))  # Store interests as string
        users.append({"user_id": user_id, "name": name, "age": age, "interests": interests})
    return pd.DataFrame(users)

# Generate synthetic courses
def generate_courses(num_courses=100):
    courses = []
    for course_id in range(1, num_courses + 1):
        category = random.choice(COURSE_CATEGORIES)
        topic = random.choice(TOPICS[category])
        title = f"{topic} for Beginners" if random.random() > 0.5 else f"Advanced {topic} Techniques"
        description = f"A comprehensive course on {topic} in {category}."
        courses.append({"course_id": course_id, "title": title, "category": category, "description": description})
    return pd.DataFrame(courses)

# Generate Data
users_df = generate_users()
courses_df = generate_courses()

# Save as CSV
users_df.to_csv("./datasets/users.csv", index=False)
courses_df.to_csv("./datasets/courses.csv", index=False)

print("Users and Courses datasets saved successfully!")