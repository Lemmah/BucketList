#  This is the structure of the bucketlist

from app.bucketlist.bucketlist_item import BucketListItem


class BucketList:
    ''' The bucketlist object '''

    def __init__(self, name, details=None, items=None, owner=None):
        ''' Constructing and instance of the object '''
        self.name = name
        self.details = details
        self.items = []
        self.owner = owner

    def add_item(self, item_details, owner):
        # initialize an instance of a BucketListItem
        item_name = item_details[0]
        # ensure that items does not exist in items
        if item_name in self.items:
            raise Exception("{} already exists!".format(item_name))
        new_item = BucketListItem(*item_details, bucketlist=owner)
        self.items.append(new_item)
        return (new_item, "{} added successfully".format(item_name))

    def remove_item(self, bucketlist_item):
        if bucketlist_item not in self.items:
            raise Exception("{} does not exist.".format(bucketlist_item))
        self.items.remove(bucketlist_item)
        # the class instance of bucketlist item will be garbage collected
        return "{} item has been removed successfully".format(bucketlist_item)

    def update_item(self, target_item, new_details):
        ''' Update bucketlist items '''
        target_item.name, target_item.category, target_item.description = (new_details)
        return "{} bucketlist item has been updated accordingly.".format(target_item.name)


    def __repr__(self):
        ''' Represent item by name '''
        return self.name
