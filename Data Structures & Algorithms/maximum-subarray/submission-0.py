class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        maxS = float('-inf')

        for n in nums:
            if cur < 0:
                cur = 0
            cur += n
            maxS = max ( maxS, cur)
        
        return maxS