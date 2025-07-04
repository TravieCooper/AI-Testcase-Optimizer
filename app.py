from flask import Flask, render_template, request
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv
import traceback

load_dotenv("app.env")

app = Flask(__name__)
client = InferenceClient(token=os.getenv("HUGGINGFACE_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        user_input = request.form["user_input"]

        try:
            response = client.text_to_text(
            model="google/flan-t5-large",
            inputs=user_input,
            )
            answer = response
        except Exception as e:
            traceback.print_exc()
            answer = f"Помилка: {str(e)}"

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
