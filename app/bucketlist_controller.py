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

    def rename_bucketlist(self, target_bucketlist, new_name):
        ''' Functionality to rename a bucketlist '''
        old_name = target_bucketlist.name
        # change name in list of available bucketlists
        for bucketlist in self.available_bucketlists:
            if bucketlist == target_bucketlist.name:
                bucketlist = new_name
        # change name in bucketlist instance
        target_bucketlist.name = new_name
        return "{} bucketlist has been renamed to {}".format(old_name, new_name)

    def change_bucketlist_details(self, target_bucketlist, new_bucketlist_description):
        ''' Functionality to update bucketlist description '''
        target_bucketlist.description = new_bucketlist_description
        return "{} has been updated accordingly".format(target_bucketlist.name)

    def delete_bucketlist(self, bucketlist):
        ''' Functionality to delete bucketlist '''
        target_bucketlist = bucketlist
        self.available_bucketlists.remove(bucketlist.name)
        bucketlist.name = None
        return "Successfully deleted {} bucketlist".format(target_bucketlist)
