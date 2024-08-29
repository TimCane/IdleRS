
from skills.skill import Skill, UtilitySkill


class Firemaking(Skill, UtilitySkill):

    def get_name(self):
        return "Firemaking"

    def get_icon(self):
        return '🔥'

    def get_option_key(self):
        return "Fir"

    def get_option_value(self):
        return "(Fir)emaking"

    def get_description(self):
        return "Lighting logs into fire."
