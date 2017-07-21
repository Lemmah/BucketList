# Testing the workings of a bucketlist
import unittest
from app.bucketlist import BucketList
from app.bucketlist_item import BucketListItem


class TestBucketList(unittest.TestCase):
    ''' Testing or defining the bucketlist '''

    def setUp(self):
        ''' Instatiating reusable variables '''
        self.bucketlist_owner = "Test Owner"
        self.new_bucketlist = BucketList("Test Bucket", owner=self.bucketlist_owner)
        self.new_item_details = ("ItemName", "Category", "Description: optional")

    # 1. Tests for successful creating of a new_bucketlist instance
    def test_bucketlist_is_created(self):
        ''' Checking that bucketlist has been created '''
        self.assertEqual(isinstance(self.new_bucketlist, BucketList), True)

    def test_bucketlist_has_id(self):
        ''' Asserting that any bucketlist created has an id '''
        self.assertNotEqual(self.new_bucketlist.bucket_id, None)

    def test_bucketlist_items_is_list(self):
        ''' Asserting that a bucketlist can take a list of items '''
        self.assertEqual(isinstance(self.new_bucketlist.items, list), True)

    def test_bucketlist_has_owner(self):
        ''' Asserting that each bucketlist has an owner '''
        self.assertNotEqual(self.new_bucketlist.owner, None)

    # 2. Tests for bucketlist behaviors
    def test_add_bucketlist_item(self):
        ''' Testing adding items to a bucketlist '''
        # see that an item has been added successfully by message return
        new_item = self.new_bucketlist.add_item(self.new_item_details, self.bucketlist_owner)
        self.assertEqual(new_item[1], "ItemName added successfully")
        # ensure that it is indeed in the list of items
        self.assertIn(self.new_item_details[0], self.new_bucketlist.items)
        # check and ascertain that a bucketlist_item object is created
        self.assertEqual(isinstance(new_item[0], BucketListItem), True)

    def test_update_bucketlist_item_details(self):
        ''' Testing for updating bucketlist item details '''
        # This depends on successful creation of a new item
        new_item = self.new_bucketlist.add_item(self.new_item_details, self.bucketlist_owner)
        # The new item object is returned by the add_item method in a tuple at the first index
        # So,
        new_item = new_item[0]  # ommitting the success message
        # First check that the new item is indeed a BucketListItem
        self.assertEqual(isinstance(new_item, BucketListItem), True)
        # unpark the details
        item_name, category, description = new_item.name, new_item.category, new_item.description
        # confirming that name is as in new_item_details
        self.assertEqual(item_name, self.new_item_details[0])
        # Test for changing the all the item details
        new_item.name, new_item.category, new_item.description = "ChangedName", "ChangedCategory", "ChangedDescription"
        self.assertEqual((new_item.name, new_item.category, new_item.description), ("ChangedName", "ChangedCategory", "ChangedDescription"))
        self.assertNotEqual(item_name, new_item.name)

    def test_remove_bucketlist_item(self):
        ''' Testing that items are removed from the list '''
        # Create item before removal
        new_item = self.new_bucketlist.add_item(self.new_item_details, self.bucketlist_owner)
        # self.assert message returned on removal
        remove_item = self.new_bucketlist.remove_item(self.new_item_details[0])
        self.assertEqual(remove_item, "ItemName removed successfully")
        # ensure that the item is no longer in the list
        self.assertEqual(self.new_item_details[0] in self.new_bucketlist.items, False)

    # 3. Testing for handling of edge cases
    def test_adding_same_bucketlist_items_twice(self):
        ''' Ensuring user cannot the same item to a bucketlist twice '''
        # create a bucketlist item
        new_item = self.new_bucketlist.add_item(self.new_item_details, self.bucketlist_owner)
        # ensure that calling the add_item method with the same details raises and exception
        self.assertRaises(Exception, self.new_bucketlist.add_item, self.new_item_details)

    def test_deleting_non_existing_bucketlist_item(self):
        ''' Testing that non-existing items do not get other items deleted '''
        # Ensure that removing an item that does not exist raises an error
        self.assertRaises(Exception, self.new_bucketlist.remove_item, self.new_item_details[0])

