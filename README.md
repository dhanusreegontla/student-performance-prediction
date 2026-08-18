# Student Performance Prediction

## Project Overview

Student Performance Prediction is a machine learning project that predicts whether a student may have **Good** or **Low** academic performance based on study hours, attendance, previous exam score, and assignment performance.

## Objectives

The main objective of this project is to use machine learning to predict student performance and understand how academic factors can influence the prediction.

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* Pickle

## Features

* Enter hours studied per day
* Enter attendance percentage
* Enter previous exam score
* Enter assignment score
* Predict student performance
* Display prediction probability

## Dataset

The dataset contains the following features:

* **Hours_Studied** – Number of hours studied per day
* **Attendance** – Student attendance percentage
* **Previous_Score** – Previous examination score
* **Assignments** – Assignment score
* **Performance** – Target variable (`0 = Low`, `1 = Good`)

## Machine Learning Model

A **Random Forest Classifier** is used to train the model and predict student performance.

## Project Structure

```text
student_performance_prediction/
│
├── student_performance.csv
├── train_model.py
├── app.py
└── student_model.pkl
```

## How to Run the Project

### 1. Install required libraries

```bash
python -m pip install pandas scikit-learn streamlit
```

### 2. Train the model

```bash
python train_model.py
```

This creates the trained model file:

```text
student_model.pkl
```

### 3. Run the Streamlit application

```bash
python -m streamlit run app.py
```

The application will open in the browser.

## Sample Prediction

For example:

* Hours Studied: 7
* Attendance: 85%
* Previous Score: 80
* Assignments: 9

The application predicts the student's academic performance.

## Future Improvements

* Use a larger real-world dataset
* Add more student-related features
* Compare multiple machine learning algorithms
* Add data visualizations
* Store prediction history
* Improve the user interface

## Conclusion

This project demonstrates how machine learning can be used to predict student academic performance using basic academic factors. It also provides a simple Streamlit interface for making predictions.

## Author

**Dhanusri Gontla**

B.Tech – Artificial Intelligence and Machine Learning
