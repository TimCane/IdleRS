
from skills.skill import UtilitySkill, Skill


class Agility(Skill, UtilitySkill):

    def get_name(self):
        return "Agility"

    def get_icon(self):
        return '🤸'

    def get_option_key(self):
        return "Ag"

    def get_option_value(self):
        return "(Ag)ility"

    def get_description(self):
        return "Traversing shortcuts and increases the rate at which energy recharges."
