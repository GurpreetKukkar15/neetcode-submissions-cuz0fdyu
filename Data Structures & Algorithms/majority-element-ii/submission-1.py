class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count={}
        result=[]
        threshold= len(nums)//3
        for num in nums:
            count[num]= count.get(num, 0)+1
        for key, value in count.items():
            if value > threshold:
                result.append(key)
        return result
