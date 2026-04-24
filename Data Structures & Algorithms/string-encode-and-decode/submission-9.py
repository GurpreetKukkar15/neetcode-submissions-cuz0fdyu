class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode the string as 
        # neet as 4neet i.e (len)word - so we avoid whatever in the word and print it
        # i love you would be 1i4love3you
        res = []
        for word in strs:
            size = str(len(word))
            res.append(size)
            res.append('#')
            res.append(word)

        return "".join(res)


    def decode(self, s: str) -> List[str]:
        # decode the string
        #1i4love3you
        # see 1 append next 1 char "i", see 4 append next 4 char "love", see 3 append next 3 char "you"
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            word_size = int(s[i:j])
            word_start = j + 1
            word_end = word_start + word_size
            ans.append(s[word_start:word_end])
            i = word_end
        return ans

