class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            res= []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i]<right[j]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j+=1
            return res + left[i:] + right[j:]
        
        def mergesort(array):
            if len(array)<=1:
                return array
            mid= len(array)//2
            left= mergesort(array[:mid])
            right= mergesort(array[mid:])
            return merge(left, right)
        return mergesort(nums)
