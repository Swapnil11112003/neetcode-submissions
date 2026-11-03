class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            l, r = 0, len(matrix[i]) - 1
            
            if target < matrix[i][r]:
                while l <= r:
                    mid = (l + r) // 2
                    if target > matrix[i][mid]:
                        l = mid + 1
                    elif target < matrix[i][mid]:
                        r = mid - 1
                    else:
                        return True
                return False
            elif target > matrix[i][r]:
                continue
            else:
                return True

        return False

                
            
        