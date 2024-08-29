
from skills.skill import Skill, UtilitySkill


class Construction(Skill, UtilitySkill):

    def get_name(self):
        return "Construction"

    def get_icon(self):
        return '🏠'

    def get_option_key(self):
        return "Con"

    def get_option_value(self):
        return "(Con)struction"

    def get_description(self):
        return "Building a player-owned house."
