# Tests for the class user

import unittest
from app.user.user import User


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
    self.assertEqual(isinstance(self.user_instance, BucketListController.User), True)

  def test_user_has_all_properties(self):
    ''' Ensure user has name, email, password '''
    assertEqual(self.user_instance.name, self.user_details[2])
    assertEqual(self.user_instance.email, self.user_details[0])
    assertEqual(self.user_instance.password, self.user_details[1])

  
