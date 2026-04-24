class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diction = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in diction:
                return [diction[complement], i]
            diction[num] = i
            
