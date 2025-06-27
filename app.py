import pandas as pd
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceApi

# Завантаження змінних середовища з файлу .env
load_dotenv('app.env')

# API ключ Hugging Face
huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")

if huggingface_api_key is None:
    print("API ключ Hugging Face не знайдений! Перевірте файл .env.")
    exit()

df = pd.read_csv("samples/CSV-файли/sample_testcases.csv")
testcases = df.to_dict(orient="records")

prompt = "Analyze these test cases. Point out duplicates, inaccuracies, and how to improve:\n\n"
for case in testcases:
    prompt += f"ID: {case['ID']}, Title: {case['Title']}, Steps: {case['Steps']}, Expected: {case['Expected Result']}\n"

huggingface_inference = InferenceApi(repo_id="your_hugging_face_model", token=huggingface_api_key)

huggingface_response = huggingface_inference(inputs=prompt)

print("\n--- Hugging Face Response ---\n")
print(huggingface_response['generated_text'])

