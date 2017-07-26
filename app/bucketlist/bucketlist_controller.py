# This is the super class, Controlling all the operations on the bucketlist and bucketlist items

from app.bucketlist.bucketlist import BucketList


class BucketListController:
    ''' Perfoming CRUD operations on bucket lists '''

    def __init__(self, user):
        ''' Construct the bucketlist controller '''
        self.user = user
        self.available_bucketlists = []

    def add_bucketlist(self, bucketlist_details):
        ''' Functionality to create new bucketlist '''
        bucketlist_name = bucketlist_details[0]
        if bucketlist_name in self.available_bucketlists:
            raise Exception("A bucketlist with the name {} already exists")
        # add name of new bucketlist to list of available bucketlists
        new_bucketlist = BucketList(*bucketlist_details, owner=self.user)
        self.available_bucketlists.append(new_bucketlist)
        return (new_bucketlist, "{} bucketlist has been created".format(new_bucketlist))

    def change_bucketlist_details(self, target_bucketlist, new_bucketlist_details):
        ''' Functionality to update bucketlist details '''
        target_bucketlist.name, target_bucketlist.details = (new_bucketlist_details)
        return "{} has been updated accordingly".format(target_bucketlist.name)

    def delete_bucketlist(self, bucketlist):
        ''' Functionality to delete bucketlist '''
        self.available_bucketlists.remove(bucketlist)
        return "Successfully deleted {} bucketlist".format(bucketlist)
