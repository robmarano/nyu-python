#!/usr/bin/env python3

from flask import Flask

print('Starting flask app named {}'.format(__name__))
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    # main line
    app.run(host='0.0.0.0',debug=True)
