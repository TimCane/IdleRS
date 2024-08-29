
from skills.skill import CombatSkill, Skill


class Magic(Skill, CombatSkill):

    def get_name(self):
        return "Magic"

    def get_icon(self):
        return '🧙'

    def get_option_key(self):
        return "Ma"

    def get_option_value(self):
        return "(Ma)gic"

    def get_description(self):
        return "Casting various combat and utility spells."
