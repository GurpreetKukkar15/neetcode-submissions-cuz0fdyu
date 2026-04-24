class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        return true if s and t are anagram
        all the character in s and t are same
            - maybe in different order

        we can build a counter of s

        then for each element of t
            check if that element exist in the counter
                - we need to keep the count in mind race/acerr
            instead we can reduce the occurence of that element in the counter
            and if at any point we find something not in counte
                return False
            and if at any point the counter goes negative
                return False
        return True - loop condition was completed
        '''
        f = Counter(s)
        if len(t) != len(s):
            return False
        for char in t:
            if char not in f:
                return False
            if char in f:
                f[char] -= 1
                if f[char] < 0:
                    return False
        return True
