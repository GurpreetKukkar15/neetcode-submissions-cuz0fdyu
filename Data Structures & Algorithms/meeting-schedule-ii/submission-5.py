"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
            
        # 1. Separate and Sort Start/End times
        # We handle them as independent events in the universe
        start_times = sorted([i.start for i in intervals])
        end_times = sorted([i.end for i in intervals])
        
        s, e = 0, 0
        count = 0
        res = 0
        
        # 2. Iterate through all Start times
        while s < len(intervals):
            
            # Case A: Need a new room
            # The next meeting starts BEFORE the earliest ending meeting finishes
            if start_times[s] < end_times[e]:
                count += 1
                s += 1
            
            # Case B: Room freed up
            # A meeting ended. We can reuse this room for the current start.
            # (Technically we decrement count, then increment for the new start,
            # so they cancel out. We just move both pointers).
            else:
                count -= 1
                e += 1
            
            # Update the global maximum demand we've seen so far
            res = max(res, count)
            
        return res