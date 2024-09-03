from Pyfhel import Pyfhel
import numpy as np


def main():
    HE = Pyfhel()
    bgv_params = {
        'scheme': 'BGV',
        'n': 2**13,
        't': 2**54,
        # 't': 2**20,
        't_bits': 54,
        'sec': 256,
    }
    HE.contextGen(**bgv_params)
    HE.keyGen()
    # HE.rotateKeyGen()
    # HE.relinKeyGen()
    a1 = 70000000000000
    p1 = HE.encode(np.array([a1]))
    b1 = 200000
    p2 = HE.encode(np.array([b1]))

    ct1 = HE.encrypt(p1)
    ct2 = HE.encrypt(p2)
    print({"ct1": ct1, "ct2": ct2})
    print({"ct1": ct1.scheme})

    # print("Initial noise budget for ct1:", HE.noise_level(ct1))
    # print("Initial noise budget for ct2:", HE.noise_level(ct2))

    print("Decrypted ct1:", HE.decrypt(ct1))
    print("Decrypted ct2:", HE.decrypt(ct2))

    at = a1 + b1
    print("at", at)

    ctt = ct1 + ct2
    print("ctt", ctt)

    # print("Noise budget after addition:", HE.noise_level(ctt))

    print("dct1", HE.decryptBGV(ct1))
    print("dct2", HE.decryptBGV(ct2))
    print("dctt", (HE.decrypt(ctt)))


main()
