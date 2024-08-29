
from skills.skill import CombatSkill, Skill


class Strength(Skill, CombatSkill):

    def get_name(self):
        return "Strength"

    def get_icon(self):
        return '💪'

    def get_option_key(self):
        return "St"

    def get_option_value(self):
        return "(St)rength"

    def get_description(self):
        return "Dealing more melee damage and equipping certain weapons."
