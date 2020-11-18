# Quest

# quest_memory: is the list of all existing quest tasks.
# it is used to keep all information about all quests

# quest_current: are the quest currently active,
# contains only the data strictly necessary for proper operation
# after their completion they are replaced with the next one

# Task
# task_current is identical to this_current, 
# except that after completion they are not replaced by the next one, but eliminated. 
# The idea is that the Tasks are not within the "Stage" and therefore have no subsequent internships.

# Stage
# the Stage is a list of quests that follow each other according to their order
# stage_memory and stage_level are synchronized, meaning they will always have the same elements

# stage_level: must not have elements at the beginning. what is it for? to know which number of this has arrived at an internship
# quest_memory is similar to quest_memory and contains information about internships

default stage_level = {}
default quest_current = {}
default task_current = {}

define stage_memory = {}
define quest_memory = {}
