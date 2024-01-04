from dataclasses import dataclass
from typing import List

from core.range_base import RangeBase


@dataclass
class RangePipeline(RangeBase):
    ranges: List[RangeBase]

    def execute(self, src_string: str) -> str:
        result = src_string
        for rng in self.ranges:
            result = rng.execute(result)

        return result
