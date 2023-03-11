from typing import Optional

import renpy.exports as renpy

from pythonpackages.flags import *
from pythonpackages.nqtr.time import TimeHandler
from pythonpackages.renpy_custom_log import *


class Goal(object):
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#goal"""

    def __init__(self,
                 id: str,
                 description: str = None,
                 complete: bool = False,
                 need: int = 0,
                 have: int = 0):

        self.id = id
        self.description = description if description else ""
        self.complete = complete
        self.need = need
        self.have = 0
        if (self.have < 0):
            self.have = 0
            log_warn("You have set have < 0, so it will be set to 0.",
                     "nqtr.quest.Goal.__init__")
        if (self.need < 0):
            self.need = 0
            log_warn("You have set need < 0, so it will be set to 0.",
                     "nqtr.quest.Goal.__init__")

    def find(self, value: int = 1) -> bool:
        """Adds in element to the target, then checks the completion status. In case a need is null completes the mission. Returns True if the mission has been completed.
        It is used to complete the Goals."""
        if (self.need == 0):
            self.complete = True
        self.have += value
        if (self.isComplete()):
            self.complete = True
            return True
        return False

    def isComplete(self) -> bool:
        """Checks the status of completion. returns True if the mission has been completed"""
        if (self.complete == True):
            return True
        if (self.need == 0):
            return False
        return self.need <= self.have


class Stage(object):
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#stage """

    def __init__(self,
                 quest_id: str,
                 goals: Optional[list[str]] = None,
                 title: str = None,
                 description: str = None,
                 advice: str = None,
                 bg: str = None,
                 days_required_to_start: int = None,
                 # TODO: implement this
                 flags_requests: Optional[list[str]] = None,
                 number_stages_completed_in_quest_requests: Optional[dict[str, int]] = None,
                 request_description: str = None,
                 start_label_name: str = None,  # Will be initiated when the stage is started
                 end_label_name: str = None,  # TODO: implement this
                 check_label_name: str = None,  # TODO: implement this
                 ):

        self.quest_id = quest_id
        self.goals = goals if goals else []
        self.active = False
        self.title = title if title else ""
        self.description = description if description else ""
        self.advice = advice if advice else ""
        self.completed = False
        self.bg = bg
        # These are the requirements to start the Stage
        self.days_required_to_start = days_required_to_start if days_required_to_start else 0
        self.day_start = None  # Will be initiated when the stage is started
        self.flags_requests = flags_requests if flags_requests else []
        self.number_stages_completed_in_quest_requests = number_stages_completed_in_quest_requests if number_stages_completed_in_quest_requests else {}
        self.request_description = request_description if request_description else ""
        # these labels will be started automatically at the appropriate time.
        self.start_label_name = start_label_name
        self.end_label_name = end_label_name
        self.check_label_name = check_label_name

    def addInCurrentQuestStages(self, current_quest_stages: dict[str, Stage], tm: TimeHandler) -> None:
        """Add the Stage in the current_quest_stages"""
        current_quest_stages[self.quest_id] = Stage(
            quest_id=self.quest_id,
            goals=self.goals,
            flags_requests=self.flags_requests,
            number_stages_completed_in_quest_requests=self.number_stages_completed_in_quest_requests,
            request_description=self.request_description,
            start_label_name=self.start_label_name,
            end_label_name=self.end_label_name,
            check_label_name=self.check_label_name,
            days_required_to_start=self.days_required_to_start,
        )
        # setDayNumberRequiredToStart: is important to set the day_start to the current day.
        current_quest_stages[self.quest_id].setDayNumberRequiredToStart(
            dayNumberRequired=self.days_required_to_start, tm=tm)
        return

    # TODO: Ora questo può essere rimpiazzato con addInCurrentQuestStages
    def addInCurrentTaskStages(self, current_task_stages: dict[str, Stage], tm: TimeHandler) -> None:
        """Add the Stage in the current_task_stages, Task: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#task """
        current_task_stages[self.quest_id] = Stage(
            quest_id=self.quest_id,
            goals=self.goals,
            flags_requests=self.flags_requests,
            number_stages_completed_in_quest_requests=self.number_stages_completed_in_quest_requests,
            request_description=self.request_description,
            start_label_name=self.start_label_name,
            end_label_name=self.end_label_name,
            check_label_name=self.check_label_name,
            days_required_to_start=self.days_required_to_start,
        )
        # setDayNumberRequiredToStart: is important to set the day_start to the current day.
        current_task_stages[self.quest_id].setDayNumberRequiredToStart(
            dayNumberRequired=self.days_required_to_start, tm=tm)
        return

    def start(self, number_stages_completed_in_quest: dict[str, int], tm: TimeHandler, flags: dict[str, bool] = {}) -> bool:
        """If you have reached all the objectives then activate the Stage.
        start() is used until the Stage becomes active."""
        if (self.active):
            return self.active
        if (not self.respectAllRequests(number_stages_completed_in_quest, tm, flags)):
            return False
        self.active = True
        if (self.start_label_name != None):
            renpy.call(self.start_label_name)
        return True

    def respectAllRequests(self, number_stages_completed_in_quest: dict[str, int], tm: TimeHandler, flags: dict[str, bool] = {}) -> bool:
        """Checks the requests, returns True if it satisfies them."""
        if (self.day_start != None and tm.day < self.day_start):
            return False
        for quest, level in self.number_stages_completed_in_quest_requests.items():
            if (number_stages_completed_in_quest[quest] < level):
                return False
        for item in self.flags_requests:
            if (not getFlags(item, flags)):
                return False
        return True

    def isCompleted(self, number_stages_completed_in_quest: dict[str, int], tm: TimeHandler, flags: dict[str, bool] = {}) -> bool:
        """Check if the Stage can be complete."""
        # if (check_label_name != None)
        if (self.completed):
            return True
        if (not self.active):
            if (not self.start(number_stages_completed_in_quest, tm, flags)):
                return False
        if self.goals:
            for x in self.goals:
                if (not x.isComplete()):
                    return False
        self.completed = True
        return True

    def find(self, goals_id: str, value: int = 1) -> bool:
        for item in self.goals:
            if (item.id == goals_id):
                item.find(value)
                return True
        return False

    def setDayNumberRequiredToStart(self, dayNumberRequired: int, tm: TimeHandler) -> None:
        """Add days of waiting before it starts"""
        if dayNumberRequired:
            self.day_start = tm.day + dayNumberRequired
        return


class Quest(object):
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#quest 
    Task: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#task """

    def __init__(self,
                 id: str,
                 title: str = None,
                 description: str = None,
                 icon: str = None,
                 bg: str = None,
                 stages_id: Optional[list[str]] = None,
                 tag: str = None,  # TODO: implement this
                 development: bool = False):

        self.id = id
        self.title = title if title else ""
        self.description = description if description else ""
        self.icon = icon
        self.bg = bg
        self.stages_id = self.stages_id = stages_id if stages_id else []
        self.tag = tag
        self.development = development

    # TODO To move in renpy
    def isCompleted(self, current_quest_stages: dict[str, Stage],  number_stages_completed_in_quest: dict[str, int]) -> bool:
        """Check if all stages have been completed."""
        if (not (self.id in number_stages_completed_in_quest)):
            updateQuestsLevels()
            return False
        if len(self.stages_id)-1 == number_stages_completed_in_quest[self.id]:
            return current_quest_stages[self.id].completed
        else:
            return False

    # TODO To move in renpy
    def currentQuestId(self, current_quest_stages: dict[str, Stage],  number_stages_completed_in_quest: dict[str, int]) -> str:
        """Return the id of this current"""
        if (not (self.id in number_stages_completed_in_quest)):
            self.update(current_quest_stages, number_stages_completed_in_quest)
        return self.stages_id[number_stages_completed_in_quest[id]]

    # TODO To move in renpy
    def completeStagesNumber(self, current_quest_stages: dict[str, Stage],  number_stages_completed_in_quest: dict[str, int]) -> int:
        """Returns the number of completed stages"""
        if (not (self.id in number_stages_completed_in_quest)):
            self.update(current_quest_stages, number_stages_completed_in_quest)
        return number_stages_completed_in_quest[id]

    def getPercentageCompletion(self, current_level: int) -> int:
        """Returns the percentage of completion"""
        return current_level/len(self.stages_id)*100

    # TODO To move in renpy
    def setDayNumberRequiredToStart(self, dayNumberRequired: int, current_quest_stages: dict[str, Stage], current_task_stages: dict[str, Stage], number_stages_completed_in_quest: dict[str, int], tm: TimeHandler) -> None:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#add-days-waiting-before-start """
        if (not (self.id in number_stages_completed_in_quest)):
            log_warn("the Quest: "+self.id +
                     " not is in number_stages_completed_in_quest, so i update it", "nqtr.quest.Quest.setDayNumberRequiredToStart()")
            self.update(current_quest_stages, number_stages_completed_in_quest)
        return current_task_stages[self.id].setDayNumberRequiredToStart(dayNumberRequired, tm)

    def update(self, current_quest_stages: dict[str, Stage], number_stages_completed_in_quest: dict[str, int]) -> None:
        """Function to update the various values,
        If it is a completed Quest and a Stage has been added in a new update, the new Stage begins.
        Prevent errors like blocked Quests."""
        if (self.isCompleted(current_quest_stages,  number_stages_completed_in_quest)):
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
        if (not self.isCompleted(current_quest_stages,  number_stages_completed_in_quest)) and current_quest_stages[self.id].completed:
            self.afterNextStage(current_quest_stages,
                                number_stages_completed_in_quest)
            return

    # TODO To move in renpy
    def start(self, quest_stages: dict[str, Stage], current_quest_stages: dict[str, Stage], number_stages_completed_in_quest: dict[str, int], tm: TimeHandler, flags: dict[str, bool] = {}, n_stage: int = 0) -> None:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#start-a-quest """
        quest_stages[self.stages_id[n_stage]].addInCurrentQuestStages(
            current_quest_stages, tm)
        current_quest_stages[self.id].start(
            number_stages_completed_in_quest, tm, flags)
        number_stages_completed_in_quest[self.id] = n_stage
        if (n_stage == 0):
            notifyEx(new_quest_notify)
        return

    # TODO To move in renpy
    def nextStageOnlyIsCompleted(self, current_quest_stages: dict[str, Stage], number_stages_completed_in_quest: dict[str, int], current_task_stages: dict[str, Stage], tm: TimeHandler, flags: dict[str, bool] = {}) -> bool:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#next-stage-only-it-is-completed """
        if (self.id in current_task_stages):
            if (not current_task_stages[self.id].isCompleted(number_stages_completed_in_quest, tm, flags)):
                return False
        elif (self.id in current_quest_stages):
            if (not current_task_stages[self.id].isCompleted(number_stages_completed_in_quest, tm, flags)):
                return False
        self.nextStage(current_quest_stages,
                       number_stages_completed_in_quest, current_task_stages)
        return True

    # TODO To move in renpy
    def nextStage(self, current_quest_stages: dict[str, Stage], number_stages_completed_in_quest: dict[str, int], current_task_stages: dict[str, Stage], ) -> None:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#next-stage """
        if (self.id in current_task_stages):
            del current_task_stages[self.quest_id]
            return
        self.afterNextStage(current_quest_stages,
                            number_stages_completed_in_quest)
        notifyEx(quest_updated_notify)
        return

    def afterNextStage(self, current_quest_stages: dict[str, Stage], number_stages_completed_in_quest: dict[str, int]) -> None:
        if (not (self.id in number_stages_completed_in_quest)):
            log_warn("the Quest: "+self.id +
                     " not is in number_stages_completed_in_quest, so i update it",  "nqtr.quest.Quest.afterNextStage()")
            self.update(current_quest_stages, number_stages_completed_in_quest)
        if len(self.stages_id)-1 == number_stages_completed_in_quest[self.id]:
            current_quest_stages[self.id].completed = True
            return
        number_stages_completed_in_quest[self.id] += 1
        self.start(number_stages_completed_in_quest[self.id])
        return

    # TODO To move in renpy
    def isStarted(self, current_quest_stages: dict[str, Stage], number_stages_completed_in_quest: dict[str, int]) -> bool:
        if (not (self.id in number_stages_completed_in_quest)):
            self.update(current_quest_stages, number_stages_completed_in_quest)
        return (self.id in current_quest_stages)


def checkInactiveStage(current_stages: dict[str: Stage]) -> None:
    """Check if the inactive Stage have the requirements to be activated, if so, activate them."""
    for k in current_stages.keys():
        current_stages[k].start()
    return

# TODO: Add the following functions
# check if current_quest_stages.key is in quests, if not there delete it: Load Game
# for isCompleted()
# compare current_quest_stages current_task_stages if in current_quest_stages ce an extra quest is deleted
