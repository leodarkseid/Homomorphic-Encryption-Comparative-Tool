import sys
from Pyfhel import Pyfhel 

def keyGen():
    HE: Pyfhel = Pyfhel()
    context = HE.contextGen(scheme='bfv', n=8192, t_bits=20, sec=128)
    HE.keyGen()
    size = HE.to_bytes_public_key(compr_mode = "zstd")

    HE1: Pyfhel = Pyfhel()
    context = HE1.contextGen(scheme='bfv', n=8192, t_bits=20, sec=128)
    HE1.keyGen()
    size1 = HE1.to_bytes_public_key(compr_mode = "zstd")

    HE2: Pyfhel = Pyfhel()
    context = HE2.contextGen(scheme='bfv', n=8192, t_bits=20, sec=128)
    HE2.keyGen()
    size2 = HE2.to_bytes_public_key(compr_mode = "zstd")

    HE3: Pyfhel = Pyfhel()
    context = HE3.contextGen(scheme='bfv', n=8192, t_bits=20, sec=128)
    HE3.keyGen()
    size3 = HE3.to_bytes_public_key(compr_mode = "zstd")

    HE4: Pyfhel = Pyfhel()
    context = HE4.contextGen(scheme='bfv', n=8192, t_bits=20, sec=128)
    HE4.keyGen()
    size4 = HE4.to_bytes_public_key(compr_mode = "zstd")

    HE5: Pyfhel = Pyfhel()
    context = HE5.contextGen(scheme='bfv', n=8192, t_bits=20, sec=128)
    HE5.keyGen()
    size5 = HE5.to_bytes_public_key(compr_mode = "zstd")

    HE6: Pyfhel = Pyfhel()
    context = HE6.contextGen(scheme='bfv', n=8192, t_bits=20, sec=128)
    HE6.keyGen()
    size6 = HE6.to_bytes_public_key(compr_mode = "zstd")

    HE7: Pyfhel = Pyfhel()
    context = HE7.contextGen(scheme='bfv', n=8192, t_bits=20, sec=128)
    HE7.keyGen()
    size7 = HE7.to_bytes_public_key(compr_mode = "zstd")

    HE8: Pyfhel = Pyfhel()
    context = HE8.contextGen(scheme='bfv', n=8192, t_bits=20, sec=128)
    HE8.keyGen()
    size8 = HE8.to_bytes_public_key(compr_mode = "zstd")

    HE9: Pyfhel = Pyfhel()
    context = HE9.contextGen(scheme='bfv', n=8192, t_bits=20, sec=128)
    HE9.keyGen()
    size9 = HE9.to_bytes_public_key(compr_mode = "zstd")


if __name__ == "__main__":
    keyGen() 