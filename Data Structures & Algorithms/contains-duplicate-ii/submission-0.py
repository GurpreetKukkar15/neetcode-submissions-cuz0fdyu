class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        index_track= {}
        for i in range(len(nums)):
            if nums[i] in index_track and i - index_track[nums[i]] <= k:
                return True
            index_track[nums[i]]=i
        return False