
from skills.skill import Skill, UtilitySkill


class Thieving(Skill, UtilitySkill):

    def get_name(self):
        return "Thieving"

    def get_icon(self):
        return '💰'

    def get_option_key(self):
        return "T"

    def get_option_value(self):
        return "(T)hieving"

    def get_description(self):
        return "Stealing from market stalls and chests and pickpocketing non-player characters."
