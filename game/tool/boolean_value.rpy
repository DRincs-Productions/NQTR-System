# IMPORTANT: insert updateBL() in start or before using bl
# bl are Boolean values, a good use is for example in quests to know quickly if MC has the possibility to do a certain thing, after unlocking it somehow.
# has the same alements as bl_list, all set as False
# I suggest to leave it empty and add the elements only if it is an initial value and set as True
default bl = {}
define bl_list = [
    # Block all actions with check_block_spendtime
    "block_spendtime",
]

init python:
    def updateBL():
        """update bl by making it with the same elements of bl_list. in case you have to add them set them as False"""
        # check if there are less elements than bl_list
        # in case you add them set with False
        for x in bl_list:
            if ((x in bl) == False):
                bl[x] = False
        # check if there are more elements than bl_list
        # in case it eliminates them
        for x in bl:
            if ((x in bl_list) == False):
                bl.remove(a)
        return
