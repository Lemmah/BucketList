# Tests for the class user

import unittest
from app.user.user import User
from app.bucketlist.bucketlist_controller import BucketListController
from app.bucketlist.bucketlist import BucketList


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
    self.bucketlist_details = ("ItemName", "Description: optional")
    self.bucketlist = BucketList(*self.bucketlist_details, owner=self.user_details[0])

  # 1. Test structure and user instance creation
  def test_user_inherits_bucketlistcontroler(self):
    ''' Test that user inherits bucketlist controller '''
    # Assert that it's a user instance
    self.assertEqual(isinstance(self.user_instance, User), True)
    # Assert that it's also a bucketlist controller instance
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
  # 2. Test bucketlist controller operations
  def test_user_can_create_bucketlist(self):
      ''' Asserting that a bucketlist controller can create a bucketlist '''
      new_bucketlist_details = ("NewName", "Description: Optional")
      new_bucketlist = self.user_instance.add_bucketlist(new_bucketlist_details)
      self.assertEqual(isinstance(new_bucketlist[0], BucketList), True)
      self.assertEqual(new_bucketlist_details[0] in self.user_instance.available_bucketlists, True)
      self.assertEqual(new_bucketlist[1], "{} bucketlist has been created".format(new_bucketlist_details[0]))

  def test_user_instance_can_update_bucketlist(self):
      ''' Asserting that bucketlist controller can change bucketlist details '''
      # rename, change details
      new_name, new_description = "NewBucket", "NewDetails: This is new"
      old_name = self.bucketlist.name
      rename = self.user_instance.rename_bucketlist(self.bucketlist, new_name)
      self.assertEqual(rename, "{} bucketlist has been renamed to {}".format(old_name, new_name))
      self.assertEqual(self.bucketlist.name, new_name)
      change_details = self.user_instance.change_bucketlist_details(self.bucketlist, new_description)
      self.assertEqual(change_details, "{} has been updated accordingly".format(self.bucketlist.name))
      self.assertEqual(self.bucketlist.description, new_description)

  def test_user_instance_can_delete_bucketlist(self):
      ''' Asserting that a bucketlist controller can delete a bucketlist '''
      # add set up test bucketlist to list of available bucketlists
      self.user_instance.available_bucketlists.append(self.bucketlist.name)
      self.assertEqual(self.bucketlist.name in self.user_instance.available_bucketlists, True)
      delete_bucketlist = self.user_instance.delete_bucketlist(self.bucketlist)
      self.assertEqual(self.bucketlist.name not in self.user_instance.available_bucketlists, True)
      self.assertEqual(str(self.bucketlist), 'Bucketlist does not exist')
