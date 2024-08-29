
from skills.skill import CombatSkill, Skill


class Attack(Skill, CombatSkill):

    def get_name(self):
        return "Attack"

    def get_icon(self):
        return '⚔️'

    def get_option_key(self):
        return "At"

    def get_option_value(self):
        return "(At)tack"

    def get_description(self):
        return "Wielding stronger melee weapons and hitting monsters more accurately in Melee."
