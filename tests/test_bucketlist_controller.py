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
