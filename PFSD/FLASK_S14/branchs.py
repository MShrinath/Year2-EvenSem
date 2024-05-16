from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/cse')
def cse():
    return 'CSE PAGE'

@app.route('/ece')
def ece():
    return 'ECE PAGE'

@app.route('/csit')
def csit():
    return 'CSIT PAGE'

if __name__ == '__main__':
    app.run(debug=True)