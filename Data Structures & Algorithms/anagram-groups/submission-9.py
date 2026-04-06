class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res= {}
        for word in strs:
            count= [0]*26
            for c in word:
                count[ord(c)-ord('a')]+=1
            key= tuple(count)
            if key not in res:
                res[key]= [word]
            else:
                res[key].append(word)
        return list(res.values())