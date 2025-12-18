import os
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}

    ],
    max_tokens=100,
    temperature=0.7  # 1 is more creative, 0 is more focused

)

story_text = response.choices[0].message.content
print(story_text)
# output = response
# print(output)