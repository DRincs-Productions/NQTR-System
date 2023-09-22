from typing import Any, Optional

import renpy.exports as renpy

from pythonpackages.renpy_utility.flags import *
from pythonpackages.nqtr.time import TimeHandler
from pythonpackages.renpy_utility.renpy_custom_log import *


class Goal(object):
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#goal"""

    def __init__(
        self,
        id: str,
        description: Optional[str] = None,
        is_completed: bool = False,
        need: int = 0,
        have: int = 0,
    ):
        self.id = id
        self.description = description
        self.is_completed = is_completed
        self.need = need
        self.have = have

    @property
    def id(self) -> str:
        """Id of the Goal"""
        return self._id

    @id.setter
    def id(self, value: str):
        self._id = value

    @property
    def description(self) -> str:
        """Description of the Goal"""
        return self._description or ""

    @description.setter
    def description(self, value: Optional[str]):
        self._description = value

    @property
    def is_completed(self) -> bool:
        """returns True if the mission has been completed"""
        if self._is_completed == True:
            return True
        return self.need <= self.have

    @is_completed.setter
    def is_completed(self, value: bool):
        self._is_completed = value

    @property
    def need(self) -> int:
        """Number of elements needed to complete the mission"""
        return self._need

    @need.setter
    def need(self, value: int):
        self._need = value
        if self._need < 0:
            self._need = 0
            log_warn(
                "You have set need < 0, so it will be set to 0.",
                "nqtr.quest.Goal.__init__",
            )

    @property
    def have(self) -> int:
        """Number of elements already collected"""
        return self._have

    @have.setter
    def have(self, value: int):
        self._have = value
        if self._have < 0:
            self._have = 0
            log_warn(
                "You have set have < 0, so it will be set to 0.",
                "nqtr.quest.Goal.__init__",
            )

    def find(self, value: int = 1) -> bool:
        """Adds in element to the target, then checks the completion status. In case a need is null completes the mission. Returns True if the mission has been completed.
        It is used to complete the Goals."""
        self.have += value
        if self.is_completed:
            self.is_completed = True
            return True
        return False


class Stage(object):
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#stage"""

    def __init__(
        self,
        quest_id: str,
        goals: list[Goal] = [],
        title: str = "",
        description: str = "",
        advice: str = "",
        info_image: Optional[str] = None,
        days_required_to_start: int = 0,
        flags_required: list[str] = [],
        required_number_completed_stages: dict[str, int] = {},
        request_description: str = "",
        start_label_name: Optional[str] = None,
        end_label_name: Optional[str] = None,
        check_label_name: Optional[str] = None,
    ):
        self.quest_id = quest_id
        self.goals = goals
        self.title = title
        self.description = description
        self.advice = advice
        self.info_image = info_image
        self.days_required_to_start = days_required_to_start
        self.flags_required = flags_required
        self.required_number_completed_stages = required_number_completed_stages
        self.request_description = request_description
        self.start_label_name = start_label_name
        self.end_label_name = end_label_name
        self.check_label_name = check_label_name

        self.day_start = None
        self.completed = False
        self.active = False

    @property
    def quest_id(self) -> str:
        """Id of the quest"""
        return self._quest_id

    @quest_id.setter
    def quest_id(self, value: str):
        self._quest_id = value

    @property
    def goals(self) -> list[Goal]:
        """List of the goals"""
        return self._goals

    @goals.setter
    def goals(self, value: list[Goal]):
        self._goals = value

    @property
    def title(self) -> str:
        """Title of the Stage"""
        return self._title

    @title.setter
    def title(self, value: str):
        self._title = value

    @property
    def description(self) -> str:
        """Description of the Stage"""
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = value

    @property
    def advice(self) -> str:
        """Advice of the Stage"""
        return self._advice

    @advice.setter
    def advice(self, value: str):
        self._advice = value

    @property
    def background(self) -> Optional[str]:
        """Deprecate: use info_image"""
        return self._info_image

    @background.setter
    def background(self, value: Optional[str]):
        """Deprecate: use info_image"""
        self._info_image = value

    @property
    def info_image(self) -> Optional[str]:
        return self._info_image

    @info_image.setter
    def info_image(self, value: Optional[str]):
        self._info_image = value

    @property
    def days_required_to_start(self) -> int:
        """Number of days required to start the Stage
        These are the requirements to start the Stage"""
        return self._days_required_to_start

    @days_required_to_start.setter
    def days_required_to_start(self, value: int):
        self._days_required_to_start = value

    @property
    def flags_required(self) -> list[str]:
        """List of the flags required to start the Stage
        # TODO: implement this"""
        return self._flags_requests

    @flags_required.setter
    def flags_required(self, value: list[str]):
        self._flags_requests = value

    @property
    def required_number_completed_stages(self) -> dict[str, int]:
        """Dict of the number of stages completed in the quest required to start the Stage"""
        return self._required_number_completed_stages

    @required_number_completed_stages.setter
    def required_number_completed_stages(self, value: dict[str, int]):
        self._required_number_completed_stages = value

    @property
    def request_description(self) -> str:
        """Description of the requirements to start the Stage"""
        return self._request_description

    @request_description.setter
    def request_description(self, value: str):
        self._request_description = value

    @property
    def start_label_name(self) -> Optional[str]:
        """Name of the label to start the Stage
        Will be initiated when the stage is started
        these labels will be started automatically at the appropriate time."""
        return self._start_label_name

    @start_label_name.setter
    def start_label_name(self, value: Optional[str]):
        self._start_label_name = value

    @property
    def end_label_name(self) -> Optional[str]:
        """Name of the label to end the Stage
        # TODO: implement this"""
        return self._end_label_name

    @end_label_name.setter
    def end_label_name(self, value: Optional[str]):
        self._end_label_name = value

    @property
    def check_label_name(self) -> Optional[str]:
        """Name of the label to check the Stage
        # TODO: implement this"""
        return self._check_label_name

    @check_label_name.setter
    def check_label_name(self, value: Optional[str]):
        self._check_label_name = value

    @property
    def day_start(self) -> Optional[int]:
        """Day when the Stage is started"""
        return self._day_start

    @day_start.setter
    def day_start(self, value: Optional[int]):
        self._day_start = value

    @property
    def completed(self) -> bool:
        """True if the Stage is completed"""
        return self._is_completed

    @completed.setter
    def completed(self, value: bool):
        self._is_completed = value

    @property
    def active(self) -> bool:
        """True if the Stage is active"""
        return self._active

    @active.setter
    def active(self, value: bool):
        self._active = value

    # Any is Stage
    def add_in_current_stages(
        self, current_stages: dict[str, Any], tm: TimeHandler
    ) -> None:
        """Add the Stage in the current_quest_stages.
        Can also be used for tasks: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#task
        """
        current_stages[self.quest_id] = Stage(
            quest_id=self.quest_id,
            goals=self.goals,
            flags_required=self.flags_required,
            required_number_completed_stages=self.required_number_completed_stages,
            request_description=self.request_description,
            start_label_name=self.start_label_name,
            end_label_name=self.end_label_name,
            check_label_name=self.check_label_name,
            days_required_to_start=self.days_required_to_start,
        )
        # add_required_days_to_start: is important to set the day_start to the current day.
        current_stages[self.quest_id].add_required_days_to_start(
            dayNumberRequired=self.days_required_to_start, tm=tm
        )
        return

    def start(
        self,
        number_stages_completed_in_quest: dict[str, int],
        tm: TimeHandler,
        flags: dict[str, bool] = {},
    ) -> bool:
        """If you have reached all the objectives then activate the Stage.
        start() is used until the Stage becomes active."""
        if self.active:
            return self.active
        if not self.all_requests_are_met(number_stages_completed_in_quest, tm, flags):
            return False
        self.active = True
        if self.start_label_name != None:
            # TODO TO Move in Renpy
            renpy.call(self.start_label_name)
        return True

    def all_requests_are_met(
        self,
        number_stages_completed_in_quest: dict[str, int],
        tm: TimeHandler,
        flags: dict[str, bool] = {},
    ) -> bool:
        """Checks the requests, returns True if it satisfies them."""
        if self.day_start != None and tm.day < self.day_start:
            return False
        for quest, level in self.required_number_completed_stages.items():
            if number_stages_completed_in_quest[quest] < level:
                return False
        for item in self.flags_required:
            if not get_flags(item, flags):
                return False
        return True

    def is_completed(
        self,
        number_stages_completed_in_quest: dict[str, int],
        tm: TimeHandler,
        flags: dict[str, bool] = {},
    ) -> bool:
        """Check if the Stage can be complete."""
        # if (check_label_name != None)
        if self.completed:
            return True
        if not self.active:
            if not self.start(number_stages_completed_in_quest, tm, flags):
                return False
        if self.goals:
            for x in self.goals:
                if not x.is_completed:
                    return False
        self.completed = True
        return True

    def find(self, goals_id: str, value: int = 1) -> bool:
        for item in self.goals:
            if item.id == goals_id:
                item.find(value)
                return True
        return False

    def add_required_days_to_start(
        self, dayNumberRequired: int, tm: TimeHandler
    ) -> None:
        """Add days of waiting before it starts"""
        if dayNumberRequired:
            self.day_start = tm.day + dayNumberRequired
        return


class Quest(object):
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#quest
    Task: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#task"""

    def __init__(
        self,
        id: str,
        title: str = "",
        description: str = "",
        icon: Optional[str] = None,
        info_image: Optional[str] = None,
        stage_ids: list[str] = [],
        development: bool = False,
    ):
        self.id = id
        self.title = title
        self.description = description
        self.icon = icon
        self.info_image = info_image
        self.stage_ids = self.stage_ids = stage_ids
        self.development = development

    @property
    def id(self) -> str:
        """Quest ID"""
        return self._id

    @id.setter
    def id(self, value: str):
        self._id = value

    @property
    def title(self) -> str:
        """Quest title"""
        return self._title

    @title.setter
    def title(self, value: str):
        self._title = value

    @property
    def description(self) -> str:
        """Quest description"""
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = value

    @property
    def icon(self) -> Optional[str]:
        """Quest icon"""
        return self._icon

    @icon.setter
    def icon(self, value: Optional[str]):
        self._icon = value

    @property
    def background(self) -> Optional[str]:
        """Deprecate: use info_image"""
        return self._info_image

    @background.setter
    def background(self, value: Optional[str]):
        """Deprecate: use info_image"""
        self._info_image = value

    @property
    def info_image(self) -> Optional[str]:
        """Quest info image"""
        return self._info_image

    @info_image.setter
    def info_image(self, value: Optional[str]):
        self._info_image = value

    @property
    def stage_ids(self) -> list[str]:
        """Quest stages"""
        return self._stage_ids

    @stage_ids.setter
    def stage_ids(self, value: list[str]):
        self._stage_ids = value

    @property
    def development(self) -> bool:
        """Quest development"""
        return self._development

    @development.setter
    def development(self, value: bool):
        self._development = value

    def is_completed(
        self,
        current_quest_stages: dict[str, Stage],
        number_stages_completed_in_quest: dict[str, int],
    ) -> bool:
        """Check if all stages have been completed."""
        if not (self.id in number_stages_completed_in_quest):
            return False
        if len(self.stage_ids) - 1 == number_stages_completed_in_quest[self.id]:
            return current_quest_stages[self.id].completed
        else:
            return False

    def quest_id(self, number_stages_completed_in_quest: dict[str, int]) -> str:
        """Return the id of this current"""
        return self.stage_ids[number_stages_completed_in_quest[self.id]]

    def completed_stages_number(
        self, number_stages_completed_in_quest: dict[str, int]
    ) -> int:
        """Returns the number of completed stages"""
        return number_stages_completed_in_quest[self.id]

    def percentage_completion(self, current_level: int) -> float:
        """Returns the percentage of completion"""
        return current_level / len(self.stage_ids) * 100

    def update(
        self,
        quest_stages: dict[str, Stage],
        current_quest_stages: dict[str, Stage],
        number_stages_completed_in_quest: dict[str, int],
        tm: TimeHandler,
        flags: dict[str, bool] = {},
    ) -> None:
        """Function to update the various values,
        If it is a completed Quest and a Stage has been added in a new update, the new Stage begins.
        Prevent errors like blocked Quests."""
        if self.is_completed(current_quest_stages, number_stages_completed_in_quest):
            return
        if (
            not (self.id in current_quest_stages)
            and number_stages_completed_in_quest[self.id] == 0
        ):
            return
        # if the Quest has been started, but there is no current_quest_stages, it restarts the Quest from 0
        if not (self.id in current_quest_stages):
            self.start(
                quest_stages,
                current_quest_stages,
                number_stages_completed_in_quest,
                tm,
                flags,
            )
            return
        # if you have somehow exceeded the number of stages
        if len(self.stage_ids) - 1 < number_stages_completed_in_quest[self.id]:
            number_stages_completed_in_quest[self.id] = len(self.stage_ids) - 1
            return
        # if it is a completed Quest and a Stage has been added in a new update
        if (
            not self.is_completed(
                current_quest_stages, number_stages_completed_in_quest
            )
        ) and current_quest_stages[self.id].completed:
            self.after_next_stage(
                quest_stages,
                current_quest_stages,
                number_stages_completed_in_quest,
                tm,
                flags,
            )
            return

    def start(
        self,
        quest_stages: dict[str, Stage],
        current_quest_stages: dict[str, Stage],
        number_stages_completed_in_quest: dict[str, int],
        tm: TimeHandler,
        flags: dict[str, bool] = {},
        n_stage: int = 0,
    ) -> None:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#start-a-quest"""
        number_stages_completed_in_quest[self.id] = n_stage
        quest_stages[self.stage_ids[n_stage]].add_in_current_stages(
            current_quest_stages, tm
        )
        current_quest_stages[self.id].start(number_stages_completed_in_quest, tm, flags)
        return

    def next_stage(
        self,
        quest_stages: dict[str, Stage],
        current_quest_stages: dict[str, Stage],
        number_stages_completed_in_quest: dict[str, int],
        current_task_stages: dict[str, Stage],
        tm: TimeHandler,
        flags: dict[str, bool] = {},
    ) -> None:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#next-stage"""
        if self.id in current_task_stages:
            del current_task_stages[self.id]
            return
        self.after_next_stage(
            quest_stages,
            current_quest_stages,
            number_stages_completed_in_quest,
            tm,
            flags,
        )
        return

    def after_next_stage(
        self,
        quest_stages: dict[str, Stage],
        current_quest_stages: dict[str, Stage],
        number_stages_completed_in_quest: dict[str, int],
        tm: TimeHandler,
        flags: dict[str, bool] = {},
    ) -> None:
        if not (self.id in number_stages_completed_in_quest):
            log_warn(
                "the Quest: "
                + self.id
                + " not is in number_stages_completed_in_quest, so i update it",
                "nqtr.quest.Quest.after_next_stage()",
            )
            self.update(
                quest_stages,
                current_quest_stages,
                number_stages_completed_in_quest,
                tm,
                flags,
            )
        if len(self.stage_ids) - 1 == number_stages_completed_in_quest[self.id]:
            current_quest_stages[self.id].completed = True
            return
        number_stages_completed_in_quest[self.id] += 1
        self.start(
            quest_stages,
            current_quest_stages,
            number_stages_completed_in_quest,
            tm,
            flags,
            number_stages_completed_in_quest[self.id],
        )
        return


# TODO: Add the following functions
# check if current_quest_stages.key is in quests, if not there delete it: Load Game
# for is_completed()
# compare current_quest_stages current_task_stages if in current_quest_stages ce an extra quest is deleted
