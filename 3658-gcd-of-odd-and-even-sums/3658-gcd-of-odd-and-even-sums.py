class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even=n*(n+1)
        odd=n*n
        ans=even-odd
        return ans