def rotateArray(matrix):
    row = len(matrix)
    col = len(matrix[0])

    for i in range(row):
        for j in range(i,col):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    print(matrix)

    for i in range(row):
        low,high = 0,col-1
        while(low<=high):
            matrix[i][low],matrix[i][high] = matrix[i][high],matrix[i][low]
            low+=1
            high-=1
    return matrix


arr = [[1,2,3],[4,5,6],[7,8,9]]
print(rotateArray(arr))


class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(matrix):
            for i in range(len(matrix)):
                for j in range(i, len(matrix[0])):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        def reverse_rows(matrix):
            for r in range(len(matrix)):
                left, right = 0, len(matrix) - 1
                while left < right:
                    matrix[r][left], matrix[r][right] = matrix[r][right], matrix[r][left]
                    left += 1
                    right -= 1

        transpose(matrix)
        print(matrix)
        reverse_rows(matrix)
        return matrix


# arr = [[1,2,3],[4,5,6],[7,8,9]]
# sol = Solution()
# print(sol.rotate(arr))