# Testing the super class that performs CRUD operations

import unittest
from app.control_bucketlist import BucketlistController
from app.bucketlist import BucketList

class TestBucketlistController:
    ''' Testing the control bucketlist feature '''
    # This class is just a layer that enable the user to control their bucketlists
    def setUp(self):
        self.test_user = "Test User"
        self.bucket_controller = BucketlistController(self.test_user)
        self.bucketlist_details = ("ItemName", "Category", "Description: optional")
        self.bucketlist = BucketList(self.bucketlist_details, self.test_user)
