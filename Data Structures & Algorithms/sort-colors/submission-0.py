class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def mergesort(arr):
            if len(arr)<=1:
                return arr
            
            left_arr= mergesort(arr[:len(arr)//2])
            right_arr= mergesort(arr[len(arr)//2:])
            

            i, j, k= 0, 0, 0
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i]< right_arr[j]:
                    arr[k]= left_arr[i]
                    i+=1
                else:
                    arr[k]= right_arr[j]
                    j+=1
                k+=1
            while i < len(left_arr):
                arr[k]= left_arr[i]
                i+=1
                k+=1
            while j < len(right_arr):
                arr[k]= right_arr[j]
                j+=1
                k+=1
            return arr
        
        return mergesort(nums)