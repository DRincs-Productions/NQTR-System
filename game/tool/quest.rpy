# Explanation of the operation of the Stages that are in current_task_stages
# to simplify I call:
#   - quests[x]: Quest
#   - quest_stages[x]: Stage
#   - current_quest_stages[x]: currentStage
#
# First phase (Initialize a Stage):
# Quest.start():                    # It is done manually
#   Stage.addInQuest()
#   currentStage.start():                  # it is done until it becomes active with TODO: ... 
#       currentStage.request_check():
#           currentStage.active = True
#--------------------------------------------------------------------------
# currentStage.completed_try():            # It is done manually
#   is_completed():
#       completed = True
#   if (completed):
#       Quest.next_stage():
#           if it's not the last quest:
#               Quest.start(next)   # Start the cycle again

init python:
    class Goal(object):
        """Goal class, it has been designed to be included in the Stage class.
        To complete the goals use find()"""
        def __init__(self,
            id,
            description,
            complete = False,
            need = None,
            have = 0):

            self.id = id
            self.description = description
            self.complete = complete
            self.need = need
            self.have = 0

        def find(self, value=1):
            """Adds in element to the target, then checks the completion status. In case a need is null completes the mission. Returns True if the mission has been completed.
            It is used to complete the Goals."""
            if (need == None):
                self.complete = True
            self.have += value
            if (self.complete_check()):
                self.complete = True
                # Todo: notify description
                return True
            return False
        def complete_check(self):
            """Checks the status of completion. returns True if the mission has been completed"""
            if (complete == True):
                return True
            if (need == None):
                return False
            return self.need <= self.have

    class Stage(object):
        """Stage class: using external variables current_quest_stages, current_task_stages, quests, tm.day and bl.
        You can go to the next Stage with Stage.completed_try(), forcibly with Stage.next_stage()."""
        def __init__(self,
            idQuestOrTask,
            goals = [],
            title = None,
            description = None,
            advice = "",
            bg = None,
            days_late = None,
            bl_requests = [],
            quests_levels_requests = {},
            description_request = "",
            label_start = None,
            label_end = None,
            label_check = None):

            self.idQuestOrTask = idQuestOrTask
            self.goals = goals
            self.active = False
            self.title = title
            self.description = description
            self.advice = advice
            self.completed = False
            self.bg = bg
            # These are the requirements to start the Stage
            self.days_late = days_late
            self.day_start = None
            self.bl_requests = bl_requests
            self.quests_levels_requests = quests_levels_requests
            self.description_request = description_request
            # these labels will be started automatically at the appropriate time.
            # TODO: have not yet been implemented
            self.label_start = label_start
            self.label_end = label_end
            self.label_check = label_check

        def addInQuest(self):
            """Add the Stage in the current_quest_stages"""
            current_quest_stages[self.idQuestOrTask] = Stage(
                idQuestOrTask = self.idQuestOrTask,
                goals = self.goals,
                bl_requests = self.bl_requests,
                quests_levels_requests = self.quests_levels_requests,
                description_request = self.description_request,
                label_start = self.label_start,
                label_end = self.label_end,
                label_check = self.label_check)
            current_quest_stages[self.idQuestOrTask].setDay(self.days_late)
        def addInTask(self):
            """Add the Stage in the current_task_stages"""
            current_task_stages[self.idQuestOrTask] = Stage(
                idQuestOrTask = self.idQuestOrTask,
                goals = self.goals,
                bl_requests = self.bl_requests,
                quests_levels_requests = self.quests_levels_requests,
                description_request = self.description_request,
                label_start = self.label_start,
                label_end = self.label_end,
                label_check = self.label_check)
            current_task_stages[self.idQuestOrTask].setDay(self.days_late)
        def start(self):
            """If you have reached all the objectives then activate the Stage.
            start() is used until the Stage becomes active.
            TODO: WARNING: there is an error because after "call expression self.label_start" it doesn't go on, so:
            the only thing that happens is that it doesn't return anything. (for now I don't know how serious is this error)"""
            if (self.active):
                return self.active
            if (self.request_check() == False):
                return False
            if (self.label_start != None):
                self.active = True
                renpy.call(self.label_start)
            self.active = True
            # TODO: notify
            return True
        def request_check(self):
            """Checks the requests, returns True if it satisfies them."""
            if (self.day_start != None and tm.day < self.day_start):
                return False
            for quest, level in self.quests_levels_requests.items():
                if (quests_levels[quest] < level):
                    return False
            for item in self.bl_requests:
                if (bl_values[item] == False):
                    return False
            return True
        def completed_try(self):
            """Check completed and if it is complete -> next_stage()
            set complete = True if it can actually go ahead completed"""
            if (self.is_completed() == False):
                return False
            self.next_stage()
            return True
        def is_completed(self):
            """Check if the Stage can be complete."""
            # if (label_check != None)
                # TODO: Execute label_check
            if (self.completed):
                return True
            if (self.active == False):
                if (self.start() == False):
                    return False
            if self.goals:
                for x in self.goals:
                    if (x.complete_check() == False):
                        return False
            self.completed = True
            # self.completed_try()
            return True
        def next_stage(self):
            """If it is a Quest is replaced by the next Quest, and if it is a Task is deleted."""
            # if (label_end != None)
                # TODO: Execute label_end
            if (self.idQuestOrTask in current_task_stages):
                del current_task_stages[self.idQuestOrTask]
                return
            quests[self.idQuestOrTask].next_stage()
        def find(self, goals_id, value=1):
            # TODO: To comment and test
            for item in self.goals:
                if (item.id == goals_id):
                    item.find(value)
                    return True
            return False
        def setDay(self, days_late):
            # TODO: To comment
            if (days_late != None):
                self.day_start = (tm.day + days_late)

    class Quest(object):
        """Internship a short story of Quest that follow each other between. This class makes use of: stages, quests_levels.
        Must be initialized manually with start()"""
        def __init__(self,
            id,
            title,
            description = "",
            icon = None,
            bg = None,
            stages_id = [],
            category = None,
            development = False):

            self.id = id
            self.title = title
            self.description = description
            self.icon = icon
            self.bg = bg
            self.stages_id = stages_id
            self.category = category
            self.development = development
        def is_completed(self):
            """Check if all stages have been completed."""
            if ((self.id in quests_levels) == False):
                updateQuestsLevels()
                return False
            if len(self.stages_id)-1 == quests_levels[self.id]:
                return current_quest_stages[self.id].completed
            else:
                return False
        def current_quest_id(self):
            """Return the id of this current"""
            if ((self.id in quests_levels) == False):
                self.update()
            return self.stages_id[quests_levels[id]]
        def complete_stages_number(self):
            """Returns the number of completed stages"""
            if ((self.id in quests_levels) == False):
                self.update()
            return quests_levels[id]
        def get_percentage_completion(self):
            """Returns the percentage of completion"""
            if ((self.id in quests_levels) == False):
                self.update()
            return quests_levels[id]/len(self.stages_id)*100
        def update(self):
            """Function to update the various values,
            If it is a completed Quest and a Stage has been added in a new update, the new Stage begins.
            Prevent errors like blocked Quests."""
            if (self.is_completed()):
                return
            if ((self.id in current_quest_stages) == False and quests_levels[self.id] == 0):
                return
            # if the Quest has been started, but there is no current_quest_stages, it restarts the Quest from 0
            if ((self.id in current_quest_stages) == False):
                self.start()
                return
            # if you have somehow exceeded the number of stages
            if len(self.stages_id)-1 < quests_levels[self.id]:
                quests_levels[self.id] = len(self.stages_id)-1
                return
            # if it is a completed Quest and a Stage has been added in a new update
            if self.is_completed() == False and current_quest_stages[self.id].completed:
                self.next_stage()
                return
        def start(self, n_stage=0):
            """Insert the Stage number n_stage in the current quests"""
            quest_stages[self.stages_id[n_stage]].addInQuest()
            current_quest_stages[self.id].start()
            quests_levels[self.id] = n_stage
        def next_stage(self):
            """Go to the next Stage, in case it is the last, it does not go on but the sect as complete."""
            if ((self.id in quests_levels) == False):
                self.update()
            if len(self.stages_id)-1 == quests_levels[self.id]:
                current_quest_stages[self.id].completed = True
                return
            quests_levels[self.id] +=1
            self.start(quests_levels[self.id])
        def is_started(self):
            if ((self.id in quests_levels) == False):
                self.update()
            return (self.id in current_quest_stages)
        # TODO: add: def delete(self):
            # removes it from current_quest_stages
            # removes it from quests_levels

    # TODO: Use it when: Load Menu
    def updateQuestsLevels():
        """Synchronize quests_levels with quests.
        After this function I suggest to use checkInactiveStage()."""
        # check if there are less elements than bl_memory
        # in case you add them set with False
        for x in quests.keys():
            if ((x in quests_levels) == False):
                quests_levels[x] = 0
        # check if there are more elements than bl_memory
        # in case it eliminates them
        for x in quests_levels.keys():
            if ((x in quests) == False):
                quests_levels.remove(x)
        return

    # this function is done in the transition from one day to another
    def checkInactiveStage():
            """Check if the inactive Stage have the requirements to be activated, if so, activate them."""
            for k in current_quest_stages.keys():
                current_quest_stages[k].start()
            for k in current_task_stages.keys():
                current_task_stages[k].start()
            return

# TODO: Add the following functions
    # check if current_quest_stages.key is in quests, if not there delete it: Load Game
    # for is_completed()
    # compare current_quest_stages current_task_stages if in current_quest_stages ce an extra quest is deleted
