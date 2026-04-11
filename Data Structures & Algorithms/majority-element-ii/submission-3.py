class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, count1= None,  0
        num2, count2= None, 0
        for num in nums:
            if num1 == num:
                count1+=1

            elif num2 == num:
                count2+=1
            
            elif count1 == 0:
                num1 = num
                count1= 1
            elif count2 ==0:
                num2= num
                count2= 1
            else:
                count1-=1
                count2-=1
        res= []
        if nums.count(num1) > len(nums)//3:
           res.append(num1)
        if nums.count(num2) > len(nums)//3:
            res.append(num2)
        return res


            
