define new_quest_notify = _("A new quest began")
define quest_updated_notify = _("The quest has been updated")

init python:
    from pythonpackages.nqtr.quest import Stage


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

    def checkInactiveStage(current_stages: dict[str, Stage]) -> None:
        """Check if the inactive Stage have the requirements to be activated, if so, activate them."""
        for k in current_stages.keys():
            current_stages[k].start(number_stages_completed_in_quest, tm, flags)
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

    def checkIfTheQuestIsCurrentQuestStages(id: str) -> bool:
        if (not checkIfTheQuestExist(id)):
            return False
        if (not (id in current_quest_stages)):
            log_warn("the Quest: " + id + " not is in current_quest_stages, so i update it", renpy.get_filename_line())
            quests[id].update(current_quest_stages, current_quest_stages)
            if (not (id in current_quest_stages)):
                log_warn("the Quest: " + id + " not is in current_quest_stages, not even after the update", renpy.get_filename_line())
                return False
        return True

    def quest_getPercentageCompletion(id: str) -> int:
        """Returns the percentage of completion"""
        log_info("quest_getPercentageCompletion", renpy.get_filename_line())
        if (not checkIfTheQuestIsInNumberStages(id)):
            return 0
        return quests[id].getPercentageCompletion(number_stages_completed_in_quest[id])

    def quest_setDayNumberRequiredToStart(id: str, day: int) -> None:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#add-days-waiting-before-start """
        log_info("quest_setDayNumberRequiredToStart", renpy.get_filename_line())
        if (not checkIfTheQuestIsCurrentTaskStages(id)):
            return
        return current_task_stages[id].setDayNumberRequiredToStart(dayNumberRequired, tm)

    def quest_start(id: str, n_stage: int = 0) -> bool:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#start-a-quest """
        log_info("quest_start", renpy.get_filename_line())
        if (not checkIfTheQuestExist(id)):
            return False
        quests[id].start(quest_stages, current_quest_stages, number_stages_completed_in_quest, tm, flags, n_stage)
        if (n_stage == 0):
            notify_add(new_quest_notify)
        return True

    def quest_nextStageOnlyIsCompleted(id: str) -> bool:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#next-stage-only-it-is-completed """
        log_info("quest_nextStageOnlyIsCompleted", renpy.get_filename_line())
        if (id in current_task_stages):
            if (not current_task_stages[id].isCompleted(number_stages_completed_in_quest, tm, flags)):
                return False
        elif (id in current_quest_stages):
            if (not current_task_stages[id].isCompleted(number_stages_completed_in_quest, tm, flags)):
                return False
        quest_nextStage(id)
        return True

    def quest_nextStage(id: str) -> None:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Quest#next-stage """
        log_info("quest_nextStage", renpy.get_filename_line())
        if (not checkIfTheQuestExist(id)):
            return
        quests[id].nextStage(quest_stages, current_quest_stages, number_stages_completed_in_quest, current_task_stages, tm, flags)
        notify_add(quest_updated_notify)
        return

    def quest_isStarted(id: str) -> bool:
        log_info("quest_isStarted", renpy.get_filename_line())
        if (not checkIfTheQuestIsCurrentQuestStages(id)):
            return False
        return (id in current_quest_stages)

    def quest_isCompleted(id: str) -> bool:
        """Check if all stages have been completed."""
        log_info("quest_isCompleted", renpy.get_filename_line())
        if (not checkIfTheQuestExist(id)):
            return
        if (not (id in number_stages_completed_in_quest)):
            updateQuestsLevels()
            return False
        return quests[id].isCompleted(current_quest_stages, number_stages_completed_in_quest)

    def quest_currentQuestId(id: str) -> str:
        """Return the id of this current"""
        log_info("quest_currentQuestId", renpy.get_filename_line())
        if (not (id in number_stages_completed_in_quest)):
            quest_update(id)
        return quests[id].currentQuestId(number_stages_completed_in_quest)

    def quest_completeStagesNumber(id: str) -> int:
        """Returns the number of completed stages"""
        log_info("quest_completeStagesNumber", renpy.get_filename_line())
        if (not (id in number_stages_completed_in_quest)):
            quest_update(id)
        return quests[id].completeStagesNumber(number_stages_completed_in_quest)

    def quest_update(id: str) -> int:
        """Function to update the various values,
        If it is a completed Quest and a Stage has been added in a new update, the new Stage begins.
        Prevent errors like blocked Quests."""
        log_info("quest_update", renpy.get_filename_line())
        return quests[id].update(quest_stages, current_quest_stages, number_stages_completed_in_quest, tm, flags)