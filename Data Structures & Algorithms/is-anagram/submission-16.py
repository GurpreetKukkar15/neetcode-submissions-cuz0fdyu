class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count= {}

        for num in s:
            count[num]= count.get(num, 0)+ 1
        
        for num in t:
            count[num]= count.get(num, 0)- 1
        
        for value in count.values():
            if value != 0:
                return False
        return True