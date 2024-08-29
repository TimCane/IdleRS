
from skills.skill import Skill, UtilitySkill


class Slayer(Skill, UtilitySkill):

    def get_name(self):
        return "Slayer"

    def get_icon(self):
        return '🗡️'

    def get_option_key(self):
        return "Sl"

    def get_option_value(self):
        return "(Sl)ayer"

    def get_description(self):
        return "Killing certain monsters that can't normally be defeated."
