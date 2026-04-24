class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        unsorted nums
            - random
        return kth largest element
            - so if k = 2, return the 2nd largest element
        
        understand eg.
        Input: nums = [2,3,1,5,4], k = 2
        
            sort.nums =[1,2,3,4,5]
            since k = 2 we return the 2nd largeste i.e 4 here
            return 4
        Clarifying question:
        what if k > len(nums)? contraints
        are there negative nums? yes

        solution:
        we make a maxHeap of size k,
        then we pop it k times ( return the kth largest element)
        since it will have the largest one at top in the start
        and then we pop k times to get kth largest
        '''
        maxHeap = []
        for n in nums:
            # we push the element in the max heap of size k
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, n)
            else:
                heapq.heappushpop(maxHeap, n)
        # # pop the heap k time
        # for _ in range(k):
        k = heapq.heappop(maxHeap)

        return k