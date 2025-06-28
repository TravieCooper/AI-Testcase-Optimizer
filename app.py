from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient


app = Flask(__name__)


load_dotenv("app.env")
huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")


if huggingface_api_key is None:
    raise ValueError("HUGGINGFACE_API_KEY не знайдено в .env файлі!")


client = InferenceClient(token=huggingface_api_key)

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    if request.method == "POST":
        user_prompt = request.form["user_input"]

        
        try:
            response = client.text_generation(
                model="tiiuae/falcon-7b-instruct",
                prompt=user_prompt,
                max_new_tokens=300,
                temperature=0.7,
                top_p=0.9,
            )
            response_text = response
        except Exception as e:
            response_text = f"⚠️ Помилка: {str(e)}"

    return render_template("index.html", response=response_text)


if __name__ == "__main__":
    app.run(debug=True)
