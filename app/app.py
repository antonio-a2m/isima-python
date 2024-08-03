import json
from flask import Flask, json, render_template
app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def home():
    return render_template('index.html')

@app.route('/github', methods=('GET', 'POST'))
def github():
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
