class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Build character count for s
        a = {}
        for i in s:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1

        # Step 2: Build character count for t
        b = {}
        for i in t:
            if i in b:
                b[i] += 1
            else:
                b[i] = 1

        # Step 3: Compare the two dictionaries
        return a == b
