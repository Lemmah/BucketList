# Test or Define a bucketlist Item

import unittest
from app.bucketlist_item import BucketListItem


class TestBucketListItem(unittest.TestCase):
    ''' Testing the bucketlist item object '''

    def setUp(self):
        ''' Initializing reusable variables '''
        self.bucketlist_item_details = "bucketlist_item_name", "category", "description: optional", "bucketlist_id"
        self.bucketlist_item = BucketListItem("bucketlist_item_name", "category", "description: optional", "bucketlist_id")

    # 1. Ensure that a bucketlist item is created
    def test_bucketlist_item_created(self):
        ''' Ensuring that a bucketlist item has been instantiated '''
        assertEqual(isinstance(self.bucketlist_item, BucketListItem), True)

    def test_bucketlist_item_belongs_to_bucketlist(self):
        ''' Ensuring that the bucketlist_id is not None '''
        assertNotTrue(isinstance(self.bucketlist_item.bucketlist_id, None))

    def test_bucketlist_item_has_status(self):
        ''' Assert that bucketlist_item is either done or in_progress '''
        assertNotTrue(isinstance(self.bucketlist_item.status, None))

    # 2. Test bucketlist item behaviours
    def test_bucketlist_item_change_status(self):
        ''' Test that status of bucketList can change from done to in_progress and viceversa '''
        bucketlist_item_status = self.bucketlist_item.status.lower()
        if bucketlist_item_status == "done":
            self.bucketlist_item.change_status()
            bucketlist_item_status = self.bucketlist_item.status.lower()
            assertNotTrue(bucketlist_item_status == "done")
        else:
            self.bucketlist_item.change_status()
            bucketlist_item_status = self.bucketlist_item.status.lower()
            assertEqual(bucketlist_item_status, "done")

    # 3. Handling edge cases
    def test_bucketlist_item_duplicate_item(self):
        ''' Test that duplicate bucketlist_items raise exception '''
        # creating a bucketlist with existing details
        duplicate_bucketlist_item = BucketListItem(self.bucketlist_item_details)
        assertTrue(isinstance(duplicate_bucketlist_item, Exception))
