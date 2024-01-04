from core.range_base import RangeBase
from dataclasses import dataclass, field
from typing import List

@dataclass
class RangeDeleter(RangeBase):
    src_range: List[str]    
    
    def execute(self, src_string: str) -> str:
        src_set = set(self.src_range)
        result = ''
        
        for src_char in src_string:
            if src_char not in src_set:
                result += src_char
            
        return result
            