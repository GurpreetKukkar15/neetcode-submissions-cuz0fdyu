class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total_tank = 0
        start = 0
        for i in range(len(gas)):
            # find the total tank now
            total_tank += gas[i] - cost[i]

            # see if this is negative 
            # and if it is reset it and start at the next gas station index i +1
            if total_tank < 0:
                total_tank = 0
                start = i + 1
        return start
