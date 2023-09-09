init -1 python:
    if not "quests_descriptions" in locals() | globals():
        quests_descriptions = {}
    if not "quests" in locals() | globals():
        quests = {}
    if not "quest_stages" in locals() | globals():
        quest_stages = {}
