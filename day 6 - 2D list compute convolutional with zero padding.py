# Ma trận đầu vào và kernel
mat_a = [
    [0, 0, 0],
    [0, 4, 0],
    [0, 1, 0]
]

kernal_b = [
    [1, 1],
    [1, 1]
]

kernal_c = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]

# Hàm padding
def pad_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    pad = 0
    padded_matrix = [[0] * (m + 2 * pad) for _ in range(n + 2 * pad)]
    for i in range(m):
        for j in range(n):
            padded_matrix[i + pad][j + pad] = matrix[i][j]
    return padded_matrix

# Hàm convolution
def convolve(matrix, kernel):
    km = len(kernel)
    kn = len(kernel[0])
    m = len(matrix)
    n = len(matrix[0])
    result_rows = m - km + 1
    result_cols = n - kn + 1
    result = [[0] * result_cols for _ in range(result_rows)]

    for i in range(result_rows):
        for j in range(result_cols):
            sum_val = 0
            for ki in range(km):
                for kj in range(kn):
                    sum_val += matrix[i + ki][j + kj] * kernel[ki][kj]
            result[i][j] = sum_val
    return result

# Áp dụng zero padding và thực hiện convolution với kernel B
padded_a = pad_matrix(mat_a)
result_b = convolve(padded_a, kernal_b)

# Áp dụng zero padding và thực hiện convolution với kernel C
padded_a = pad_matrix(mat_a)
result_c = convolve(padded_a, kernal_c)

# In kết quả
print("Output:")
print("- Câu 1:", result_b)
print("- Câu 2:", result_c)