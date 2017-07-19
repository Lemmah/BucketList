# Test or Define a bucketlist Item

import unittest
from app.bucketlist_item import BucketListItem


class TestBucketListItem(unittest.TestCase):
    ''' Testing the bucketlist item object '''

    def setUp(self):
        ''' Initializing reusable variables '''
        self.bucketlist_item_details = ("bucketlist_item_name", "category", "description: optional", "bucketlist_id")
        self.bucketlist_item = BucketListItem(self.bucketlist_item_details)

        # 1. Ensure that a bucketlist item is created
        def test_bucketlist_item_created(self):
            ''' Ensuring that a bucketlist item has been instantiated '''
            assertTrue(isinstance(self.bucketlist_item, BucketListItem))

        def test_bucketlist_item_belongs_to_bucketlist(self):
            ''' Ensuring that the bucketlist_id is not None '''
            assertNotTrue(isinstance(self.bucketlist_item.bucketlist_id, None))

        def test_bucketlist_item_has_status(self):
            ''' Assert that bucketlist_item is either done or in_progress '''
            assertNotTrue(isinstance(self.bucketlist_item.status, None))
