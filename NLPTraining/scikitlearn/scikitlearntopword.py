import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Sample text documents
documents = [
    "Machine learning enables computers to learn from data.",
    "Deep learning is a part of machine learning that uses neural networks.",
    "Natural language processing helps computers understand text and speech."
]

# Create TF-IDF Vectorizer
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(documents)

# Function to extract top keywords for each document
def get_top_keywords(model, feature_names, top_n=5):
    keywords_list = []
    for doc_idx in range(model.shape[0]):
        row = model[doc_idx].toarray().flatten()
        top_indices = row.argsort()[-top_n:][::-1]
        keywords = [feature_names[i] for i in top_indices]
        keywords_list.append(keywords)
    return keywords_list

feature_names = vectorizer.get_feature_names_out()
keywords = get_top_keywords(X, feature_names)

# Display the result
for i, kw in enumerate(keywords):
    print(f"\nDocument {i+1} Top Keywords:")
    print(", ".join(kw))
