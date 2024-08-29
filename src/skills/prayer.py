
from skills.skill import CombatSkill, Skill


class Prayer(Skill, CombatSkill):

    def get_name(self):
        return "Prayer"

    def get_icon(self):
        return '🙏'

    def get_option_key(self):
        return "P"

    def get_option_value(self):
        return "(P)rayer"

    def get_description(self):
        return "Activating temporary aids to assist in combat."
