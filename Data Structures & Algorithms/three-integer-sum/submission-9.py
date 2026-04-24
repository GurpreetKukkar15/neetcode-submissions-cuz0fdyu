class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums)<3:
            return[]

        nums.sort()

        n = len(nums)
        res = []

        for i in range(n):
            # skip condition
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # process i
            # get ll, new_r for the 2 sum
            target = -nums[i]
            new_l = i + 1
            new_r = n - 1
            while new_l < new_r:
                add = nums[new_l]+ nums[new_r]
                if add > target:
                    new_r -=1
                if add < target:
                    new_l += 1
                if add == target:
                    res.append([nums[i], nums[new_l], nums[new_r]])
                    new_l += 1
                    new_r -= 1
                    while new_l < new_r and nums[new_l] == nums[new_l - 1]:
                        new_l += 1
                        # Skip all duplicates for the right pointer
                    while new_l < new_r and nums[new_r] == nums[new_r + 1]:
                        new_r -= 1
        return res                



