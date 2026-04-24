class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        tx , ty, tz = target

        foundX , foundY, foundZ = False, False, False

        for t in triplets:
            a , b, c = t

            if a > tx or b > ty or c > tz:
                continue
            
            if a == tx: foundX= True
            if b == ty: foundY= True
            if c == tz: foundZ = True

            if foundX and foundY and foundZ:
                return True
        
        return False