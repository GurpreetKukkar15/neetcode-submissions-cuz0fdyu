class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        


        # make a heap of the input - O(n)
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
        #pop the first 2 element to get the 2 heaviest stones
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

        # case logic
        # if x == y, do nothing
        # if x < y, reduce y = y - x
            if y > x:
    
            # push y into the heap again
                heapq.heappush(stones, x-y)
        
        # if no element in the heap we append 0 to it
        stones.append(0)

        # return the first element in the list
        return abs(stones[0])