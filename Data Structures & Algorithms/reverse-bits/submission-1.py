class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            # extract the bit from the n
            cur_bit = n & 1

            # paste the bit in the res
            res = res << 1 # shifts the res by 1 to the left
            res = res | cur_bit

            # move the n left shift for next iterations
            n = n >> 1
        
        return res