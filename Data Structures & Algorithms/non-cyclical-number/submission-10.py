class Solution:
    def isHappy(self, n: int) -> bool:
        
        fast = self.SquareSum(n)
        slow = n
        # you call helper till you either find 1 or find a reapeated value
        while fast != 1 and fast != slow:
            slow = self.SquareSum(slow)
            fast = self.SquareSum(self.SquareSum(fast))
        return fast == 1

    def SquareSum(self, num):

        ans = 0
        while num > 0:
            # get the digit
            digit = num % 10

            # add the square of the digit
            ans += digit**2
            num = num // 10
        return ans
    