import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # find k such that the we can finish the whole thing in h hours
        # k should me at max the max value in the piles
        # we can start at that rate, say 25 we start at 25,
        # but there could be a value in between

        # k is bounded by [ 1, max(p)], so we do a binary search on k
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)

            if hours <= h:
                r = k - 1
                res = min(res, k)
            elif hours > h:
                l = k + 1
        return res

            

