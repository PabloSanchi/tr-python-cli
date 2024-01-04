from dataclasses import dataclass, field
from typing import List

from core.range_base import RangeBase


@dataclass
class RangeMapper(RangeBase):
    src_range: List[str]
    to_range: List[str]
    _lookup_dict: dict = field(default_factory=dict, init=False)
    _cache: dict = field(default_factory=dict, init=False)


    def __post_init__(self):
        self._lookup_dict = {char: i for i, char in enumerate(self.src_range)}
        self._cache = {}

    def execute(self, src_string: str) -> str:
        result = ''
        for src_char in src_string:
            result += self.map_char(src_char)

        return result

    def map_char(self, src_char: str) -> str:
        if src_char in self._cache:
            return self._cache[src_char]

        index = self._lookup_dict.get(src_char, -1)
        return self._get_char_from_index(self.to_range, index) if index > -1 else src_char

    def _get_char_from_index(self, range_to_get: List[str], index: int) -> str:
        return range_to_get[index] if index < len(range_to_get) else range_to_get[-1]
