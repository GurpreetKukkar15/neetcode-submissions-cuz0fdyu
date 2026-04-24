class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        we can trade of space to solve this problem
        '''

        # for all the elements in the nums
            # check if the element exist in the set()
                # return true
            # add the element in the set()
        # return false - implying the above itreation didn't return true
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        
