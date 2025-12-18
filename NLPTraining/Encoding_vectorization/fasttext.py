from gensim.models import FastText

sentences = [
    ["i", "love", "playing", "football"],
    ["football", "and","basketball","is", "a", "great", "game"]
]

model = FastText(
    sentences,
    vector_size=100,
    window=5,
    min_count=1,
    sg=1  # Skip-gram
)

print(model.wv.most_similar("football"))
print(model.wv["playing"])