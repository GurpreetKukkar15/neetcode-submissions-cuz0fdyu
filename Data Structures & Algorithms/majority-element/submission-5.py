class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count= {}
        for num in nums:
            count[num]= count.get(num,0)+1
        max_val= max(count.values())
        for key, value in count.items():
            if value == max_val:
                return key