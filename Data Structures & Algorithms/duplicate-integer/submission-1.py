from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(nums)
        # Example logic: check for duplicates
        return len(nums) != len(set(nums))

# Example usage:
nums = [1, 2, 3, 1]
sol = Solution()
print(sol.hasDuplicate(nums))  # Output: True
