from core.range_base import RangeBase
from dataclasses import dataclass, field
from typing import List

@dataclass
class RangeDeleter(RangeBase):
    src_range: List[str]    
    
    def execute(self, src_string: str) -> str:
        result = ''
        for src_char in src_string:
            if src_char not in self.src_range:
                result += src_char
            
        return result
            