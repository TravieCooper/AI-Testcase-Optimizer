print(">>> Запуск app.py")
from flask import Flask, render_template, request
import os
import openai

app = Flask(__name__)

# Встанови свій GROQ API ключ
openai.api_key = "ТУТ_ТВІЙ_GROQ_API_KEY"
openai.api_base = "https://api.groq.com/openai/v1"

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        prompt = request.form["prompt"]
        if not prompt or len(prompt.strip()) < 10:
            response = "❗ Введіть більш детальний запит (мін. 10 символів)."
        else:
            try:
                completion = openai.ChatCompletion.create(
                    model="openchat/openchat-3.5",
                    messages=[
                        {"role": "system", "content": "Ти QA-спеціаліст. Аналізуй тест-кейси, вказуй помилки або покращення."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=512
                )
                response = completion.choices[0].message["content"]
            except Exception as e:
                response = f"❌ Помилка: {str(e)}"
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)


