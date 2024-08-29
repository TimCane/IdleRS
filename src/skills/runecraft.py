
from skills.skill import ProductionSkill, Skill


class Runecraft(Skill, ProductionSkill):

    def get_name(self):
        return "Runecraft"

    def get_icon(self):
        return '🔮'

    def get_option_key(self):
        return "Ru"

    def get_option_value(self):
        return "(Ru)necraft"

    def get_description(self):
        return "Creating runes used for casting Magic."
