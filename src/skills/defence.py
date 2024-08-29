
from skills.skill import CombatSkill, Skill


class Defence(Skill, CombatSkill):
    def get_name(self):
        return "Defence"

    def get_icon(self):
        return '🛡️'

    def get_option_key(self):
        return "D"

    def get_option_value(self):
        return "(D)efence"

    def get_description(self):
        return "Wearing stronger armour and decreasing chance of being hit."
