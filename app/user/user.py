# Modelling a user
# A user is a bucketlist controller so,

from app.bucketlist.bucketlist_controller import BucketListController

class User(BucketListController):
  ''' A user who is also a bucketlist controller '''
  def __init__(self, email, password, name):
    ''' Construct an instance of a user '''
    BucketListController.__init__(self, email)
    self.name = name
    self.email = email
    self.password = password


