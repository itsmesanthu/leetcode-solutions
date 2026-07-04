class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        i=0
        j=row*col-1
        while i<=j:
            m=(i+j)//2
            r=m//col
            c=m%col
            if matrix[r][c]==target:
                return True
            if matrix[r][c]<target:
                i=m+1
            else:
                j=m-1
        return False