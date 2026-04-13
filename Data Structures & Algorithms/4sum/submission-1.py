class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        [-3,0,1,2,3,3]
        for i in range(len(nums)-1):
            if i!=0 and nums[i]==nums[i-1]:
                continue

            for j in range(i+1,len(nums)):
                if j!= i+1 and nums[j]==nums[j-1]:
                    continue

                new_target= target - nums[i] - nums[j]
                m, n = j+1, len(nums)-1
                while m < n:
                    if nums[m]+nums[n] > new_target:
                        n-=1
                    elif nums[m]+nums[n] < new_target:
                        m+=1
                    else:
                        res.append([nums[i],nums[j],nums[m],nums[n]])

                        while m < n and nums[m+1]==nums[m]:
                                m+=1
                        while m < n and nums[n-1]==nums[n]:
                                n-=1
                        n-=1
                        m+=1
        return res

