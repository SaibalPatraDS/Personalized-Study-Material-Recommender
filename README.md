# Personalized-Study-Material-Recommender
Imagine an online learning platform where users enroll in different courses. The platform has a large library of study materials (videos, PDFs, articles, quizzes, coding problems).

## Dataset Structure:
We'll create three tables similar to what one will find in a real-world ed-tech platform:

`Users Table` (*users*):

    * user_id: Unique ID for each user.
    * name: Random user names.
    * study_level: Beginner, Intermediate, Advanced.

`Study Materials Table` (*materials*):

    * material_id: Unique ID for each material.
    * title: Study material title.
    * course_topic: Topic of the material (e.g., Python, SQL, ML).
    * difficulty: Difficulty level (Beginner, Intermediate, Advanced).
    * content_type: Type of content (Video, PDF, Article, Quiz).

`User Interactions Table` (*interactions*):

    * user_id: Who interacted with the material.
    * courese_id: Which material was accessed.
    * rating: User rating (1-5).
    * time_spent: Time spent on the material (in minutes).
    * clicked: Whether the user clicked (1 = Yes, 0 = No)

*Note* : 
**Understanding Click Activity (C) and Watch Time (W) Relationship**

Click Activity (C) = Whether a user clicked on a course (1 = Clicked, 0 = Not Clicked)
Watch Time (W) = Total minutes a user watched the course
💡 **Logical Assumption**:

    If C = 0 (User didn’t click), then W should be 0 because watching is impossible without clicking.
    Possible Reasons Why W ≠ 0 when C = 0

The Dataset Might Have Some Noise:

*   Sometimes, datasets contain inconsistencies due to logging errors.
Maybe "clicked" was recorded separately, while "watch time" was extracted from session logs.
Implicit Interaction Logging:

*   If a user accesses a course via direct links or recommendations, the platform may not register a "click" but still track watch time.
Example: Auto-play videos on some platforms don’t require explicit clicks.
Delayed Click Events:

*   Some platforms record clicks with delays, causing misalignment in logs.


## Step 2: Compute Engagement Scores
Now that you have your interactions.csv ready, let's compute the Engagement Score for each user-course interaction. This will help in improving the quality of recommendations.

💡 What is **Engagement Score**?
Engagement score quantifies how much a user is interacting with a course. It is a weighted sum of multiple factors like:

*Rating (R)* → How much the user rated the course (1-5 scale).
*Watch Time (W)* → How much time (in minutes) the user spent watching the course.
*Click Activity (C)* → Whether the user clicked on the course or not (binary: 0 or 1).
Formula:

                        𝐸 = 𝛼 × 𝑅 + 𝛽 × 𝑊 + 𝛾 × 𝐶

where α, β, γ are the weights of each factor.
