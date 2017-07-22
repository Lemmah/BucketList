# Tests for the class user

import unittest
from app.user.user import User
from app.bucketlist.bucketlist_controller import BucketListController


class TestUser(unittest.TestCase):
  '''
    A user is a bucketlist controller
    A user is has a name, email and password
    A user can do everything a bucketlist controller does
  '''

  def setUp(self):
    ''' Set up reusable variables and instances '''
    self.user_details = ("jnlemayian@gmail.com", "Password", "James Lemayian")
    self.user_instance = User(*self.user_details)

  # 1. Test structure and user instance creation
  def test_user_inherits_bucketlistcontroler(self):
    ''' Test that user inherits bucketlist controller '''
    # Assert that it's a user instance
    self.assertEqual(isinstance(self.user_instance, User), True)
    # Assert that it's also a bucketlist instance
    self.assertEqual(isinstance(self.user_instance, BucketListController), True)

  def test_user_has_all_properties(self):
    ''' Ensure user has name, email, password '''
    self.assertEqual(self.user_instance.name, self.user_details[2])
    self.assertEqual(self.user_instance.email, self.user_details[0])
    self.assertEqual(self.user_instance.password, self.user_details[1])

  def test_user_representation(self):
    ''' Assert that __repr__ function returns a useful object representation '''
    self.assertEqual(str(self.user_instance), "James Lemayian")

  ## The user is just an extension of the bucketlist controller
