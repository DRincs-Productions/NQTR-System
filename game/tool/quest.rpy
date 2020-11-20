# Explanation of the operation of the Quests that are in task_current
# to simplify I call:
#   - stage_memory[x]: Stage
#   - quest_memory[x]: Qmemory
#   - quest_current[x]: Quest
#
# First phase (Initialize a Stage):
# Stage.start():                    # It is done manually
#   Qmemory.insertQuest()
#   Quest.start():                  # it is done until it becomes active with TODO: ... 
#       Quest.request_check():
#           Quest.active = True
#--------------------------------------------------------------------------
# Quest.completed_try():            # It is done manually
#   is_completed():
#       completed = True
#   if (completed):
#       Stage.next_quest():
#           if it's not the last quest:
#               Stage.start(next)   # Start the cycle again

init python:
    class Goal(object):
        """Goal class, it has been designed to be included in the Quest class.
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

    class Quest(object):
        """Quest class: using external variables quest_current, task_current, stage_memory, tm.day and bl.
        You can go to the next quest with completed_try(), forcibly with connext_quest()."""
        def __init__(self,
            id_stageOrTask,
            goals = [],
            title = None,
            description = None,
            advice = "",
            bg = None,
            days_late = None,
            bl_requests = [],
            stage_level_requests = {},
            description_request = "",
            label_start = None,
            label_end = None,
            label_check = None):

            self.id_stageOrTask = id_stageOrTask
            self.goals = goals
            self.active = False
            self.title = title
            self.description = description
            self.advice = advice
            self.completed = False
            self.bg = bg
            # These are the requirements to start the quest
            self.days_late = days_late
            self.day_start = None
            self.bl_requests = bl_requests
            self.stage_level_requests = stage_level_requests
            self.description_request = description_request
            # these labels will be started automatically at the appropriate time.
            # TODO: have not yet been implemented
            self.label_start = label_start
            self.label_end = label_end
            self.label_check = label_check

        def insertQuest(self):
            """Inserts the quest in the current Quests"""
            quest_current[self.id_stageOrTask] = Quest(
                id_stageOrTask = self.id_stageOrTask,
                goals = self.goals,
                bl_requests = self.bl_requests,
                stage_level_requests = self.stage_level_requests,
                description_request = self.description_request,
                label_start = self.label_start,
                label_end = self.label_end,
                label_check = self.label_check)
            quest_current[self.id_stageOrTask].setDay(self.days_late)
        def insertTask(self):
            """Insert the quest in the current Tasks"""
            task_current[self.id_stageOrTask] = Quest(
                id_stageOrTask = self.id_stageOrTask,
                goals = self.goals,
                bl_requests = self.bl_requests,
                stage_level_requests = self.stage_level_requests,
                description_request = self.description_request,
                label_start = self.label_start,
                label_end = self.label_end,
                label_check = self.label_check)
            quest_current[self.id_stageOrTask].setDay(self.days_late)
        def start(self):
            """If you have reached all the objectives then activate the Quest.
            start () is used until the quest becomes active"""
            if (self.active):
                return self.active
            if (self.request_check() == False):
                return False
            # if (label_start != None)
                # TODO: Execute label_start
            self.active = True
            # TODO: notify
            return True
        def request_check(self):
            """Checks the requests, returns True if it satisfies them."""
            if (self.day_start != None and tm.day < self.day_start):
                return False
            for stage, level in self.stage_level_requests.items():
                if (stage_level[stage] < level):
                    return False
            for item in self.bl_requests:
                if (bl_values[item] == False):
                    return False
            return True
        def completed_try(self):
            """Check completed and if it is complete -> next_quest()
            set complete = True if it can actually go ahead completed"""
            if (self.is_completed() == False):
                return False
            self.next_quest()
            return True
        def is_completed(self):
            """Check if the quest can be complete."""
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
        def next_quest(self):
            """If it is a quest is replaced by the next quest, and if it is a Task is deleted."""
            # if (label_end != None)
                # TODO: Execute label_end
            if (self.id_stageOrTask in task_current):
                del task_current[id_stageOrTask]
                return
            stage_memory[self.id_stageOrTask].next_quest()
        def find(self, quest_id, value=1):
            """Execute find() in Goal with id == quest_id"""
            for x in goals:
                if (x.id == quest_id):
                    x.find(value)
                    return True
            return False
        def setDay(self, days_late):
            """Execute find() in Goal with id == quest_id"""
            if (days_late != None):
                self.day_start = (tm.day + days_late)

    class Stage(object):
        """Internship a short story of Quest that follow each other between. This class makes use of: quest_list, stage_level.
        Must be initialized manually with start()"""
        def __init__(self,
            id,
            title,
            description = "",
            icon = None,
            bg = None,
            quest_list = [],
            category = None,
            development = False):

            self.id = id
            self.title = title
            self.description = description
            self.icon = icon
            self.bg = bg
            self.quest_list = quest_list
            self.category = category
            self.development = development
        def is_completed(self):
            """Check if all quests have been completed."""
            if ((self.id in stage_level) == False):
                updateStageCompL()
                return False
            if len(self.quest_list)-1 == stage_level[self.id]:
                return current_quest[self.id].completed
            else:
                return False
        def current_quest(self):
            """Return the id of this current"""
            if ((self.id in stage_level) == False):
                self.update()
            return self.quest_list[stage_level[id]]
        def quest_completed_number(self):
            """Returns the number of completed quests"""
            if ((self.id in stage_level) == False):
                self.update()
            return stage_level[id]
        def get_percentage_completion(self):
            """Returns the percentage of completion"""
            if ((self.id in stage_level) == False):
                self.update()
            return stage_level[id]/len(self.quest_list)*100
        def update(self):
            """Function to update the various values,
            If it is a completed stage and a quest has been added in a new update, the new quest begins.
            Prevent errors like blocked stages."""
            if (self.is_completed()):
                return
            if ((self.id in current_quest) == False and stage_level[self.id] == 0):
                return
            # if the stage has been started, but there is no current_quest, it restarts the Stage from 0
            if ((self.id in current_quest) == False):
                self.start()
                return
            # if you have somehow exceeded the number of quests
            if len(self.quest_list)-1 < stage_level[self.id]:
                stage_level[self.id] = len(self.quest_list)-1
                return
            # if it is a completed stage and a quest has been added in a new update
            if self.is_completed() == False and current_quest[self.id].completed:
                self.next_quest()
                return
        def start(self, n_quest=0):
            """Insert the quest number n_quest in the current quests"""
            quest_memory[self.quest_list[n_quest]].insertQuest()
            quest_current[self.id].start()
            stage_level[self.id] = n_quest
        def next_quest(self):
            """Go to the next quest"""
            if ((self.id in stage_level) == False):
                self.update()
            if len(self.quest_list)-1 == stage_level[self.id]:
                return
            stage_level[self.id] +=1
            self.start(stage_level[self.id])
        def is_started(self):
            if ((self.id in stage_level) == False):
                self.update()
            return (self.id in current_quest)
    def updateStageCompL():
        """Synchronize stage_level with stage_memory."""
        # check if there are less elements than bl_memory
        # in case you add them set with False
        for x in stage_memory.keys():
            if ((x in stage_level) == False):
                stage_level[x] = 0
        # check if there are more elements than bl_memory
        # in case it eliminates them
        for x in stage_level.keys():
            if ((x in stage_memory) == False):
                stage_level.remove(x)
        return
