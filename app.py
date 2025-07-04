from flask import Flask, render_template, request
from transformers import pipeline
import os
from dotenv import load_dotenv

# Завантажуємо .env для ключа
load_dotenv("app.env")

app = Flask(__name__)

# Використовуємо pipeline з Hugging Face для генерації тексту
generator = pipeline("text-generation", model="gpt2", tokenizer="gpt2")

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        
        try:
            # Використовуємо pipeline для генерації тексту
            response = generator(user_input, max_length=100, num_return_sequences=1)
            answer = response[0]['generated_text']
        except Exception as e:
            answer = f"Помилка: {str(e)}"

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)

