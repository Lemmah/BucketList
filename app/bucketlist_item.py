# A bucketlist item and all it's attributes


class BucketListItem:
    ''' Tis is the bucketlist item object '''

    def __init__(self, name, category, description=None, status=None, bucketlist=None):
        ''' Constructing the bucketlist item while handling possible exceptions '''
        # Ensure item belongs to a bucketlist
        if bucketlist is None:
            raise Exception("BucketList item must belong to a bucketlist")
        self.name = name
        self.category = category
        self.description = description
        self.bucketlist_id = bucketlist
        if status is None:
            self.status = "in_progress"
        else:
            self.status = status
