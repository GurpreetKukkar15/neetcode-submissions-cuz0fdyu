class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total= sum(weights)
        l, r= max(weights), total
        while l < r:
            mid= (l+r)//2
            current_load= 0
            days_needed =1
            for weight in weights:
                if current_load + weight > mid:
                    current_load= weight
                    days_needed+=1
                else:
                    current_load+=weight
            if days_needed <= days:
                r= mid



            else:
                l= mid + 1
        return l
        