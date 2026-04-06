class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count= {}
        number= 0
        max_count= 0
        for num in nums:
            if num not in count:
                count[num]= 0
            count[num]+= 1
            if count[num]> max_count:
                max_count= count[num]
                number= num
        return number
                

        
      