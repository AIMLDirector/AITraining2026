import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pickle

# Download resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Load dataset (update path if needed)
data = pd.read_csv("SMSSpamCollection",
                   sep='\t',
                   names=["label", "text"],
                   encoding="latin-1")

data.columns = ['label', 'text']
print(data.head())
print(data.columns)

# Preprocessing
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def clean_text(text):
    words = nltk.word_tokenize(text.lower())
    words = [lemmatizer.lemmatize(w) for w in words if w.isalpha() and w not in stop_words]
    return " ".join(words)

# Apply cleaning
data['text'] = data['text'].apply(clean_text)

# Label encoding
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    data['text'], data['label'], test_size=0.2, random_state=42)

# Vectorizer
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

# Model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Save .pkl files
pickle.dump(model, open("spam_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print(" Model training complete and .pkl files saved!")
