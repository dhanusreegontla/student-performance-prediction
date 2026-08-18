import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("student_performance.csv")

# Input features
X = data[
    [
        "Hours_Studied",
        "Attendance",
        "Previous_Score",
        "Assignments"
    ]
]

# Output
y = data["Performance"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Test model
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# Save model
with open("student_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained successfully!")
print("student_model.pkl created successfully!")