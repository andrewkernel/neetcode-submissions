from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        fleet_time_ahead = 0.0
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > fleet_time_ahead:
                fleets += 1
                fleet_time_ahead = time
        return fleets