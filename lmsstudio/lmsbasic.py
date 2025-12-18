import lmstudio as lms

with lms.Client() as client:
    model = client.llm.model()
    print(model.respond("What is the meaning of life?"))