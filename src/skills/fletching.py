
from skills.skill import ProductionSkill, Skill


class Fletching(Skill, ProductionSkill):

    def get_name(self):
        return "Fletching"

    def get_icon(self):
        return '🏹'

    def get_option_key(self):
        return "Fl"

    def get_option_value(self):
        return "(Fl)etching"

    def get_description(self):
        return "Creating ranged weapons and ammunition."
