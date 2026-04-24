class Solution:
    def countBits(self, n: int) -> List[int]:
        # the idea goes as follow

        # we divide the number by 2, and then add 1 to the number of bits from this
        # so num_of_bits(n) = 1 + num_of_bits(n//2)

        dp = [0]*(n+1)
        # [0..0]

        for i in range(1, n + 1):
            # 1,2,3,...n

            prefix_count = dp[i>>1] # getting the count from i //2

            lsb = i & 1

            dp[i] = prefix_count + lsb
        return dp

            
            

