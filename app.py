import pandas as pd
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient


load_dotenv('app.env')

huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")

if huggingface_api_key is None:
    print("API ключ Hugging Face не знайдений! Перевірте файл .env.")
    exit()

df = pd.read_csv("samples/CSV-файли/sample_testcases.csv")
testcases = df.to_dict(orient="records")

prompt = "Analyze these test cases. Point out duplicates, inaccuracies, and how to improve:\n\n"
for case in testcases:
    prompt += f"ID: {case['ID']}, Title: {case['Title']}, Steps: {case['Steps']}, Expected: {case['Expected Result']}\n"

from huggingface_hub import InferenceClient


client = InferenceClient(token=huggingface_api_key)

response = client.chat.completions.create(
    model="google/gemma-3n-E2B-it",
    messages=[{"role": "user", "content": prompt}],
)


print("\n--- Hugging Face Chat Response ---\n")
print(response.choices[0].message.content)
