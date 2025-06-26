🧠 AI Testcase Optimizer

AI Testcase Optimizer is a tool designed to automatically optimize test cases using artificial intelligence. It helps QA engineers reduce the volume of test data without losing functional coverage.

⸻

🚀 Features
 • Automatically reduces duplicated or redundant test cases
 • Integrates with OpenAI API for intelligent analysis
 • Easy-to-run interface with CSV files
 • Flexible configuration via .env file

⸻

📁 Project Structure

AI-Testcase-Optimizer/
├── app.py           # Main script that processes the CSV file
├── app.env          # Local environment file for storing the API key (do not push!)
├── .gitignore       # Ignores app.env, __pycache__, etc.
├── Samples/         # Example input files
└── README.md        # Project information

⚙️ Setup
 1. Clone the repository:

git clone https://github.com/TravieCooper/AI-Testcase-Optimizer.git

2. Install dependencies:

pip install -r requirements.txt

3. Create a .env file based on app.env:

OPENAI_API_KEY=your_openai_api_key_here

4. Run the script:

python app.py

📌 Requirements
 • Python 3.8+
 • Access to OpenAI API
 • CSV file with test cases

⸻

📬 Contact

This project was created for educational purposes.
For ideas, improvements, or inquiries, feel free to reach out.
