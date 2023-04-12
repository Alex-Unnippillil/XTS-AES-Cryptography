# -*- coding: utf-8 -*-
"""
Alex Unnippillil
Cryptography Cipher XTS-AES 
"""

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend 

import time


backend = default_backend()
k = b'001001001'
text = 'qwertgyhujik'
iv = os.urandom(128)
mode = modes.XTS(text)
ms = modes.XTS(iv)
print(' time ' + '\t' + 'outputsize')
for m in ms:

    cip1 = Cipher(algorithms.XTS(k), m, backend=backend)
    encryptor1 = cip1.encryptor()

    t1 = time.time()
    ct1 = encryptor1.update(text)
    t2 = time.time()
    encryptor1.finalize()
    
