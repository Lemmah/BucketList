from flask import request
from flask import render_template

from app import app

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/dashboard')
def dashboard():
  return render_template("dashboard.html")

@app.route('/logout')
def logout():
  return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')
    return "{} - {}".format(email, password)
  else:
    return "Something went wrong with the post method."

@app.route('/register', methods=['POST'])
def register():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')
    name = request.form.get('username')
    return "{} - {} - {}".format(name, email, password)
  else:
    return "Something went wrong with the post method."

