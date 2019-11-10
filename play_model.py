#!/usr/bin/env python3

import pickle
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import svds, eigs
import matplotlib.pyplot as plt
import numpy as np


pickle_in = open("dict.pickle","rb")
example_dict = pickle.load(pickle_in)

# data I/O
data = open('input.txt', 'r').read() # should be simple plain text file
chars = list(set(data))
data_size, vocab_size = len(data), len(chars)
print('data has %d characters, %d unique.' % (data_size, vocab_size))
char_to_ix = { ch:i for i,ch in enumerate(chars) }
ix_to_char = { i:ch for i,ch in enumerate(chars) }

mc = np.zeros((vocab_size, vocab_size))
#mc = lil_matrix((vocab_size, vocab_size))  #np.zeros((vocab_size, vocab_size))


for i in range(data_size-1):
    if i % 1000000 == 0:
        print(i, data_size)

    cur = data[i]
    nex = data[i+1]

    mc[char_to_ix[cur], char_to_ix[nex]] += 1

np.save('mc', mc)

pickle_out = open("char_to_ix.pickle","wb")
pickle.dump(char_to_ix, pickle_out)
pickle_out.close()

pickle_out = open("ix_to_char.pickle","wb")
pickle.dump(ix_to_char, pickle_out)
pickle_out.close()

print("Number of non-zero entries : " + str(np.count_nonzero(mc)) + \
      " out of " + str(vocab_size*vocab_size) + ". Sparseness: " + \
      str(np.count_nonzero(mc)/(vocab_size*vocab_size)))

mc == 0

plt.imshow(mc)
plt.colorbar()
plt.show()
