from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)


openai.api_key = "gsk_ВАШ_API_КЛЮЧ"  # Замініть на ваш API ключ


@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    if request.method == "POST":
        prompt = request.form["prompt"]

        if not prompt or len(prompt.strip()) < 10:
            response_text = "⚠️ Введіть запит довжиною не менше 10 символів."
        else:
            try:
                completion = openai.ChatCompletion.create(
                    model="openchat/openchat-3.5",  # Якщо це OpenAI модель
                    messages=[
                        {"role": "system", "content": "Ти допомагаєш аналізувати тест-кейси."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=512
                )
                response_text = completion.choices[0].message["content"].strip()
            except Exception as e:
                response_text = f"❌ Помилка: {str(e)}"

    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
