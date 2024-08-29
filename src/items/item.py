

from abc import ABC, abstractmethod


class Item(ABC):
    @abstractmethod
    def get_name(self):
        pass
