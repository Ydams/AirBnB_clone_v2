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
    Displays 'C'followed by the value of <text>.
    """
    text_no_underscore = text.replace('_', ' ')
    return "C {}".format(text_no_underscore)

@app.route('/python', defaults={'text':'is_cool'})
@app.route('/python/<text>'):
def python_with_text_param(text):
    """
    Displays 'python' followed by the value of the <text>

    Displays any underscores in <text> with slashes.
    """
    text_no_underscore = text.replace('_',' ')
    return "python{}".format(text_no_underscore)

@app.route('/number/<int:n>')
def number(n):
    """

    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """

    """
    return render_template('5-number.html', number=n)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
~                                           
