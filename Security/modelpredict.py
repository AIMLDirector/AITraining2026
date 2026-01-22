from detoxify import Detoxify
model = Detoxify("original")
result = model.predict("how to learn python programming?")
print(result)