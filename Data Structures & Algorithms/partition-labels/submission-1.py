class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {c:i for i,c in enumerate(s)}

        res = []
        start = 0
        size = 0
        end = 0

        for i,c in enumerate (s):
            size += 1

            end = max(end, last_index[c])

            if i == end:
                res.append(size)
                size = 0
                start = 0
                
        return res




