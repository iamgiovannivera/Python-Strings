# 1. Product Review Analysis

# reviews = [
#     "This product is really good. I'm impressed with its quality.",
#     "The performance of this product is excellent. Highly recommended!",
#     "I had a bad experience with this product. It didn't meet my expectations.",
#     "Poor quality product. Wouldn't recommend it to anyone.",
#     "The product was average. Nothing extraordinary about it."
# ]

# keywords = ["good", "excellent", "bad", "poor", "average"]

# def highlight_keywords(review, keywords):
#     for keyword in keywords:
#         review = review.replace(keyword, keyword.upper())
#     return review

# for review in reviews:
#     highlighted_review = highlight_keywords(review, keywords)
#     print(highlighted_review)
    
    
# Task 2:
    
    
    
# positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
# negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

# def tally_sentiment(review, positive_words, negative_words):
#     positive_count = sum(review.count(word) for word in positive_words)
#     negative_count = sum(review.count(word) for word in negative_words)
#     return positive_count, negative_count

# for review in reviews:
#     positive_count, negative_count = tally_sentiment(review, positive_words, negative_words)
#     print(f"Review: {review}")
#     print(f"Positive words: {positive_count}, Negative words: {negative_count}\n
          
# Task 3: 


# def create_summary(review, length=30):
#     if len(review) <= length:
#         return review
#     else:
#         end = review[:length].rfind(' ')
#         return review[:end] + "…"

# for review in reviews:
#     summary = create_summary(review)
#     print(f"Summary: {summary}")
