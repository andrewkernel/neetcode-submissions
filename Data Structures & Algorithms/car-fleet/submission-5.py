class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed), reverse=True)
        fleets = 0
        slowest_ahead_time = 0.0

        for pos, vel in cars:
            arrival_time = (target - pos) / vel

            if arrival_time > slowest_ahead_time:
                fleets += 1
                slowest_ahead_time = arrival_time

        return fleets