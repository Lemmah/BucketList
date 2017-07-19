# This is the super class, Controlling all the operations on the bucketlist and bucketlist items

from app.bucketlist import BucketList


class BucketListController:
    ''' Perfoming CRUD operations on bucket lists '''

    def __init__(self, user):
        ''' Construct the bucketlist controller '''
        self.user = user
        self.available_bucketlists = []
