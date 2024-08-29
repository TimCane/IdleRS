
from skills.skill import ProductionSkill, Skill


class Herblore(Skill, ProductionSkill):

    def get_name(self):
        return "Herblore"

    def get_icon(self):
        return '🌿'

    def get_option_key(self):
        return "He"

    def get_option_value(self):
        return "(He)rblore"

    def get_description(self):
        return "Cleaning and using herbs to create potions."
