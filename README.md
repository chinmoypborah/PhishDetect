# Phish Detect v1

Phish Detect v1 is a Python script that utilizes a trained machine-learning model to classify URLs as either phishing or legitimate. It is designed to help detect potential phishing websites by analyzing the provided URL.

<b>Accuracy:</b> 0.9635933375807773

## Description
This script leverages a logistic regression model trained on a dataset of phishing and legitimate URLs. It uses the CountVectorizer for feature extraction and the trained model for classification. By preprocessing the user input URL and transforming it into a feature vector, the script predicts whether the URL is a phishing website or a legitimate website.

## Usage

1. Ensure that you have Python installed on your system.
2. Clone or download this repository to your local machine.
3. Install the required dependencies by running the following command:

```pip install -r requirements.txt```

4. Download the trained model (trained_model.pkl) and vectorizer (vectorizer.pkl) files and place them in the same directory as the script.
5. Open a command prompt or terminal and navigate to the project directory.
6. Run the script using the following command:

```python main.py```

7. Follow the on-screen prompts to enter the URL you want to classify as phishing or legitimate.
8. The script will provide the classification result based on the trained model.

<b>Note:</b> The trained model in this repository was trained on a specific dataset. It is recommended to periodically update the dataset and retrain the model for better performance and accuracy.

Thanks to Tarun Tiwari for the Dataset. (https://www.kaggle.com/datasets/taruntiwarihp/phishing-site-urls)

<b>Note:</b> This data-set is 3 years old, so it might not detect some new Phishing URLs, I will update the data-set constantly with new URLs so it detects new possible URL's as well.

Feel free to customize the description and usage instructions to provide additional details or clarify any specific steps or requirements for your repository.
