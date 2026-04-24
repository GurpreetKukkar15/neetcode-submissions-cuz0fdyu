class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def counter(l):
            char_count = {}  # Define dictionary inside the function
            for x in l:
                if x in char_count:
                    char_count[x] += 1  # Increment count
                else:
                    char_count[x] = 1  # Initialize count
            return char_count # Return the dictionary
        if(counter(s)==counter(t)):
            return True
        else:
            return False
