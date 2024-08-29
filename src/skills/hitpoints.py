
from skills.skill import CombatSkill, Skill


class Hitpoints(Skill, CombatSkill):

    def __init__(self):
        self.xp = 1154
        super().__init__()

    def get_name(self):
        return "Hitpoints"

    def get_icon(self):
        return '❤️'

    def get_option_key(self):
        return "Hi"

    def get_option_value(self):
        return "(Hi)tpoints"

    def get_description(self):
        return "Amount of damage you can withstand."
