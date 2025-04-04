from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Aleksey'}
    posts = [
        {
            'author' : {'username' : 'Vladislav'},
            'body' : 'New Features MacOS.'
        },
        {
            'author' : {'username' : 'Aleksander'},
            'body' : 'POSIX Std.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)