init python:
    from typing import Optional


    class Goal(object):
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#goal"""

        def __init__(self,
                    id: str,
                    description: str,
                    complete: bool = False,
                    need: int = 0,
                    have: int = 0):

            self.id = id
            self.description = description
            self.complete = complete
            self.need = need
            self.have = 0
            if (self.have < 0):
                self.have = 0
                renpy.log("Warn: You have set have < 0, so it will be set to 0.")
            if (self.need < 0):
                self.need = 0
                renpy.log("Warn: You have set need < 0, so it will be set to 0.")

        def find(self, value: int = 1):
            """Adds in element to the target, then checks the completion status. In case a need is null completes the mission. Returns True if the mission has been completed.
            It is used to complete the Goals."""
            if (self.need == 0):
                self.complete = True
            self.have += value
            if (self.isComplete()):
                self.complete = True
                # Todo: notify description
                return True
            return False

        def isComplete(self):
            """Checks the status of completion. returns True if the mission has been completed"""
            if (self.complete == True):
                return True
            if (self.need == 0):
                return False
            return self.need <= self.have


    class Stage(object):
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#stage """

        def __init__(self,
                    quest_id,
                    goals=[],
                    title=None,
                    description=None,
                    advice="",
                    bg=None,
                    waiting_days_before_start=None,
                    flags_requests=[],
                    quests_levels_requests={},
                    description_request="",
                    label_start=None, # Todo: implement this
                    label_end=None, # Todo: implement this
                    label_check=None, # Todo: implement this
                    ):

            self.quest_id = quest_id
            self.goals = goals
            self.active = False
            self.title = title
            self.description = description
            self.advice = advice
            self.completed = False
            self.bg = bg
            # These are the requirements to start the Stage
            self.waiting_days_before_start = waiting_days_before_start
            self.day_start = None
            self.flags_requests = flags_requests
            self.quests_levels_requests = quests_levels_requests
            self.description_request = description_request
            # these labels will be started automatically at the appropriate time.
            self.label_start = label_start
            self.label_end = label_end
            self.label_check = label_check

        def addInCurrentQuestStages(self):
            """Add the Stage in the current_quest_stages"""
            current_quest_stages[self.quest_id] = Stage(
                quest_id=self.quest_id,
                goals=self.goals,
                flags_requests=self.flags_requests,
                quests_levels_requests=self.quests_levels_requests,
                description_request=self.description_request,
                label_start=self.label_start,
                label_end=self.label_end,
                label_check=self.label_check)
            current_quest_stages[self.quest_id].setDay(
                self.waiting_days_before_start)

        def addInCurrentTaskStages(self):
            """Add the Stage in the current_task_stages, Task: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#task """
            current_task_stages[self.quest_id] = Stage(
                quest_id=self.quest_id,
                goals=self.goals,
                flags_requests=self.flags_requests,
                quests_levels_requests=self.quests_levels_requests,
                description_request=self.description_request,
                label_start=self.label_start,
                label_end=self.label_end,
                label_check=self.label_check)
            current_task_stages[self.quest_id].setDay(
                self.waiting_days_before_start)

        def start(self):
            """If you have reached all the objectives then activate the Stage.
            start() is used until the Stage becomes active."""
            if (self.active):
                return self.active
            if (not self.respectAllRequests()):
                return False
            # if (self.label_start != None):
            #     self.active = True
            #     renpy.call(self.label_start)
            self.active = True
            # TODO: notify
            return True

        def respectAllRequests(self):
            """Checks the requests, returns True if it satisfies them."""
            if (self.day_start != None and tm.day < self.day_start):
                return False
            for quest, level in self.quests_levels_requests.items():
                if (number_stages_completed_in_quest[quest] < level):
                    return False
            for item in self.flags_requests:
                if (not flags[item]):
                    return False
            return True

        def isCompleted(self):
            """Check if the Stage can be complete."""
            # if (label_check != None)
            if (self.completed):
                return True
            if (not self.active):
                if (not self.start()):
                    return False
            if self.goals:
                for x in self.goals:
                    if (not x.isComplete()):
                        return False
            self.completed = True
            return True

        def find(self, goals_id, value=1):
            for item in self.goals:
                if (item.id == goals_id):
                    item.find(value)
                    return True
            return False

        def addDaysWaitingBeforeStart(self, day):
            """Add days of waiting before it starts"""
            if (day != None):
                self.day_start = (tm.day + day)
            return

    class Quest(object):
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#quest 
        Task: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#task """

        def __init__(self,
                    id: str,
                    title: str,
                    description: str = "",
                    icon: str = None,
                    bg: str = None,
                    stages_id: Optional[list[str]] = None,
                    tag: str = None,
                    development: bool = False):

            self.id = id
            self.title = title
            self.description = description
            self.icon = icon
            self.bg = bg
            self.stages_id = self.stages_id = stages_id if stages_id else []
            self.tag = tag
            self.development = development

        def isCompleted(self):
            """Check if all stages have been completed."""
            if (not (self.id in number_stages_completed_in_quest)):
                updateQuestsLevels()
                return False
            if len(self.stages_id)-1 == number_stages_completed_in_quest[self.id]:
                return current_quest_stages[self.id].completed
            else:
                return False

        def currentQuestId(self):
            """Return the id of this current"""
            if (not (self.id in number_stages_completed_in_quest)):
                self.update()
            return self.stages_id[number_stages_completed_in_quest[id]]

        def completeStagesNumber(self):
            """Returns the number of completed stages"""
            if (not (self.id in number_stages_completed_in_quest)):
                self.update()
            return number_stages_completed_in_quest[id]

        def getPercentageCompletion(self):
            """Returns the percentage of completion"""
            if (not (self.id in number_stages_completed_in_quest)):
                self.update()
            return number_stages_completed_in_quest[id]/len(self.stages_id)*100

        def addDaysWaitingBeforeStart(self, day):
            """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#add-days-waiting-before-start """
            if (not (self.id in number_stages_completed_in_quest)):
                renpy.log("Warn: the Quest: "+self.id+" not is in number_stages_completed_in_quest, so i update it")
                self.update()
            return current_task_stages[self.id].addDaysWaitingBeforeStart()

        def update(self):
            """Function to update the various values,
            If it is a completed Quest and a Stage has been added in a new update, the new Stage begins.
            Prevent errors like blocked Quests."""
            if (self.isCompleted()):
                return
            if (not (self.id in current_quest_stages) and number_stages_completed_in_quest[self.id] == 0):
                return
            # if the Quest has been started, but there is no current_quest_stages, it restarts the Quest from 0
            if (not (self.id in current_quest_stages)):
                self.start()
                return
            # if you have somehow exceeded the number of stages
            if len(self.stages_id)-1 < number_stages_completed_in_quest[self.id]:
                number_stages_completed_in_quest[self.id] = len(self.stages_id)-1
                return
            # if it is a completed Quest and a Stage has been added in a new update
            if (not self.isCompleted()) and current_quest_stages[self.id].completed:
                self.afterNextStage()
                return

        def start(self, n_stage=0):
            """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#start-a-quest """
            quest_stages[self.stages_id[n_stage]].addInCurrentQuestStages()
            current_quest_stages[self.id].start()
            number_stages_completed_in_quest[self.id] = n_stage
            return

        def nextStageOnlyIsCompleted(self):
            """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#next-stage-only-it-is-completed """
            if (self.id in current_task_stages):
                if (not current_task_stages[self.id].isCompleted()):
                    return False
            elif (self.id in current_quest_stages):
                if (not current_task_stages[self.id].isCompleted()):
                    return False
            self.nextStage()
            return True

        def nextStage(self):
            """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#next-stage """
            if (self.id in current_task_stages):
                del current_task_stages[self.quest_id]
                return
            self.afterNextStage()
            return

        def afterNextStage(self):
            if (not (self.id in number_stages_completed_in_quest)):
                renpy.log("Warn: the Quest: "+self.id+" not is in number_stages_completed_in_quest, so i update it")
                self.update()
            if len(self.stages_id)-1 == number_stages_completed_in_quest[self.id]:
                current_quest_stages[self.id].completed = True
                return
            number_stages_completed_in_quest[self.id] += 1
            self.start(number_stages_completed_in_quest[self.id])
            return

        def isStarted(self):
            if (not (self.id in number_stages_completed_in_quest)):
                self.update()
            return (self.id in current_quest_stages)

    
    def updateQuestsLevels():
        """Synchronize number_stages_completed_in_quest with quests.
        After this function I suggest to use checkInactiveStage()."""
        # check if there are less elements than flag_keys
        # in case you add them set with False
        for x in quests.keys():
            if (not (x in number_stages_completed_in_quest)):
                number_stages_completed_in_quest[x] = 0
        # check if there are more elements than flag_keys
        # in case it eliminates them
        for x in number_stages_completed_in_quest.keys():
            if (not (x in quests)):
                number_stages_completed_in_quest.remove(x)
        return

    def checkInactiveStage():
        """Check if the inactive Stage have the requirements to be activated, if so, activate them."""
        for k in current_quest_stages.keys():
            current_quest_stages[k].start()
        for k in current_task_stages.keys():
            current_task_stages[k].start()
        return

# TODO: Add the following functions
    # check if current_quest_stages.key is in quests, if not there delete it: Load Game
    # for isCompleted()
    # compare current_quest_stages current_task_stages if in current_quest_stages ce an extra quest is deleted
