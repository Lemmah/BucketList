# Test or Define a bucketlist Item

import unittest
from app.bucketlist_item import BucketListItem


class TestBucketListItem(unittest.TestCase):
    ''' Testing the bucketlist item object '''

    def setUp(self):
        ''' Initializing reusable variables '''
        self.bucketlist_item_details = ("bucketlist_item_name", "category", "description: optional", "bucketlist_id")
        self.bucketlist_item = BucketListItem(self.bucketlist_item_details)
