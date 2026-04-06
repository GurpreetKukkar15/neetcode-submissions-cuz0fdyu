class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= {}
        for num in nums:
            count[num]= count.get(num, 0)+1
        buckets= [[] for _ in range(len(nums)+ 1)]
        for key, value in count.items():
            buckets[value].append(key)
        lis= []
        for i in range(len(buckets)-1, -1, -1):
            if len(lis) == k:
                return lis
            else:
                lis.extend(buckets[i])