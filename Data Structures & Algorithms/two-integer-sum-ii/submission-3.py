class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [1,2,3,4]
        # so we take 1 + 4 = 5
        # say target is 4 so sum < 5
        # means we can ignore the 5, since this is the min sum it can have
        # and say target is 7 so sum > 5, we need to incr the min to catch the sum

        # l , r pointer
        l = 0
        r = len(numbers) - 1

        # while l and r do not cross
        while l < r:
            # sum = l + r
            summ = numbers[l] + numbers[r]
            # if sum is more than target, we move r inside
            if summ > target:
                r -=1
            if summ < target:
                l += 1
            if summ == target:
                break
        return [l + 1, r + 1]
