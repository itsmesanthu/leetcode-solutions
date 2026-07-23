class Solution:
    def strfilter(self,s):
        n=""
        for i in range(0,len(s)):
            if "A"<=s[i]<="Z":
                n+=chr(ord(s[i])+32)
            if "a"<=s[i]<="z"or"0"<=s[i]<="9":
                n+=s[i]
        return n
    def isPalindrome(self, s: str) -> bool:
        s=self.strfilter(s)
        i,j=0,len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True

