from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def main():
    is_it_tuesday = "yes!" if datetime.datetime.now().strftime("%a") == "Tue" else "no" 
    return f"Is it Tuesday? <b>{ is_it_tuesday }</b><hr /><code>{ datetime.datetime.now().isoformat() }</code>"
