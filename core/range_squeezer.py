from dataclasses import dataclass
from typing import List

from core.range_base import RangeBase


@dataclass
class RangeSqueezer(RangeBase):
    src_range: List[str]

    def execute(self, src_string: str) -> str:
        result = ''
        previous_char = None

        for char in src_string:
            if char in self.src_range and char == previous_char:
                continue
            result += char
            previous_char = char

        return result
