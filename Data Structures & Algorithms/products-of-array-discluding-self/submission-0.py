from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        int arr - nums
        return output
            - output[i] is product of all elemetn of nums except nums[i]
        
        Your idea is perfect: prefix * postfix
        Let's implement that in an O(1) space solution.
        '''
        
        n = len(nums)
        # We will use the output array to first store all the prefix products
        output = [1] * n 
        
        # [1, 2, 3, 4]
        
        # 1. First pass: Calculate and store prefix products in 'output'
        # output[i] will store the product of all numbers *before* nums[i]
        prefix_product = 1
        for i in range(n):
            output[i] = prefix_product  # Store the product *before* this element
            prefix_product *= nums[i]   # Update the product for the *next* element
        
        # After this loop, 'output' looks like: [1, 1, 2, 6]
        # This is our prefix array!

        # 2. Second pass: Calculate postfix products and multiply
        # We go in reverse and use a single variable for the postfix product
        postfix_product = 1
        for i in range(n - 1, -1, -1): # Iterate from the end (n-1) down to 0
            # output[i] (which is the prefix) * postfix_product
            output[i] *= postfix_product # Multiply the existing prefix value by the postfix product
            postfix_product *= nums[i]   # Update the postfix product for the *next* (left) element
        
        # How the second loop runs:
        # i = 3: output[3] = 6 * 1 = 6.  postfix_product becomes 1 * 4 = 4
        # i = 2: output[2] = 2 * 4 = 8.  postfix_product becomes 4 * 3 = 12
        # i = 1: output[1] = 1 * 12 = 12. postfix_product becomes 12 * 2 = 24
        # i = 0: output[0] = 1 * 24 = 24. postfix_product becomes 24 * 1 = 24
        
        # Final output: [24, 12, 8, 6]
        
        return output