class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count={}
        result=[]
        max= len(nums)/3
        for num in nums:
            count[num]= count.get(num, 0)+1
        for key, value in count.items():
            if value > max:
                result.append(key)
        return result
