class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count= dict()
        for i in s:
            count[i]= count.get(i, 0)+1
        for i in t:
            count[i]= count.get(i,0)-1
        
        for values in count.values():
            if values != 0:
                return False

        return True