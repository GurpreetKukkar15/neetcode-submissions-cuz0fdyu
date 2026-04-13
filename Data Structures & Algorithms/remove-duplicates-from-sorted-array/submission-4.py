class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j, k=0, 1, 0
        while j < len(nums):
            if nums[i]==nums[j]:
                j+=1

            else:
                nums[i+1]=nums[j]
                i+=1
                j+=1
                k+=1
        return k+1