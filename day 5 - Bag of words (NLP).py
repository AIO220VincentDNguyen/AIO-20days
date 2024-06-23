# Xử lý dataset
corpus = ['Tôi thích môn Toán', 'Tôi thích AI', 'Tôi thích âm nhạc']
vocabulary = (' '.join(corpus))
vocabulary = vocabulary.split()
vocabulary = set(vocabulary)
vocabulary = sorted(vocabulary)
# Request
input_str = 'Tôi thích AI thích Toán'
input_str = input_str.split()
vector_str = [input_str.count(word) for word in vocabulary]

print('Tôi thích AI thích Toán: ', vector_str)
print('Bag-Of-Word:', vocabulary)