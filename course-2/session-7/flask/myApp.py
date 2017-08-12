#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask import session
from flask import make_response
from flask import redirect
from flask import abort

print('Starting flask app named {}'.format(__name__))
app = Flask(__name__)

@app.route('/')
def index():
    response = '''
    <html>
    <head>
    <title>Hello you!</title>
    </head>
    <body>
    <h1>Hello World!!!</h1>
    <p>
    You're coming to me via {}
    With full request details:
    {}
    With session:
    {}
    </p>
    </body>
    </html>
    '''
    user_agent = request.headers.get('User-Agent')
    response = response.format(user_agent,request.headers,session)
    response = make_response(response)
    response.set_cookie('answer', '42')
    return response

@app.route('/help')
def help_index():
    response = '''
    <html>
    <head>
    <title>Support</title>
    </head>
    <body>
    <h1>Call your parents.</h1>
    </body>
    </html>
    '''
    return response

@app.route('/user/names/<name>')
def user(name):
    response = '''
    <html>
    <head>
    <title>Support</title>
    </head>
    <body>
    <h1>Call your parents, {}!</h1>
    </body>
    </html>
    '''
    response = response.format(name)
    return response

@app.route('/redirect')
def redirect_me():
    return redirect('http://www.nyu.edu')

def load_user(id):
    print(type(id))
    if (int(id) == 1):
        return 'rob'
    else:
        return None

@app.route('/user/ids/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(403)
    return '<h1>Hello, %s</h1>' % user

if __name__ == '__main__':
    # main line
    app.run(host='0.0.0.0',debug=False)
    #app.run(debug=True)

