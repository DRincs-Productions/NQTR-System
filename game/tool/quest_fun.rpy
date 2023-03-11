define new_quest_notify = _("A new quest began")
define quest_updated_notify = _("The quest has been updated")

init python:
    def updateQuestsLevels() -> None:
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
                del number_stages_completed_in_quest[x]
        return

    def checkIfTheQuestExist(id: str) -> bool:
        if (not (id in quests)):
            log_warn("the Quest: " + id + " does not exist", renpy.get_filename_line())
            return False
        return True

    def checkIfTheQuestIsInNumberStages(id: str) -> bool:
        if (not checkIfTheQuestExist(id)):
            return False
        if (not (id in number_stages_completed_in_quest)):
            log_warn("the Quest: " + id + " not is in number_stages_completed_in_quest, so i update it", renpy.get_filename_line())
            quests[id].update(current_quest_stages, number_stages_completed_in_quest)
            if (not (id in number_stages_completed_in_quest)):
                log_warn("the Quest: " + id + " not is in number_stages_completed_in_quest, not even after the update", renpy.get_filename_line())
                return False
        return True

    def checkIfTheQuestIsCurrentTaskStages(id: str) -> bool:
        if (not checkIfTheQuestExist(id)):
            return False
        if (not (id in current_task_stages)):
            log_warn("the Quest: " + id + " not is in current_task_stages, so i update it", renpy.get_filename_line())
            quests[id].update(current_quest_stages, current_task_stages)
            if (not (id in current_task_stages)):
                log_warn("the Quest: " + id + " not is in current_task_stages, not even after the update", renpy.get_filename_line())
                return False
        return True

    def getPercentageCompletion(id: str) -> int:
        """Returns the percentage of completion"""
        log_info("getPercentageCompletion", renpy.get_filename_line())
        if (not checkIfTheQuestIsInNumberStages(id))
            return 0
        return quests[id].getPercentageCompletion(number_stages_completed_in_quest[id])

    def setDayNumberRequiredToStart(id: str, dayNumberRequired: int) -> None:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#add-days-waiting-before-start """
        log_info("setDayNumberRequiredToStart", renpy.get_filename_line())
        if (not checkIfTheQuestIsCurrentTaskStages(id))
            return
        return current_task_stages[id].setDayNumberRequiredToStart(dayNumberRequired, tm)

    def start(id: str, n_stage: int = 0) -> None:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#start-a-quest """
        if (not checkIfTheQuestExist(id)):
            return
        quests[id].start(quest_stages, current_quest_stages, number_stages_completed_in_quest, tm, flags, n_stage)
        if (n_stage == 0):
            notifyEx(new_quest_notify)
        return

    def nextStageOnlyIsCompleted(id: str) -> bool:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#next-stage-only-it-is-completed """
        if (id in current_task_stages):
            if (not current_task_stages[id].isCompleted(number_stages_completed_in_quest, tm, flags)):
                return False
        elif (id in current_quest_stages):
            if (not current_task_stages[id].isCompleted(number_stages_completed_in_quest, tm, flags)):
                return False
        nextStage(current_quest_stages, number_stages_completed_in_quest, current_task_stages)
        return True

    def nextStage(id: str) -> None:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#next-stage """
        if (not checkIfTheQuestExist(id)):
            return
        quests[id].nextStage(current_quest_stages, number_stages_completed_in_quest, current_task_stages)
        notifyEx(quest_updated_notify)
        return

    # TODO To move in renpy
    def isStarted(self, current_quest_stages: dict[str, Stage], number_stages_completed_in_quest: dict[str, int]) -> bool:
        if (not (self.id in number_stages_completed_in_quest)):
            self.update(current_quest_stages, number_stages_completed_in_quest)
        return (self.id in current_quest_stages)
