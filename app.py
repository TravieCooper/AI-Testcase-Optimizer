from flask import Flask, render_template, request
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

# Завантаження змінних оточення з файлу .env
load_dotenv("app.env")

app = Flask(__name__)
client = InferenceClient(token=os.getenv("HUGGINGFACE_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        user_input = request.form["user_input"]

        try:
            # Виклик моделі для генерації тексту
            response = client.text_generation(
                model="tiiuae/falcon-7b-instruct",  # Використовуємо модель Falcon
                prompt=user_input,
                max_new_tokens=300,
                temperature=0.7,
                top_p=0.9,
            )
            
            # Зберігаємо результат у змінну, витягуючи відповідь з response
            answer = response["generated_text"] if "generated_text" in response else "Відповідь не знайдена."
            
        except Exception as e:
            # Якщо виникає помилка, виводимо її
            answer = f"Помилка: {str(e)}"

    # Повертаємо шаблон і передаємо відповідь
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
