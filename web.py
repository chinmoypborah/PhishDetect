import joblib
from flask import Flask, request

# Load the trained model and vectorizer
model = joblib.load('trained_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Initialize the Flask application
app = Flask(__name__)

# Function to preprocess the user input URL
def preprocess_url(url):
    if url.startswith("https://"):
        url = url[8:]
    elif url.startswith("http://"):
        url = url[7:]
    return url.lower()

# Function to classify the URL as phishing or legitimate
def classify_url(url):
    preprocessed_url = preprocess_url(url)
    input_url_vector = vectorizer.transform([preprocessed_url])
    prediction = model.predict(input_url_vector)
    return prediction[0]

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        prediction = classify_url(url)
        if prediction == 1:
            result = "Phishing website detected!"
            result_color = "red"
        else:
            result = "Legitimate website."
            result_color = "green"
        return f"""
        <html>
        <head>
            <style>
                body {{
                    background-color: black;
                    overflow: hidden;
                }}

                h1 {{
                    color: green;
                    text-align: center;
                }}

                .textbox {{
                    display: block;
                    margin: 0 auto;
                    text-align: center;
                    box-shadow: 0 0 10px yellow;
                    border-radius: 10px;
                    padding: 10px;
                    width: 300px;
                }}

                .button {{
                    display: block;
                    margin: 0 auto;
                    text-align: center;
                    padding: 10px 20px;
                    background-color: #4CAF50;
                    color: white;
                    border-radius: 5px;
                    font-weight: bold;
                    cursor: pointer;
                }}

                .result {{
                    text-align: center;
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
            <h1>Phish Detect v1</h1>
            <div class="textbox">
                <form method="POST" action="/">
                    <input type="text" name="url" placeholder="Enter URL" required>
                    <button class="button" type="submit">Classify</button>
                </form>
            </div>
            <div class="result" style="color: {result_color};">
                <h2>Result:</h2>
                <p>{result}</p>
            </div>
        </body>
        </html>
        """
    else:
        return """
        <html>
        <head>
            <style>
                body {{
                    background-color: black;
                    overflow: hidden;
                }}

                h1 {{
                    color: green;
                    text-align: center;
                }}

                .textbox {{
                    display: block;
                    margin: 0 auto;
                    text-align: center;
                    box-shadow: 0 0 10px yellow;
                    border-radius: 10px;
                    padding: 10px;
                    width: 300px;
                }}

                .button {{
                    display: block;
                    margin: 0 auto;
                    text-align: center;
                    padding: 10px 20px;
                    background-color: #4CAF50;
                    color: white;
                    border-radius: 5px;
                    font-weight: bold;
                    cursor: pointer;
                }}

                .result {{
                    text-align: center;
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
            <h1>Phish Detect v1</h1>
            <div class="textbox">
                <form method="POST" action="/">
                    <input type="text" name="url" placeholder="Enter URL" required>
                    <button class="button" type="submit">Classify</button>
                </form>
            </div>
        </body>
        </html>
        """

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
