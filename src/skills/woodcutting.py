
from skills.skill import GatheringSkill, Skill


class Woodcutting(Skill, GatheringSkill):

    def __init__(self):
        self.gathering_options = [
        ]
        super().__init__()

    def get_name(self):
        return "Woodcutting"

    def get_icon(self):
        return '🌲'

    def get_option_key(self):
        return "W"

    def get_option_value(self):
        return "(W)oodcutting"

    def get_description(self):
        return "Chopping down trees."
