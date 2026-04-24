class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_duplicate = len(nums) != len(set(nums))

        return has_duplicate
        