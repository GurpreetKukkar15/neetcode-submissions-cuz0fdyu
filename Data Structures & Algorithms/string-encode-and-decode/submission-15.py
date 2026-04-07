class Solution:

    def encode(self, strs: List[str]) -> str:
        encode= ''
        for char in strs:
            encode+= str(len(char))+ '#' + char
        return encode
    def decode(self, s: str) -> List[str]:
        decode= []
        i=0
        while i < len(s):
            j= i
            while s[j]!='#':
                j+=1
            length= int(s[i:j])
            i= j + 1
            j= i + length
            decode.append(s[i:j])
            i=j
        return decode
