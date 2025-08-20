import re

# Simple sentiment lexicon
positive_words = {"good", "happy", "joy", "excellent", "fortunate", "correct", "superior", "love", "like", "great", "awesome", "fantastic", "positive", "enjoy"}
negative_words = {"bad", "sad", "pain", "terrible", "unfortunate", "wrong", "inferior", "hate", "dislike", "awful", "horrible", "negative", "angry", "disappoint"}

# Example of potentially biased words (for demonstration)
biased_words = {"always", "never", "everyone", "nobody"}

def clean_text(text):
    # Lowercase and remove non-alphabetic characters
    return re.sub(r'[^a-zA-Z\s]', '', text.lower())

def detect_bias(text):
    found_biased = [word for word in biased_words if word in text.split()]
    return found_biased

def sentiment_analysis(text):
    text = clean_text(text)
    words = text.split()
    pos_count = sum(1 for word in words if word in positive_words)
    neg_count = sum(1 for word in words if word in negative_words)
    bias_found = detect_bias(text)
    
    if bias_found:
        print(f"Warning: Potentially biased words detected: {', '.join(bias_found)}")
        print("Consider revising your input to reduce bias for more accurate sentiment analysis.")
    
    if pos_count > neg_count:
        return "Positive"
    elif neg_count > pos_count:
        return "Negative"
    else:
        return "Neutral"

def main():
    print("Sentiment Analysis Tool")
    user_input = input("Enter a sentence for sentiment analysis: ")
    result = sentiment_analysis(user_input)
    print(f"Sentiment: {result}")

if __name__ == "__main__":
    main()
