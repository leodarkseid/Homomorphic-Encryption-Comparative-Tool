from Pyfhel import Pyfhel
import numpy as np


def main():
    HE = Pyfhel()
    bgv_params = {
    'scheme': 'BGV',
    'n': 2**13, 
    't': 65537, 
    't_bits': 20, 
    'sec': 128,
}
    HE.contextGen(**bgv_params)
    HE.keyGen() 
    HE.rotateKeyGen()
    HE.relinKeyGen()
    a1 = 258048
    p1 = np.array([a1], dtype=np.int64)
    b1 = 258048
    p2 = np.array([b1], dtype=np.int64)

    ct1 = HE.encryptBGV(p1)
    ct2 = HE.encryptBGV(p2)
    print({"ct1": ct1, "ct2": ct2})

    at = a1 + b1
    print("at",at)

    ctt = ct1 + ct2
    print("ctt", ctt)

    print("dct1",HE.decryptBGV(ct1))
    print("dct2", HE.decryptBGV(ct2))
    print("dctt", HE.decrypt(ctt))

main()