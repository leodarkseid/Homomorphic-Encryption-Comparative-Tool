import sys
from Pyfhel import Pyfhel 

def keyGen():
    HE: Pyfhel = Pyfhel()
    context = HE.contextGen(scheme='bfv', n=8192, t_bits=20)
    HE.keyGen()
    # ......................
    HE1: Pyfhel = Pyfhel()
    context1 = HE1.contextGen(scheme='bfv', n=8192, t_bits=20)
    HE1.keyGen()
    # ......................
    HE2: Pyfhel = Pyfhel()
    context2 = HE2.contextGen(scheme='bfv', n=8192, t_bits=20)
    HE2.keyGen()
    # ......................
    HE3: Pyfhel = Pyfhel()
    context3 = HE3.contextGen(scheme='bfv', n=8192, t_bits=20)
    HE3.keyGen()
    # ......................
    HE4: Pyfhel = Pyfhel()
    context4 = HE4.contextGen(scheme='bfv', n=8192, t_bits=20)
    HE4.keyGen()
    # ......................
    HE5: Pyfhel = Pyfhel()
    context5 = HE5.contextGen(scheme='bfv', n=8192, t_bits=20)
    HE5.keyGen()
    # ......................
    HE6: Pyfhel = Pyfhel()
    context6 = HE6.contextGen(scheme='bfv', n=8192, t_bits=20)
    HE6.keyGen()
    # ......................
    HE7: Pyfhel = Pyfhel()
    context7 = HE7.contextGen(scheme='bfv', n=8192, t_bits=20)
    HE7.keyGen()
    # ......................
    HE8: Pyfhel = Pyfhel()
    context8 = HE8.contextGen(scheme='bfv', n=8192, t_bits=20)
    HE8.keyGen()
    # ......................
    HE9: Pyfhel = Pyfhel()
    context9 = HE9.contextGen(scheme='bfv', n=8192, t_bits=20)
    HE9.keyGen()
    # ......................

if __name__ == "__main__":
    keyGen()

