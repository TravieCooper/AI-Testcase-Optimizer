from flask import Flask, render_template, request
from transformers import pipeline, set_seed
import torch

app = Flask(__name__)

# Налаштування моделі GPT-2
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Device set to use {device}")
generator = pipeline("text-generation", model="gpt2", tokenizer="gpt2", device=0 if device.type == "cuda" else -1)
set_seed(42)

def generate_response(prompt):
    result = generator(
        prompt,
        max_new_tokens=256,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.9,
        truncation=True,
        pad_token_id=50256
    )
    return result[0]["generated_text"]

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        prompt = request.form["prompt"].strip()

        if len(prompt) < 10:
            result = "⚠️ Введений текст занадто короткий. Будь ласка, введіть більше деталей."
        else:
            result = generate_response(prompt)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)


