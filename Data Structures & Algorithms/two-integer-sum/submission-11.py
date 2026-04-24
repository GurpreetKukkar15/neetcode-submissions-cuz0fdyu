class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        return i, j
            - where nums[i] + nums[j] = target
            - and i != j - the same element is not used twice
        
        solution exist always

        return with smaller of the i or j first 

        make a seen set() --->
        for all the element in the nums:
            - add it to the seen() 
            - calculate the complement
            - if complement in seen:
                - return the current index ---> this implies we need to store the index with the element

        return False
        '''

        seen = defaultdict() # add ( element, index )
        for i,j in enumerate(nums):
            complement = target - j
            if complement in seen:
                return [seen[complement],i]
            seen[j]=i

