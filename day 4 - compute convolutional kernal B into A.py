# Định nghĩa ma trận A và các kernal B, C
mat_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
kernel_b = [[2, 4], [1, 3]]
kernel_c = [[1, 1, 1], [0, 0, 0], [1, 1, 1]]

# Hàm để thực hiện phép convolution
def convolve(matrix, kernel):
    m = len(matrix)
    n = len(matrix[0])
    km = len(kernel)
    kn = len(kernel[0])
    output = []

    for i in range(m - km + 1):
        row = []
        for j in range(n - kn + 1):
            sum_val = 0
            for ki in range(km):
                for kj in range(kn):
                    sum_val += matrix[i + ki][j + kj] * kernel[ki][kj]

            row.append(sum_val)
        output.append(row)

    return output

# Tính convolution của A với B và C
result_b = convolve(mat_a, kernel_b)
result_c = convolve(mat_a, kernel_c)

print("Câu 1: ", result_b)
print("Câu 2: ", result_c)
