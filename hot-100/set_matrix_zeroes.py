#Time complexity  :O(M*N)
#Space Complexity :O(1)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #1. Check if the first row and first column have any zeros
        row_have_zero=False
        column_have_zero=False

        for j in range(len(matrix[0])): 
            if matrix[0][j]==0:
                row_have_zero=True
                break
        
        for i in range(len(matrix)): 
            if matrix[i][0]==0:
                column_have_zero=True
                break
        # 2. Use the first row and column to mark rows/columns to be zeroed
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] =0 
        # 3. Set rows to zero based on markers        
        for i in range(1,len(matrix)):
            if  matrix[i][0] == 0:
                matrix[i] = [0] * len (matrix[0])
        # 4. Set column to zero based on markers
        for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0:
                    for i in range (len(matrix)):
                        matrix[i][j] = 0 
        # 5. Zero out the first row if needed
        if row_have_zero ==True:
            matrix[0] = [0] * len(matrix[0])
        # 6. Zero out the first column if needed
        if column_have_zero == True :
            for i in range(len(matrix)):
                matrix[i][0]=0


        
