from flask import session
from flask import request
from flask import flash
from flask import render_template
from app.bucketlist.bucketlist import BucketList
from app.bucketlist.bucketlist_controller import BucketListController
from app.user.user import User

from app import app
# List of registered users for non-persistent data
registered_users = []

@app.route('/logout/')
def logout():
  ''' Terminate session and return user to login page '''
  # Set session to false for logout
  session['logged_in'] = False
  session.pop('user', None)
  flash("You are logged out.")
  return render_template("index.html")

@app.route('/login/', methods=['POST'])
def login():
  ''' Validate user details from existing non-persistent data '''
  email = request.form.get('email')
  password = request.form.get('password')
  for user in registered_users:
      if user.email == email:
          if user.password == password:
              flash("Login successful")
              # After validation, set session to True
              session['logged_in'] = True
              session['user'] = email
              return render_template("dashboard.html")
          else:
              flash("Wrong Username or Password")
              return render_template("index.html")
  flash("You are not a registered user. Please register.")
  return render_template("index.html")

@app.route('/register/', methods=['POST'])
def register():
  ''' Add user details to current block of non-persitent data '''
  email = request.form.get('email')
  password = request.form.get('password')
  name = request.form.get('username')
  for user in registered_users:
      if user.email == email:
          flash("The email {} is already registered, login instead.".format(email))
          return render_template("index.html")
  user = User(email, password, name)
  registered_users.append(user)
  flash("Registration for {} was successfull, please login with details.".format(user.name))
  return render_template("index.html")

@app.route('/')
def index():
  ''' Loading the home page for user login or registration '''
  return render_template("index.html")

@app.route('/dashboard/')
def dashboard():
  ''' Dashboard for user interaction with bucketlist: has a list of bucketlists '''
  if session['logged_in']:
    return render_template("dashboard.html")
  flash("You are not logged in. Please log in.")
  return render_template("index.html")

# Bucketlist CRUD
@app.route('/dashboard/create_bucketlist/')
def create_bucketlist():
  ''' Create bucketlist from form data '''
  user = BucketListController("Test User")
  add_user = user.add_bucketlist(("Test", "Travelling"))
  bucketlist = add_user[0]
  success_message = add_user[1]
  return "BucketList: {} Description: {} Owner: {} :: {}".format(bucketlist.name, bucketlist.details, bucketlist.owner, success_message)

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

