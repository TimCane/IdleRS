
from skills.skill import GatheringSkill, Skill


class Hunter(Skill, GatheringSkill):

    def __init__(self):
        self.gathering_options = [
        ]
        super().__init__()

    def get_name(self):
        return "Hunter"

    def get_icon(self):
        return '🦌'

    def get_option_key(self):
        return "Hu"

    def get_option_value(self):
        return "(Hu)nter"

    def get_description(self):
        return "Capturing wild animals and creatures."
