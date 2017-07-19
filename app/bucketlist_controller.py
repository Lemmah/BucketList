# This is the super class, Controlling all the operations on the bucketlist and bucketlist items

from app.bucketlist import BucketList


class BucketListController:
    ''' Perfoming CRUD operations on bucket lists '''

    def __init__(self, user):
        ''' Construct the bucketlist controller '''
        self.user = user
        self.available_bucketlists = []

    def add_bucketlist(self, bucketlist_details):
        ''' Functionality to create new bucketlist '''
        owner = self.user
        bucketlist_name = bucketlist_details[0]
        if bucketlist_name in self.available_bucketlists:
            raise Exception("A bucketlist with the name {} already exists")
        # add name of new bucketlist to list of available bucketlists
        self.available_bucketlists.append(bucketlist_details[0])
        new_bucketlist = BucketList(*bucketlist_details, owner=self.user)
        return (new_bucketlist, "{} bucketlist has been created".format(bucketlist_name))
