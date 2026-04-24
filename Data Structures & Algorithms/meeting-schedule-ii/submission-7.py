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
        
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s = 0
        e = 0
        count = 0
        res = 0

        while s < len(intervals):

            if start[s] < end[e]:
                # overlap
                count +=1 
                s +=1 
            
            else: # start[s] < end[e]:
                # not overlap room became free
                count -=1 
                e +=1
            res = max(res, count)
        
        return res