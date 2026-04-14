class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area= 0
        for i in range(len(heights)-1):
            j= len(heights)-1
            while i < j:
                width= j-i
                area= min(heights[i], heights[j]) * width
                if area > max_area:
                    max_area= area
                j-=1
        return max_area
            