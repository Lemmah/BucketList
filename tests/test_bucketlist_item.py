# Test or Define a bucketlist Item

import unittest
from app.bucketlist_item import BucketListItem


class TestBucketListItem(unittest.TestCase):
    ''' Testing the bucketlist item object '''

    def setUp(self):
        ''' Initializing reusable variables '''
        self.name, self.category, self.description, self.bucketlist = "bucketlist_item_name", "category", "description: optional", "bucketlist_id"
        self.bucketlist_item = BucketListItem(self.name, self.category, self.description, bucketlist=self.bucketlist)

    # 1. Ensure that a bucketlist item is created
    def test_bucketlist_item_created(self):
        ''' Ensuring that a bucketlist item has been instantiated '''
        self.assertTrue(isinstance(self.bucketlist_item, BucketListItem))

    def test_bucketlist_item_belongs_to_bucketlist(self):
        ''' Ensuring that the bucketlist_id is not None '''
        self.assertNotEqual(self.bucketlist_item.bucketlist_id, None)

    def test_bucketlist_item_has_status(self):
        ''' self.assert that bucketlist_item is either done or in_progress '''
        self.assertNotEqual(self.bucketlist_item.status, None)

    # 2. Test bucketlist item behaviours
    def test_bucketlist_item_change_status(self):
        ''' Test that status of bucketList can change from done to in_progress and viceversa '''
        bucketlist_item_status = self.bucketlist_item.status.lower()
        if bucketlist_item_status == "done":
            self.bucketlist_item.change_status()
            bucketlist_item_status = self.bucketlist_item.status.lower()
            self.assertNotEqual(bucketlist_item_status == "done", True)
        else:
            self.bucketlist_item.change_status()
            bucketlist_item_status = self.bucketlist_item.status.lower()
            self.assertEqual(bucketlist_item_status, "done")

