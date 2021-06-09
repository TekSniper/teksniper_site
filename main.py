from flask import *

ts = Flask(__name__)

@ts.route('/')
@ts.route('/home')
def index():
    return render_template('home.html')

@ts.route('/about')
def apropos():
    return render_template('about.html')

@ts.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    ts.run(debug = True)