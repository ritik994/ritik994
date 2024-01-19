def print_spiral(matrix):
    if not matrix:
        return []
    rows, cols = len(matrix), len(matrix[0])
    result = []
    top, bottom, left, right = 0, rows - 1, 0, cols - 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result
matrix_example = [
    [1, 2, 3,88],
    [4, 5, 6,98],
    [7, 8, 9,100]
]

result_spiral = print_spiral(matrix_example)
print(result_spiral)