
from skills.skill import GatheringSkill, Skill


class Farming(Skill, GatheringSkill):

    def __init__(self):
        self.gathering_options = [
        ]
        super().__init__()

    def get_name(self):
        return "Farming"

    def get_icon(self):
        return '🌾'

    def get_option_key(self):
        return "Fa"

    def get_option_value(self):
        return "(Fa)rming"

    def get_description(self):
        return "Planting and harvesting crops."
