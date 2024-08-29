
from skills.skill import CombatSkill, Skill


class Ranged(Skill, CombatSkill):

    def get_name(self):
        return "Ranged"

    def get_icon(self):
        return '🏹'

    def get_option_key(self):
        return "Ra"

    def get_option_value(self):
        return "(Ra)nged"

    def get_description(self):
        return "Equipping stronger ranged weapons and armour. It also increases ranged accuracy."
