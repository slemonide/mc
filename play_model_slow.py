#!/usr/bin/env python3

import pickle
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import svds, eigs
import matplotlib.pyplot as plt
import numpy as np
import time

pickle_in = open("char_to_ix.pickle","rb")
char_to_ix = pickle.load(pickle_in)

pickle_in = open("ix_to_char.pickle","rb")
ix_to_char = pickle.load(pickle_in)

mc = np.load('mc.npy')

# randomly choose initial character
char = np.random.choice(range(mc.shape[0]), 1, p=mc[0,:]/np.sum(mc[0,:]))[0]


while True:
    print(ix_to_char[char], end="", flush=True)
    char = np.random.choice(range(mc.shape[0]), 1, p=mc[char,:]/np.sum(mc[char,:]))[0]
    time.sleep(0.05)

