#  This is the structure of the bucketlist

from app.bucketlist_item import BucketListItem


class BucketList:
    ''' The bucketlist object '''

    def __init__(self, name, details=None, items=None, owner=None):
        ''' Constructing and instance of the object '''
        # Every bucketlist must have an owner
        if owner is None:
            raise Exception("Every bucketlist must have an owner")
        self.name = name
        self.details = details
        if items is not None:
            self.items = items
        else:
            self.items = []
        self.owner = owner
