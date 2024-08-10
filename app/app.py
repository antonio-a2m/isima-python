import json
from flask import Flask, json, render_template
import githubClass
app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def home():
    return render_template('index.html')

@app.route('/github', methods=('GET', 'POST'))
def github():
    obj= githubClass.GithubClient()
    userRes=obj.queryUser()
    return userRes
    
@app.route('/misdatos', methods=('GET', 'POST'))
def githubdatos():
    obj= githubClass.GithubClient()
    userRes=obj.queryUser()
    if not "name" in userRes:
        return "<h2>El token no jala</h2>"
    else:
        html="<h2>{}</h2><h4>{}</h4><img src={}>".format(userRes["name"],userRes["bio"],userRes["avatar_url"])
    return html

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
