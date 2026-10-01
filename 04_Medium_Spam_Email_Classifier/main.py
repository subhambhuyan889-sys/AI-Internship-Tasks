from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

DATA = [
    ("Congratulations! You won a free prize", "spam"),
    ("Claim your free reward now", "spam"),
    ("Win money by clicking this link", "spam"),
    ("You have received a special offer", "spam"),
    ("Please send the project report", "not spam"),
    ("Can we meet tomorrow for the project?", "not spam"),
    ("The class starts at 10 AM", "not spam"),
    ("Please review the attached document", "not spam"),
]


def train_model():
    texts = [item[0] for item in DATA]
    labels = [item[1] for item in DATA]

    vectorizer = CountVectorizer()
    x_train = vectorizer.fit_transform(texts)

    model = MultinomialNB()
    model.fit(x_train, labels)

    return vectorizer, model


def classify_message(message, vectorizer, model):
    features = vectorizer.transform([message])
    return model.predict(features)[0]


def run_classifier():
    vectorizer, model = train_model()
    print("Spam Email Classifier")
    message = input("Enter an email/message: ")
    result = classify_message(message, vectorizer, model)
    print("Prediction:", result.upper())


if __name__ == "__main__":
    run_classifier()
