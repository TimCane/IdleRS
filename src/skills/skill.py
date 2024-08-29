

from abc import ABC, abstractmethod


class Skill(ABC):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Skill, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    xp = 0

    def get_xp(self):
        return self.xp

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_icon(self):
        pass

    @abstractmethod
    def get_option_key(self):
        pass

    @abstractmethod
    def get_option_value(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


class CombatSkill(ABC):
    pass


class GatheringSkillEntry():

    level = 0

    def __init__(self, level, item):
        self.level = level
        self.item = item


class GatheringSkill(ABC):
    gathering_options = []

    def get_gathering_options(self):
        pass


class ProductionSkill(ABC):
    pass


class UtilitySkill(ABC):
    pass
