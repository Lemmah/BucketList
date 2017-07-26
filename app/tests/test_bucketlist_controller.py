# Testing the super class that performs CRUD operations

import unittest
from app.bucketlist.bucketlist_controller import BucketListController
from app.bucketlist.bucketlist import BucketList


class TestBucketListController(unittest.TestCase):
    ''' Testing the control bucketlist feature '''
    # This class is just a layer that enable the user to control their bucketlists

    def setUp(self):
        ''' Initializing reusable variables '''
        self.test_user = "Test User"
        self.bucketlist_controller = BucketListController(self.test_user)
        self.bucketlist_details = ("ItemName", "Description: optional")
        self.bucketlist = BucketList(*self.bucketlist_details, owner=self.test_user)

    # 1. Test successfull instantiation
    def test_bucketlist_controller_creation(self):
        ''' Asserting that a bucketlist controller can be created '''
        self.assertEqual(isinstance(self.bucketlist_controller, BucketListController), True)

    def test_bucketlist_controller_has_available_bucketlists(self):
        ''' Asserting that the bucketlist controller knows about available bucketlists '''
        self.assertEqual(isinstance(self.bucketlist_controller.available_bucketlists, list), True)

    # 2. Test bucketlist controller operations
    def test_bucketlist_controller_can_create_bucketlist(self):
        ''' Asserting that a bucketlist controller can create a bucketlist '''
        new_bucketlist_details = ("NewName", "Description: Optional")
        new_bucketlist = self.bucketlist_controller.add_bucketlist(new_bucketlist_details)
        self.assertEqual(isinstance(new_bucketlist[0], BucketList), True)
        self.assertEqual(new_bucketlist[1], "{} bucketlist has been created".format(new_bucketlist_details[0]))

    def test_bucketlist_controller_can_update_bucketlist(self):
        ''' Asserting that bucketlist controller can change bucketlist details '''
        new_details = ("New Name", "New Description")
        update_bucketlist = self.bucketlist_controller.change_bucketlist_details(self.bucketlist, new_details)
        self.assertEqual(update_bucketlist, "{} has been updated accordingly".format(self.bucketlist.name))

    def test_bucketlist_controller_can_delete_bucketlist(self):
        ''' Asserting that a bucketlist controller can delete a bucketlist '''
        # add set up test bucketlist to list of available bucketlists
        self.bucketlist_controller.available_bucketlists.append(self.bucketlist)
        # remember it's name
        bucketlist_name = self.bucketlist.name
        delete_bucketlist = self.bucketlist_controller.delete_bucketlist(self.bucketlist)
        self.assertEqual(delete_bucketlist,"Successfully deleted {} bucketlist".format(bucketlist_name))
