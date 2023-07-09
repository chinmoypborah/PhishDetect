import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Step 1: Load the dataset
dataset = pd.read_csv("phishing_dataset.csv")

# Step 2: Preprocess the data (if needed)

# Step 3: Split the dataset into features (URL) and labels
X = dataset.iloc[:, 0]  # Assuming the URL column is the first column (index 0)
y = dataset.iloc[:, 1]  # Assuming the Label column is the second column (index 1)

# Step 4: Feature extraction
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Step 5: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Train the model with increased max_iter
model = LogisticRegression(max_iter=1000)  # Increase max_iter value
model.fit(X_train, y_train)

# Step 7: Make predictions on the testing set
y_pred = model.predict(X_test)

# Step 8: Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Step 9: Save the trained model to a file
joblib.dump(model, 'trained_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

# Step 10: Print a message indicating the model is saved
print("Trained model saved successfully.")
