# Testing the super class that performs CRUD operations

import unittest
from app.control_bucketlist import BucketListController
from app.bucketlist import BucketList


class TestBucketListController:
    ''' Testing the control bucketlist feature '''
    # This class is just a layer that enable the user to control their bucketlists

    def setUp(self):
        ''' Initializing reusable variables '''
        self.test_user = "Test User"
        self.bucketlist_controller = BucketListController(self.test_user)
        self.bucketlist_details = ("ItemName", "Category", "Description: optional")
        self.bucketlist = BucketList(self.bucketlist_details, self.test_user)

    # 1. Test successfull instantiation
    def test_bucketlist_controller_creation(self):
        ''' Asserting that a bucketlist controller can be created '''
        assertTrue(isinstance(bucketlist_controller, BucketListController))

    def test_bucketlist_controller_has_available_bucketlists(self):
        ''' Asserting that the bucketlist controller knows about available bucketlists '''
        assertTrue(isinstance(BucketListController.available_bucketlists, list))

    # 2. Test bucketlist controller operations
    def test_bucketlist_controller_can_create_bucketlist(self):
        ''' Asserting that a bucketlist controller can create a bucketlist '''
        new_bucketlist_details = ("NewName", "NewCategory", "Description: Optional")
        new_bucketlist = self.bucketlist_controller.add_bucketlist(new_bucketlist_details, self.test_user)
        assertTrue(isinstance(new_bucketlist, BucketList))

    def test_bucketlist_controller_can_update_bucketlist(self):
        ''' Asserting that bucketlist controller can change bucketlist details '''
        pass

    def test_bucketlist_controller_can_delete_bucketlist(self):
        ''' Asserting that a bucketlist controller can delete a bucketlist '''
        bucketlist_name = self.bucketlist_details[0]
        delete_bucketlist = self.bucketlist_controller.delete_bucketlist(bucketlist_name)
        assertEqual(self.bucketlist, None)
