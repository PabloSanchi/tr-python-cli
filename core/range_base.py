from abc import ABC, abstractmethod


class RangeBase(ABC):

    @abstractmethod
    def execute(self, src_string: str) -> str:
        ...
