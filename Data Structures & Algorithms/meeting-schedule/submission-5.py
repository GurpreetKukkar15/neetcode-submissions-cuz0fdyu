"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # basically we have to determine if an overlap exist and return False if it does

        # intervals.sort(key = lambda x: x[0])

        # 1. Sort by Start Time
        intervals.sort(key=lambda x: x.start)
        
        # 2. Iterate through the meetings
        for i in range(1, len(intervals)):
            prev_end = intervals[i-1].end
            curr_start = intervals[i].start
            
            # 3. Collision Check
            # If the current meeting starts BEFORE the previous one finishes...
            if curr_start < prev_end:
                return False
                
        return True

            