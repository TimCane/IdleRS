
from skills.skill import GatheringSkill, Skill, GatheringSkillEntry
from items.copper_ore import CopperOre


class Mining(Skill, GatheringSkill):

    def __init__(self):
        self.gathering_options = [
            GatheringSkillEntry(1, CopperOre())
        ]
        super().__init__()

    def get_name(self):
        return "Mining"

    def get_icon(self):
        return '⛏️'

    def get_option_key(self):
        return "Mi"

    def get_option_value(self):
        return "(Mi)ning"

    def get_description(self):
        return "Obtaining ores and minerals from rocks."
