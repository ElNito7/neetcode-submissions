class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix)-1, len(matrix[0])-1
        s, e, mid = 0, m, 0
        row = matrix[0]
        while e >= s:
            mid = s + (e-s) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                if matrix[mid][-1] >= target:
                    row = matrix[mid]
                    break
                s = mid+1
            else:
                e = mid-1
            row = matrix[mid]
        
        s, e = 0, n
        while e >= s:
            mid = s + (e-s) // 2
            if row[mid] == target:
                return True
            if row[mid] < target:
                s = mid+1
            else:
                e = mid-1
        
        return False