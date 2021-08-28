# IMPORTANT: insert updateBL() in start or before using bl_values
# bl_values are Boolean values, a good use is for example in quests to know quickly if MC has the possibility to do a certain thing, after unlocking it somehow.
# has the same alements as bl_memory, all set as False
# I suggest to leave it empty and add the elements only if it is an initial value and set as True
default bl_values = {}
define bl_memory = [
    # Block all actions with check_block_spendtime
    "block_spendtime",
    "goout",
]

init python:
    def updateBL():
        """update bl_values by making it with the same elements of bl_memory. in case you have to add them set them as False"""
        # check if there are less elements than bl_memory
        # in case you add them set with False
        for x in bl_memory:
            if ((x in bl_values) == False):
                bl_values[x] = False
        # check if there are more elements than bl_memory
        # in case it eliminates them
        for x in bl_values:
            if ((x in bl_memory) == False):
                del bl_values[x]
        return
