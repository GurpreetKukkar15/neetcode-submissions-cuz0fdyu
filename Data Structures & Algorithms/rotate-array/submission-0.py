class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_k= k%len(nums)
        def reverse(arr, i, j):
            while i < j:
                arr[i], arr[j]= arr[j], arr[i]
                i+=1
                j-=1
            
        
        reverse(nums, 0, len(nums)-1)
        reverse(nums, 0, new_k-1)
        reverse(nums, new_k, len(nums)-1)