Medical Cost Prediction App 

📌 Project Overview:
The Medical Cost Prediction App is a machine learning–powered web application built using Streamlit.
It predicts the medical insurance charges for an individual based on demographic and lifestyle factors such as age, BMI, smoking habits, and region.
This helps users understand estimated medical expenses and supports organizations in cost planning and risk assessment.

🧠 Features:
Predicts insurance charges based on user input
Simple and interactive Streamlit UI
Uses a trained machine learning model (.pkl)
Real-time prediction with clean UI
Lightweight, fast, and easy to deploy

📂 Project Structure:
Medical_Cost_App/
│-- app.py
│-- model.pkl
│-- requirements.txt
│-- README.md

⚙️ Input Features:
The app takes the following inputs:

Feature	Description:
Age:	Age of the individual
Sex:	Male / Female
BMI:	Body Mass Index
Children:	Number of dependents
Smoker:	Yes / No
Region:	Northeast / Northwest / Southeast / Southwest

📈 How the Model Works:
The model is trained using the Medical Cost Personal Dataset.
Algorithms commonly used for this task include:
Linear Regression
Random Forest Regression
XGBoost / Gradient Boosting
The final best-performing model is saved as model.pkl.

🛠️ Technologies Used:
Python
Streamlit
NumPy & Pandas
Scikit-learn
Pickle

📊 Sample Prediction Workflow:
User enters personal and lifestyle details
The model processes the input
Returns estimated medical insurance charges

🚀 Deployment (Optional):
You can deploy the app easily using:
Streamlit Cloud
Render
Hugging Face Spaces
Heroku (Docker recommended)

🙌 Author:
Tanvi Bramhnakar

✔ Model explanation

Would you like the Streamlit app code as well?
