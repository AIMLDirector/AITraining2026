import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
stop_words = stopwords.words('english')
sentence1 = "This is a sample sentence, showing off the stop words filtration."
word_sentence1 = word_tokenize(sentence1)
print(word_sentence1)
filtered_sentence1 = []

for i in word_sentence1:
    if i not in stop_words:
        filtered_sentence1.append(i)

print(filtered_sentence1)
# filtered_sentence2 = [i for i in word_sentence2 if i not in stop_words]
