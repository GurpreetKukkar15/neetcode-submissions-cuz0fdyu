class Solution:
    def jump(self, nums: List[int]) -> int:
        l , r = 0, 0

        jump = 0

        while r < len(nums) - 1:
            farthest = 0


            for i in range(l, r + 1): # [l,r]
                farthest = max(farthest, i + nums[i])
            
            l = r + 1
            r = farthest
            
            jump +=1

        return jump
