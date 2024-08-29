
from skills.skill import ProductionSkill, Skill


class Crafting(Skill, ProductionSkill):

    def get_name(self):
        return "Crafting"

    def get_icon(self):
        return '🧵'

    def get_option_key(self):
        return "Cr"

    def get_option_value(self):
        return "(Cr)afting"

    def get_description(self):
        return "Creating items such as jewellery, pottery, and ranged armour."
