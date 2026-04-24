class Solution:
    def search(self, nums: List[int], target: int) -> int:
         # left, right pointer
         l, r = 0, len(nums)-1
        
        # while l is less than or equal to r
         while l<=r:
            # update the middle
            m = (l + r) // 2
            # case by case
            # case 1.
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
         return -1