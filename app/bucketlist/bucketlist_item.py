# A bucketlist item and all it's attributes

class BucketListItem:
    ''' This is the bucketlist item object '''

    def __init__(self, name, category, description=None, status=None, bucketlist=None):
        ''' Constructing the bucketlist item while handling possible exceptions '''
        self.name = name
        self.category = category
        self.description = description
        self.bucketlist_id = bucketlist
        if status is None:
            self.status = "in_progress"
        else:
            self.status = status

    def change_status(self):
        ''' toggle the status of a bucketlist item '''
        if self.status == "done":
            self.status == "in_progress"
        else:
            self.status = "done"
        return self.status

    def __repr__(self):
        ''' Item representation '''
        return self.name
