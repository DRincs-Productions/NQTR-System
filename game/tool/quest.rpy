init python:
    class Goal(object):
        """Goal class, it has been designed to be included in the Quest class"""
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
            """Adds in element to the target, then checks the completion status. In case a need is null completes the mission. Returns True if the mission has been completed"""
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
        """Quest class: using external variables quest_current, task_current, stage_memory and bl."""
        def __init__(self,
            id_stageOrTask,
            goals = [],
            title = None,
            description = None,
            advice = None,
            bg = None,
            day_start = None,
            bl_requests = [],
            stage_level_requests = {},
            description_request = None,
            label_start = None,
            label_end = None,
            label_check = None):

            self.id_stageOrTask = id_stageOrTask
            self.goals = goals
            self.active = False
            self.title = title
            self.description = description
            self.advice = advice
            self.bg = bg
            self.day_start = day_start
            # These are the requirements to start the quest
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
            quest_current[id_stageOrTask] = Quest(
                id_stageOrTask = self.id_stageOrTask,
                goals = self.goals,
                day_start = self.day_start,
                bl_requests = self.bl_requests,
                stage_level_requests = self.stage_level_requests,
                description_requests = self.description_requests,
                label_start = self.label_start,
                label_end = self.label_end,
                label_check = label_check)
            self.start()
        def insertTask(self):
            """Insert the quest in the current Tasks"""
            task_current[id_stageOrTask] = Quest(
                id_stageOrTask = self.id_stageOrTask,
                goals = self.goals,
                day_start = self.day_start,
                bl_requests = self.bl_requests,
                stage_level_requests = self.stage_level_requests,
                description_requests = self.description_requests,
                label_start = self.label_start,
                label_end = self.label_end,
                label_check = label_check)
            self.start()
        def start(self):
            """If you have reached all the objectives then activate the Quest."""
            if (self.request_check() == False):
                return False
            # if (label_start != None)
                # TODO: Execute label_start
            self.active == True
            # TODO: notify
            return True
        def request_check(self):
            """Checks the requests, returns True if it satisfies them."""
            for stage, level in stage_level_requests.items():
                if (stage_level[stage] < level):
                    return False
            for item in bl_requests:
                if (bl[item] == False):
                    return False
            return True
        def completed(self):
            """Check completed and if it is complete -> next_quest()"""
            # if (label_check != None)
                # TODO: Execute label_check
            if not goals:
                self.next_quest()
                return True
            for x in goals:
                if (x.complete_check() == False):
                    return False
            self.next_quest()
            return True
        def next_quest(self):
            """If it is a quest is replaced by the next quest, and if it is a Task is deleted."""
            # if (label_end != None)
                # TODO: Execute label_end
            if (self.id_stageOrTask in task_current):
                del task_current[id_stageOrTask]
                return
            stage_memory[id_stageOrTask].next_quest()
        def find(self, quest_id, value=1):
            """Execute find() in Goal with id == quest_id"""
            for x in goals:
                if (x.id == quest_id):
                    x.find(value)
                    return True
            return False

    class Stage(object):
        """Internship a short story of Quest that follow each other between. This class makes use of: quest_list, stage_level"""
        def __init__(self,
            id,
            title,
            icon = None,
            quest_list = [],
            category = None,
            development = False):

            self.id = id
            self.title = title
            self.icon = icon
            self.quest_list = quest_list
            self.category = category
            self.development = development
        def is_completed(self):
            """Check if all quests have been completed."""
            if ((self.id in stage_level) == False):
                updateStageCompL()
                return False
            if len(self.quest_list) == stage_level[self.id]:
                return True
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
            """Function to update the various values"""
            if ((self.id in stage_level) == False):
                self.update()
            if (self.is_completed() or stage_level[id] == 0):
                return
            if ((self.id in current_quest) == False):
                self.next_quest()
        def start(self, n_quest):
            """Insert the quest number n_quest in the current quests"""
            quest_memory[self.quest_list[n_quest]].insertQuest()
        def next_quest(self):
            """Go to the next quest"""
            if ((self.id in stage_level) == False):
                self.update()
            if self.is_completed():
                return
            stage_level[id] +=1
            self.start(stage_level[id])
        def is_started(self):
            if ((self.id in stage_level) == False):
                self.update()
            return (self.id in current_quest)
    def updateStageCompL():
        """Synchronize stage_level with stage_memory."""
        # check if there are less elements than bl_list
        # in case you add them set with False
        for x in stage_memory:
            if ((x in stage_level) == False):
                stage_level[x] = 0
        # check if there are more elements than bl_list
        # in case it eliminates them
        for x in stage_level:
            if ((x in stage_memory) == False):
                stage_level.remove(x)
        return
