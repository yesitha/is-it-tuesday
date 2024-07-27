from flask import Flask
import datetime

__maintainer__ = "hasithsen - sen dot hasith at gmail"

app = Flask(__name__)

@app.route("/")
def main():
    is_it_tuesday = "yes!" if datetime.datetime.now().strftime("%a") == "Tue" else "no" 
    return f"<span style="text-align: center;">Is it Tuesday? <b>{ is_it_tuesday }</b></span><hr /><code>{ datetime.datetime.now().isoformat() }</code>"
