from flask import flask

app = flask.Flask(__name__)

# This is the home page of our flask code and it will return a string when we will hit the home page of our flask app
@app.route('/')
def home():
    return 'Hello user , Myself Rakesh sahu and i welcome to my flask learning journey!'


# This is the about page of our flask code and it will return a string when we will hit the about page of our flask app
@app.route('/about')
def about():
    return 'This is the about page of our flask app and here we will learn about flask and its fundamentals!'


#  This is the contact page of our flask code and it will return a string when we will hit the contact page of our flask app
@app.route('/contact')
def contact():
    return 'This is the contact page of our flask app and here we will learn about flask and its fundamentals!' 


# This is the services page of our flask code and it will return a string when we will hit the services page of our flask app
@app.route('/services')
def services():
    return 'This is the services page of our flask app and here we will learn about flask and its fundamentals!'


# This is the products page of our flask code and it will return a string when we will hit the products page of our flask app
@app.route('/products')
def products():
    return 'This is the products page of our flask app and here we will learn about flask and its fundamentals!'

