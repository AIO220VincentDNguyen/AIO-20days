# day 4
import numpy as np

def convol2d_manual(matrix, kernel):
    m, n = matrix.shape
    k, l = kernel.shape

    result_height = m - k + 1
    result_width = n - l + 1

    result = np.zeros((result_height, result_width))

    for i in range(result_height):
        for j in range(result_width):
            sub_matrix = matrix[i:i+k, j:j+l]
            result[i, j] = np.sum(sub_matrix * kernel)
    return result

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[2, 4],
              [1, 3]])

C = np.array([[1, 1, 1],
              [0, 0, 0],
              [1, 1, 1]])

result_B = convol2d_manual(A, B)
result_C = convol2d_manual(A, C)

print('result B :', result_B)
print('result C :', result_C)

# day 5

corpus = ['Tôi thích môn Toán', 'Tôi thích AI', 'Tôi thích âm nhạc']

vocabulary = []
for sentence in corpus:
    words = sentence.split()
    for word in words:
        if word not in vocabulary:
            vocabulary.append(word)

vocabulary = sorted(vocabulary)

def sentence_to_bow(sentence, vocabulary):
    words = sentence.split()
    bow_vector = np.zeros(len(vocabulary), dtype = int)
    for word in words:
        if word in vocabulary:
            index = vocabulary.index(word)
            bow_vector[index] += 1
    return bow_vector

sentence = 'Tôi thích AI thích Toán'
bow_vector = sentence_to_bow(sentence, vocabulary)

print('vector Bow: ', bow_vector)
print('Bag of Words:', vocabulary)

# day 6

def pad_matrix(matrix, pad):
    m, n = matrix.shape
    padded_matrix = np.zeros((m + 2 * pad, n + 2 * pad))
    padded_matrix[pad:pad + m, pad:pad + n] = matrix
    return padded_matrix

def convolve2d_with_padding(matrix, kernel):
    m, n = matrix.shape
    k, l = kernel.shape

    result_height = m
    result_width = n

    result = np.zeros((result_height, result_width))
    padded_matrix = pad_matrix(matrix, k // 2)

    for i in range(result_height):
        for j in range(result_width):
            sub_matrix = padded_matrix[i:i + k, j:j + l]
            result[i][j] = np.sum(sub_matrix * kernel)
    return result
A = np.array([[0, 0, 0],
    [0, 4, 0],
    [0, 1, 0]])

B = np.array([[1, 1],
    [1, 1]])

C = np.array([[0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]])


result_B = convolve2d_with_padding(A, B)

result_C = convolve2d_with_padding(A, C)

print('result B :', result_B)
print('result C :', result_C)

# day 7

def max_pooling(matrix, size = 2, stride = 2):
    m, n = matrix.shape
    pool_height = (m - size) // stride + 1
    pool_width = (n - size) // stride + 1

    pooled_matrix = np.zeros((pool_height,pool_width))

    for i in range(0, m - size + 1, stride):
        for j in range(0, n - size + 1, stride):
            pooled_matrix[i // stride, j // stride] = np.max(matrix[i:i + size, j:j + size])
    return pooled_matrix

def average_pooling(matrix, size = 2, stride = 2)
    m, n = matrix.shape
    pooled_height = (m - size) // stride + 1
    pooled_width = (n - size)// stride + 1

    pooled_matrix = np.zeros((pooled_height, pooled_width))

    for i in range(0, m - size + 1, stride):
        for j in range( 0, n - size + 1, stride):
            pooled_matrix[i // stride, j // stride] = np.mean(matrix[i:i + size, j:j + size])
    return pooled_matrix

A = np.array([[0, 0, 0, 4],
              [0, 4, 0, 2],
              [0, 1, 0, 2],
              [0, 3, 0, 2]])


max_pool_result = max_pooling(A)
avg_pool_result = average_pooling(A)

print('Max Pooling result:\n', max_pool_result)
print('Average Pooling result:\n', avg_pool_result)

