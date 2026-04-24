class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for i in nums:
            count = count + 1 if i == 1 else 0
            max_count = max(count, max_count)

        return max_count

        