from core.range_base import RangeBase
from dataclasses import dataclass, field
from typing import List


@dataclass
class RangeMapper(RangeBase):
    src_range: List[str]
    to_range: List[str]
    
    
    def execute(self, src_string: str) -> str:
        result = ''
        for src_char in src_string:
            index = self._find_index(self.src_range, src_char)
            result += self._get_char_from_index(self.to_range, index) if index > -1 else src_char
            
        return result
            
    def _find_index(self, range_to_find: List[str], char: str) -> int:
        try:
            reverse_index = range_to_find[::-1].index(char)
            return len(range_to_find) - 1 - reverse_index
        except ValueError:
            return -1
    
    def _get_char_from_index(self, range_to_get: List[str], index: int) -> str:
        return range_to_get[index] if index < len(range_to_get) else range_to_get[-1]