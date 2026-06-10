import os
from flask import Flask
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

app = Flask(__name__)

@app.route('/')
def home():
    proj_name = os.environ.get("PROJECT_NAME", "Training")
    print(Fore.GREEN + Style.BRIGHT + f"Successfully verified core foundations for project: {proj_name}")
    return f"<h1>🚀 CI/CD AUTOMATION LOOP COMPLETED SUCCESSFULLY, BRO!!! 🚀</h1>"

if __name__ == "__main__":
    # This keeps the container alive and listening for cloud web traffic!
    app.run(host="0.0.0.0", port=5000)
