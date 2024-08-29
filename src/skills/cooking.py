
from skills.skill import ProductionSkill, Skill


class Cooking(Skill, ProductionSkill):

    def get_name(self):
        return "Cooking"

    def get_icon(self):
        return '🍳'

    def get_option_key(self):
        return "Coo"

    def get_option_value(self):
        return "(Coo)king"

    def get_description(self):
        return "Making and cooking food."
