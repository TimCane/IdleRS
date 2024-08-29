
from skills.skill import ProductionSkill, Skill


class Smithing(Skill, ProductionSkill):

    def get_name(self):
        return "Smithing"

    def get_icon(self):
        return '⚒️'

    def get_option_key(self):
        return "Sm"

    def get_option_value(self):
        return "(Sm)ithing"

    def get_description(self):
        return "Smelting ores into bars and forging bars into armour and weapons."
