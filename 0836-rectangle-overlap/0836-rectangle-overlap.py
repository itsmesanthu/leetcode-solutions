class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        x1_1, y1_1, x2_1, y2_1 = rec1
        x1_2, y1_2, x2_2, y2_2 = rec2
       
        if (x2_2 <= x1_1 or  
            x1_2 >= x2_1 or  
            y2_2 <= y1_1 or  
            y1_2 >= y2_1):   
            return False
            
        return True
