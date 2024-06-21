# this is a script for testing python's bfv
from Pyfhel import Pyfhel 
import numpy as np


HE:Pyfhel = Pyfhel()


HE.contextGen(scheme='bfv', n=8192, t_bits=20)

HE.keyGen()
# print(HE)

# integer1 = np.array([1], dtype=np.int64)
# integer2 = np.array([2], dtype=np.int64)

# cipher1 = HE.encryptInt(integer1)
# cipher2 = HE.encryptInt(integer2)

# print("int1", integer1, cipher1)
# cipher3 = cipher1 + cipher2
# print("resu;t",cipher3)

# #decrypt
# cipher4 = HE.decryptInt(cipher3)
# print("ci[her4",cipher4)



HE.rotateKeyGen()
HE.relinKeyGen()
# Then we encrypt some data
c = HE.encrypt(np.array([42]))
p = HE.encode(np.array([-1]))

print("1. Creating serializable objects")
print(f"  Pyfhel object HE: {HE}")
print(f"  PyCtxt c=HE.encrypt([42]): {c}")
print(f"  PyPtxt p=HE.encode([-1]): {p}")
# xx = cipher4 + np.array([1], dtype=np.int64)
# print("xxx", xx)
con_size, con_size_zstd   = HE.sizeof_context(),    HE.sizeof_context(compr_mode="zstd")
pk_size,  pk_size_zstd    = HE.sizeof_public_key(), HE.sizeof_public_key(compr_mode="zstd")
sk_size,  sk_size_zstd    = HE.sizeof_secret_key(), HE.sizeof_secret_key(compr_mode="zstd")
rotk_size,rotk_size_zstd  = HE.sizeof_rotate_key(), HE.sizeof_rotate_key(compr_mode="zstd")
rlk_size, rlk_size_zstd   = HE.sizeof_relin_key(),  HE.sizeof_relin_key(compr_mode="zstd")
c_size,   c_size_zstd     = c.sizeof_ciphertext(),  c.sizeof_ciphertext(compr_mode="zstd")
# alternatively, for ciphertext sizes you can use sys.getsizeof(c)

print("2. Checking size of serializable objects (with and without compression)")
print(f"   - context:    [ \"zstd\"  --> {con_size_zstd} | No compression --> {con_size}]")
print(f"   - public_key: [ \"zstd\"  --> {pk_size_zstd} | No compression --> {pk_size}]")
print(f"   - secret_key: [ \"zstd\"  --> {sk_size_zstd} | No compression --> {sk_size}]")
print(f"   - relin_key:  [ \"zstd\"  --> {rotk_size_zstd} | No compression --> {rotk_size}]")
print(f"   - rotate_key: [ \"zstd\"  --> {rlk_size_zstd} | No compression --> {rlk_size}]")
print(f"   - c:          [ \"zstd\"  --> {c_size_zstd} | No compression --> {c_size}]")