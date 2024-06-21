import sys
from Pyfhel import Pyfhel 

def keyGen():
    HE: Pyfhel = Pyfhel()
    ckks_params = {'scheme':'ckks','n':8192, 'scale':2**30, 'qi_sizes':[60, 30, 30, 30, 60]}
    context = HE.contextGen(**ckks_params)
    HE.keyGen()
    # .................................
    HE1: Pyfhel = Pyfhel()
    ckks_params1 = {'scheme':'ckks','n':8192, 'scale':2**30, 'qi_sizes':[60, 30, 30, 30, 60]}
    context1 = HE1.contextGen(**ckks_params)
    HE1.keyGen()
    # .................................
    HE2: Pyfhel = Pyfhel()
    ckks_params2 = {'scheme':'ckks','n':8192, 'scale':2**30, 'qi_sizes':[60, 30, 30, 30, 60]}
    context2 = HE2.contextGen(**ckks_params)
    HE2.keyGen()
    # .................................
    HE3: Pyfhel = Pyfhel()
    ckks_params3 = {'scheme':'ckks','n':8192, 'scale':2**30, 'qi_sizes':[60, 30, 30, 30, 60]}
    context3 = HE3.contextGen(**ckks_params)
    HE3.keyGen()
    # .................................
    HE4: Pyfhel = Pyfhel()
    ckks_params4 = {'scheme':'ckks','n':8192, 'scale':2**30, 'qi_sizes':[60, 30, 30, 30, 60]}
    context4 = HE4.contextGen(**ckks_params)
    HE4.keyGen()
    # .................................
    HE5: Pyfhel = Pyfhel()
    ckks_params5 = {'scheme':'ckks','n':8192, 'scale':2**30, 'qi_sizes':[60, 30, 30, 30, 60]}
    context5 = HE5.contextGen(**ckks_params)
    HE5.keyGen()
    # .................................
    HE6: Pyfhel = Pyfhel()
    ckks_params6 = {'scheme':'ckks','n':8192, 'scale':2**30, 'qi_sizes':[60, 30, 30, 30, 60]}
    context6 = HE6.contextGen(**ckks_params)
    HE6.keyGen()
    # .................................
    HE7: Pyfhel = Pyfhel()
    ckks_params7 = {'scheme':'ckks','n':8192, 'scale':2**30, 'qi_sizes':[60, 30, 30, 30, 60]}
    context7 = HE7.contextGen(**ckks_params)
    HE7.keyGen()
    # .................................
    HE8: Pyfhel = Pyfhel()
    ckks_params8 = {'scheme':'ckks','n':8192, 'scale':2**30, 'qi_sizes':[60, 30, 30, 30, 60]}
    context8 = HE8.contextGen(**ckks_params)
    HE8.keyGen()
    # .................................
    HE9: Pyfhel = Pyfhel()
    ckks_params9 = {'scheme':'ckks','n':8192, 'scale':2**30, 'qi_sizes':[60, 30, 30, 30, 60]}
    context9 = HE9.contextGen(**ckks_params)
    HE9.keyGen()
    # .................................

if __name__ == "__main__":
    keyGen()
