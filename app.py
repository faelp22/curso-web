from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=('GET',))
def hello():
    print('====================================================')
    print(request.headers)
    print('====================================================')
    return render_template('index.html')
    
