
from skills.skill import GatheringSkill, Skill


class Fishing(Skill, GatheringSkill):

    def __init__(self):
        self.gathering_options = [
        ]
        super().__init__()

    def get_name(self):
        return "Fishing"

    def get_icon(self):
        return '🎣'

    def get_option_key(self):
        return "Fis"

    def get_option_value(self):
        return "(Fis)hing"

    def get_description(self):
        return "Catching fish."
