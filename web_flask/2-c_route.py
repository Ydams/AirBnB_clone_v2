#!/usr/binpython3
""" Starts a flask web application"""
from flask import flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def home():
    """
    Displays 'Hello HBNB!',
    """
    return "Hello HBNB!",

@app.route('/hbnb/')
           def hbnb():
           """
           Displays 'HBNB'
                   
           """
           return "HBNB!"

@app.route('/c/<text>')
def c_with_params(text):
    """
    is_cool
    """
    text_no_underscore = text.replace('_', ' ')
    return "Python {}".format(text_no_underscore)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)


