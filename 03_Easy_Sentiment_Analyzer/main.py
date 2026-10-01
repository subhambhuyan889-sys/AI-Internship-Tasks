import re

POSITIVE_WORDS = {
    "amazing", "awesome", "good", "great", "happy",
    "excellent", "love", "wonderful", "fantastic", "best"
}

NEGATIVE_WORDS = {
    "bad", "terrible", "sad", "hate", "awful",
    "boring", "worst", "poor", "horrible"
}


def analyze_sentiment(text):
    words = re.findall(r"\b[a-z']+\b", text.lower())
    positive_count = sum(word in POSITIVE_WORDS for word in words)
    negative_count = sum(word in NEGATIVE_WORDS for word in words)

    if positive_count > negative_count:
        sentiment = "Positive"
    elif negative_count > positive_count:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, positive_count, negative_count


def run_analyzer():
    print("Text Sentiment Analyzer")
    text = input("Enter a sentence: ")

    sentiment, positive_count, negative_count = analyze_sentiment(text)

    print("Positive count:", positive_count)
    print("Negative count:", negative_count)
    print("Sentiment:", sentiment)


if __name__ == "__main__":
    run_analyzer()
