from flask import session
from flask import request
from flask import flash
from flask import render_template, redirect, url_for
from app.bucketlist.bucketlist import BucketList
from app.bucketlist.bucketlist_controller import BucketListController
from app.user.user import User

from app import app
# List of registered users for non-persistent data
registered_users = []

def get_session_user():
    ''' Get the object of the session user '''
    for user in registered_users:
        if user.email == session['user']:
            return user

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
              session['logged_in'] = True
              session['user'] = email
              return redirect(url_for("dashboard"))
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
  session['logged_in'] = False
  return render_template("index.html")

# Bucketlist CRUD
@app.route('/dashboard/')
def dashboard():
  ''' Dashboard for user interaction with bucketlist: has a list of bucketlists '''
  if session['logged_in']:
      if get_session_user() is not None:
          no_bucketlists = (len(get_session_user().available_bucketlists) == 0)
          session_user = get_session_user()
          return render_template("dashboard.html", username=get_session_user().name, no_bucketlists=no_bucketlists, session_user=session_user)
      else:
          flash("Your session has expired.")
          return render_template("index.html")
  flash("You are not logged in. Please log in.")
  return render_template("index.html")

@app.route('/dashboard/create_bucketlist/', methods=['POST'])
def create_bucketlist():
  ''' Create bucketlist from form data '''
  name = request.form.get('bucketlist_name')
  description = request.form.get('bucketlist_desc')
  bucketlist_details = (name, description)
  if get_session_user is not None:
      create_bucketlist = get_session_user().add_bucketlist(bucketlist_details)
      flash(create_bucketlist[1])
      return redirect("dashboard/")
  flash("Your session has expired.")
  return render_template("index.html")

@app.route('/dashboard/bucketlists/<bucketlist_name>/delete/')
def delete_bucketlist(bucketlist_name):
  ''' Deletes the bucketlist with the name name '''
  if get_session_user is not None:
      session_user = get_session_user()
      for bucketlist in session_user.available_bucketlists:
          if str(bucketlist) == bucketlist_name:
              delete_bucketlist = session_user.delete_bucketlist(bucketlist)
              flash(delete_bucketlist)
              return redirect("/dashboard/")
  flash("The bucketlist you are trying to delete is not available")
  return redirect("/dashboard/")

@app.route('/dashboard/bucketlists/<bucketlist_name>/update/', methods=['POST'])
def update_bucketlist_details(bucketlist_name):
  ''' Updates the bucketlist details from a form '''
  name = request.form.get('bucketlist_name')
  description = request.form.get('bucketlist_desc')
  bucketlist_details = (name, description)
  if get_session_user is not None:
      session_user = get_session_user()
      for bucketlist in session_user.available_bucketlists:
          if str(bucketlist) == bucketlist_name:
              update_bucketlist = session_user.change_bucketlist_details(bucketlist, bucketlist_details)
              flash(update_bucketlist)
              return redirect("dashboard/")
  flash("Your session has expired.")
  return render_template("index.html")

# Bucketlist Items CRUD
@app.route('/dashboard/bucketlists/<bucketlist_name>/')
def display_bucketlist_items(bucketlist_name):
    ''' Read bucketlist items and display them '''
    if session['logged_in']:
      if get_session_user() is not None:
          session_user = get_session_user()
          for bucketlist in session_user.available_bucketlists:
              if str(bucketlist) == bucketlist_name:
                  target_index = session_user.available_bucketlists.index(bucketlist)
                  target_bucketlist = session_user.available_bucketlists[target_index]
                  items = target_bucketlist.items
                  empty_bucketlist = (len(items) == 0)
                  flash("You can control {} bucketlist items from here".format(target_bucketlist))
                  return render_template("manipulate_items.html",bucketlist=target_bucketlist, username=get_session_user().name, empty_bucketlist=empty_bucketlist, session_user=session_user)
      else:
          flash("Your session has expired.")
          return render_template("index.html")
    flash("You are not logged in. Please log in.")
    return render_template("index.html")

@app.route('/dashboard/bucketlists/<bucketlist_name>/add_item/', methods=['POST'])
def add_bucketlist_item(bucketlist_name):
  ''' Add item details to bucketlist_name from a form '''
  return "This is yet to be implemented"

@app.route('/dashboard/bucketlists/<bucketlist_name>/remove_item/<item_name>/')
def remove_bucketlist_item(bucketlist_name, item_name):
  ''' Remove item_name from bucketlist_name '''
  return "This is yet to be implemented"

@app.route('/dashboard/bucketlists/<bucketlist_name>/update_item/')
def update_bucketlist_item(bucketlist_name, item_details):
  ''' Update item_name in bucketlist_name with item_details '''
  return "This is yet to be implemented"

