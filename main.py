import joblib

# Load the trained model and vectorizer
model = joblib.load('trained_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Function to preprocess the user input URL
def preprocess_url(url):
    # Remove the "https://" prefix
    if url.startswith("https://"):
        url = url[8:]
    elif url.startswith("http://"):
        url = url[7:]
    return url.lower()  # Convert to lowercase (or apply any other preprocessing steps)

# Function to classify the URL as phishing or legitimate
def classify_url(url):
    preprocessed_url = preprocess_url(url)
    input_url_vector = vectorizer.transform([preprocessed_url])
    prediction = model.predict(input_url_vector)
    return prediction[0]  # Return the predicted label (0 or 1)

# Print the fancy header
print("\033[1;31mPhish Detect v1\033[0m")
print("\033[1;32mAuthor: Chinmoy Pratim Borah\033[0m")
print("\033[1;32mThanks to Tarun Tiwari for the dataset.\033[0m")
print("\033[1;32mProfile: \033[0m\033[1;32mhttps://www.linkedin.com/in/chinmoypratimborah/\033[0m")

while True:
    # Get user input URL for classification
    user_url = input("Enter the URL to classify (or 'exit' to quit): ")

    if user_url.lower() == 'exit':
        break

    # Classify the user input URL
    prediction = classify_url(user_url)

    # Display the prediction result
    if prediction == 1:
        print("Phishing website detected!")
    else:
        print("Legitimate website.")

    print()  # Add an empty line for better readability

print("Thank you for using Phish Detect v1!")
