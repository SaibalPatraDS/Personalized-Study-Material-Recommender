# Personalized-Study-Material-Recommender
Imagine an online learning platform where users enroll in different courses. The platform has a large library of study materials (videos, PDFs, articles, quizzes, coding problems).

## Dataset Structure:
We'll create three tables similar to what one will find in a real-world ed-tech platform:

`Users Table` (*users_df*):

    * user_id: Unique ID for each user.
    * name: Random user names.
    * study_level: Beginner, Intermediate, Advanced.

`Study Materials Table` (*materials_df*):

    * material_id: Unique ID for each material.
    * title: Study material title.
    * course_topic: Topic of the material (e.g., Python, SQL, ML).
    * difficulty: Difficulty level (Beginner, Intermediate, Advanced).
    * content_type: Type of content (Video, PDF, Article, Quiz).

`User Interactions Table` (*interactions_df*):

    * user_id: Who interacted with the material.
    * material_id: Which material was accessed.
    * time_spent: Time spent on the material (in minutes).
    * rating: User rating (1-5).
    * progress_percent: How much of the material was completed.
