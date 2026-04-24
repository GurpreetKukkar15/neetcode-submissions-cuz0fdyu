class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        new_num = n
        # you call helper till you either find 1 or find a reapeated value
        while new_num != 1 and new_num not in seen:
            seen.add(new_num)
            new_num = self.SquareSum(new_num)
        return new_num == 1

    def SquareSum(self, num):

        ans = 0
        while num > 0:
            # get the digit
            digit = num % 10

            # add the square of the digit
            ans += digit**2
            num = num // 10
        return ans
    