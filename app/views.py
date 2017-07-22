from flask import request
from flask import render_template

from app import app

@app.route('/')
def index():
  ''' Loading the home page for user login or registration '''
  return render_template("index.html")

@app.route('/dashboard/')
def dashboard():
  ''' Dashboard for user interaction with bucketlist '''
  return render_template("dashboard.html")

@app.route('/logout/')
def logout():
  ''' Terminate session and return user to login page '''
  return render_template("index.html")

@app.route('/login/', methods=['POST'])
def login():
  ''' Validate user details from existing non-persistent data '''
  email = request.form.get('email')
  password = request.form.get('password')
  return "{} - {}".format(email, password)

@app.route('/register/', methods=['POST'])
def register():
  ''' Add user details to current block of non-persitent data '''
  email = request.form.get('email')
  password = request.form.get('password')
  name = request.form.get('username')
  return "{} - {} - {}".format(name, email, password)

# Bucketlist CRUD
@app.route('/dashboard/create_bucketlist/', methods=['POST'])
def create_bucketlist():
  ''' Create bucketlist from form data '''
  return "This is yet to be implemented"

@app.route('/dashboard/bucketlists/')
def show_bucketlists():
  ''' Render a list of bucketlists '''
  return "This is yet to be implemented"

@app.route('/dashboard/bucketlists/<bucketlist_name>/')
def display_bucketlist_details(bucketlist_name):
  ''' Display the details of a bucketlist '''
  return "This is yet to be implemented"

@app.route('/dashboard/bucketlists/<bucketlist_name>/delete/')
def delete_bucketlist(bucketlist_name):
  ''' Deletes the bucketlist with the name name '''
  return "This is yet to be implemented"

@app.route('/dashboard/bucketlists/<bucketlist_name>/update/', methods=['POST'])
def update_bucketlist_details(bucketlist_name, new_details):
  ''' Updates the bucketlist details from a form '''
  return "This feature is yet to be implemented"

# Bucketlist Items CRUD
@app.route('/dashboard/bucketlists/<bucketlist_name>/add_item/', methods=['POST'])
def add_bucketlist_item(bucketlist_name):
  ''' Add item details to bucketlist_name from a form '''
  return "This is yet to be implemented"

@app.route('/dashboard/bucketlists/<bucketlist_name>/remove_item/<item_name>/')
def remove_bucketlist_item(bucketlist_name, item_name):
  ''' Remove item_name from bucketlist_name '''
  return "This is yet to be implemented"

@app.route('/dashboard/bucketlists/<bucketlist_name>/update_item/<item_name>/<item_details>/')
def update_bucketlist_item(bucketlist_name, item_details):
  ''' Update item_name in bucketlist_name with item_details '''
  return "This is yet to be implemented"

