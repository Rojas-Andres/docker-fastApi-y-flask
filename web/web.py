from flask import Flask,render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    url = 'http://fast-api/frutas'
    reponse = requests.get(url)
    reponse_json = json.loads(reponse.text)
    return render_template('index.html',context=reponse_json)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)