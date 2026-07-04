from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair positions with times to reach target
        cars = [(p, (target - p) / s) for p, s in zip(position, speed)]
        
        # Sort by position descending (closest to target first)
        cars.sort(reverse=True)
        
        fleets = 0
        max_time = 0
        
        for _, time in cars:
            if time > max_time:
                fleets += 1
                max_time = time  # new fleet leader
            # else: merges into existing fleet
        
        return fleets
