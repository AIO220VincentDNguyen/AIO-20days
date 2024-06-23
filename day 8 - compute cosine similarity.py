import math

A = [1, 2]
B = [4, 5]

# tính tích vô hướng
def scalar_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

# tính độ lớn của vector
def magnitube(v):
    return math.sqrt(sum(x ** 2 for x in v))

# tính cosine similarity
def cosine_similarity(v1,v2):
    return scalar_product(v1, v2)/ (magnitube(v1) * magnitube(v2))

print(f'{cosine_similarity(A, B): .3f}')