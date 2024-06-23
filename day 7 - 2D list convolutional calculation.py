# Định nghĩa ma trận A và kernal B
mat_a = [[0, 0, 0, 4],[0, 4, 0, 2],[0, 1, 0, 2],[0, 3, 0, 2]]
kernal_b = [[1, 1], [1, 1]]


# Hàm để tính max pooling
def max_pooling(matrix, kernel_size):
    pooled_matrix = []
    for i in range(0, len(matrix), kernel_size):
        row = []
        for j in range(0, len(matrix[0]), kernel_size):
            block = [matrix[x][j:j + kernel_size] for x in range(i, i + kernel_size)]
            max_value = max([max(row) for row in block])
            row.append(max_value)
        pooled_matrix.append(row)
    return pooled_matrix

# Hàm để tính average pooling
def average_pooling(matrix, kernel_size):
    pooled_matrix = []
    for i in range(0, len(matrix), kernel_size):
        row = []
        for j in range(0, len(matrix[0]), kernel_size):
            block = [matrix[x][j:j + kernel_size] for x in range(i, i + kernel_size)]
            sum_value = sum([sum(row) for row in block])
            avg_value = sum_value / (kernel_size * kernel_size)
            row.append(avg_value)
        pooled_matrix.append(row)
    return pooled_matrix

# Tính max pooling và average pooling
kernel_size = len(kernal_b)
max_pool_result = max_pooling(mat_a, kernel_size)
avg_pool_result = average_pooling(mat_a, kernel_size)


print(max_pooling(mat_a, kernel_size))
print(average_pooling(mat_a, kernel_size))