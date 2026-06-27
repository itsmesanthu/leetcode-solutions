class Solution:
    def maxArea(self, height: List[int]) -> int:
        an=0
        i,j=0,len(height)-1
        while i<j:
            h=min(height[i],height[j])
            w=j-i
            an=max(an,h*w)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return an