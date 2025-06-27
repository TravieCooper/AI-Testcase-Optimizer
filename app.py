from huggingface_hub import InferenceClient
import os
import pandas as pd
from dotenv import load_dotenv

# Завантаження токена
load_dotenv('app.env')
huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")

if huggingface_api_key is None:
    print("API ключ Hugging Face не знайдений!")
    exit()

# CSV
df = pd.read_csv("samples/CSV-файли/sample_testcases.csv")
testcases = df.to_dict(orient="records")

# Формуємо запит
prompt = "Analyze these test cases. Point out duplicates, inaccuracies, and how to improve:\n\n"
for case in testcases:
    prompt += f"ID: {case['ID']}, Title: {case['Title']}, Steps: {case['Steps']}, Expected: {case['Expected Result']}\n"

# Hugging Face client з перевіреною моделлю
client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.1",
    token=huggingface_api_key
)

response = client.text_generation(
    prompt=prompt,
    max_new_tokens=300,
    temperature=0.7,
    top_p=0.9,
)

print("\n--- Hugging Face Chat Response ---\n")
print(response)

