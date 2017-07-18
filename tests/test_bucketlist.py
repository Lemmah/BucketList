# Testing the workings of a bucketlist
import unittest
from app.bucketlist import BucketList

class TestBucketList(unittest.TestCase):
    ''' Testing or defining the bucketlist '''

    def setUp(self):
        ''' Instatiating reusable variables '''
        self.new_bucketlist = BucketList("Test Bucket")

    #1. Tests for successful creating of a new_bucketlist instance
    def test_bucketlist_is_created(self):
        ''' Checking that bucketlist has been created '''
        assertTrue(isinstance(self.new_bucketlist, "BucketList"))

    def test_bucketlist_has_id(self):
        ''' Asserting that any bucketlist created has an id '''
        assertNotEqual(self.new_bucketlist.bucket_id, None)

    def test_bucketlist_items_is_list(self):
        ''' Asserting that a bucketlist can take a list of items '''
        assertTrue(isinstance(self.new_bucketlist.items, list))

    def test_bucketlist_has_owner(self):
        ''' Asserting that each bucketlist has an owner '''
        assertNotTrue(isinstance(self.new_bucketlist.owner, None))

    #2. Tests for bucketlist behaviors
    def test_add_bucketlist_item(self):
        ''' Testing adding items to a bucketlist '''
        # see that an item has been added successfully by message return
        assertEqual(self.new_bucketlist.add_item("ItemName", "Category", "Description: optional"), "ItemName added successfully")
        # ensure that it is indeed in the list of items
        assertIn("ItemName", self.new_bucketlist.items)

    def test_update_bucketlist_item_details(self):
        ''' Testing for updating bucketlist item details '''
        # This will require me to implement the bucketlist item object first
        pass

    def test_remove_bucketlist_item(self):
        ''' Testing that items are removed from the list '''
        # assert message returned on removal
        assertEqual(self.new_bucketlist.remove_item("ItemName", "Category", "Description: optional"), "ItemName added successfully")
        # ensure that the item is no longer in the list
        assertNotIn("ItemName", self.new_bucketlist.items)
