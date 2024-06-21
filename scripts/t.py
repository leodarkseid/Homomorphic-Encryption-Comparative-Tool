from Pyfhel import Pyfhel
import numpy as np
import sys

HE = Pyfhel()
HE.contextGen(scheme='bfv', n=8192, t_bits=20)
HE.keyGen()
message1 = np.array([1] , dtype=np.int64)

cipherTxt1 = HE.encryptInt(message1)

m1 = 1
message2 = np.array([2], dtype=np.int64)
cipherTxt2 = HE.encryptInt(message2)
total = cipherTxt2 + cipherTxt1

contextSize = HE.sizeof_context()
print("c", contextSize)
publicKeySize = HE.sizeof_public_key()
cSize1 = cipherTxt1.sizeof_ciphertext()
cSize2 = sys.getsizeof(cipherTxt1)
print("c",publicKeySize )
print("cSIze1", cSize1)
print("csize2", cSize2)

r = HE.decryptInt(total)
print("HE",r[0])
print("plain", 1 + 2)
print(HE.get_scheme())
print("28",sys.getsizeof("1"))
print("size of m1", sys.getsizeof(m1))
print("size of m1", sys.getsizeof([1]))
print("size of message", sys.getsizeof(message1))
print(message1)