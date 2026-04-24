class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. Sort by Start Time (Crucial Step)
        intervals.sort(key=lambda x: x[0])
        
        # Initialize with the first interval to avoid empty checks in loop
        output = [intervals[0]]
        
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            
            # 2. Overlap Check
            if start <= lastEnd:
                # Merge: Extend the previous interval's end
                # Note: We use max() because the current interval might be 
                # completely inside the previous one (e.g., [1, 5] and [2, 3])
                output[-1][1] = max(lastEnd, end)
            else:
                # No Overlap: Add as new interval
                output.append([start, end])
                
        return output