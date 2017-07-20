from flask import Flask
from flask import render_template
from flask import request, redirect, url_for

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    ''' Rendering like the homepage  where user can login/register'''
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    ''' Rendering a specific user dashboard '''
    return render_template('dashboard.html')



if __name__ == "__main__":
    ''' modularization for importation '''
    app.run()
