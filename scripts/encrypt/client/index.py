from enum import Enum
import random
import time
from Pyfhel import Pyfhel
from typing import Literal
import numpy as np

class He_type(Enum):
    BGV= 'BGV'
class ClientObject:
    def __init__(self, id: int,  balance: any, HE: Pyfhel, name: str = '') -> None:
        self.id = id
        self.name = name
        self.balance = balance
        self.HE = HE
        start_time = time.perf_counter()
        end_time = time.perf_counter()
        self.initTime = end_time-start_time

class Client:
    def __init__(self, id:int, balance:int, he_type: Literal["BGV", "BFV", "CKKS"], desc:str) -> None:
        start_time = time.perf_counter()
        HE = Pyfhel()
        self.client: ClientObject = ClientObject(id=0, balance={}, HE={})
       
        if he_type == "BGV":
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
            bal = np.array([balance], dtype=np.int64)
        
            # self.pain = 1
            balanceCipherText = HE.encryptBGV(bal)
            self.client = ClientObject(id=id, balance=balanceCipherText, HE=HE)
            end_time = time.perf_counter()
            self.initTime = end_time-start_time
        elif he_type == 'BFV':
            bfv_params = {
                'scheme': 'BFV',
                'n': 2**13,
                't':65537,
                't_bits':20,
                'sec':128
            }
            bal = np.array([balance], dtype=np.int64)
            HE.contextGen(**bfv_params) 
            HE.keyGen()
            HE.rotateKeyGen()
            HE.relinKeyGen()
            encodedBalance = HE.encode(bal)
            cipherBalance = HE.encryptPtxt(encodedBalance)
            self.client = ClientObject(id=id, balance=cipherBalance, HE=HE)
            end_time = time.perf_counter()
            self.initTime = end_time-start_time
        elif he_type == "CKKS":
            ckks_params = {
                'scheme':'ckks',
                'n':8192, 
                'scale':2**30, 
                'qi_sizes':[60, 30, 30, 30, 60]
                }
            HE.contextGen(**ckks_params)
            HE.keyGen()
            HE.rotateKeyGen()
            bal = np.array([balance], dtype=np.float64)
            encodedBalance = HE.encodeFrac(bal)
            cipherBalance = HE.encryptPtxt(encodedBalance)
            self.client = ClientObject(id=id, balance=cipherBalance, HE=HE)
            end_time = time.perf_counter()
            self.initTime = end_time-start_time

    

    @property
    def balance(self):
        return self.client.balance

    @property
    def he(self) -> Pyfhel:
        return self.client.HE
    
    @property
    def id(self):
        return self.client.id

    def genBalance(self):
        num_balances = 10000000
        min_balances = 10000
        max_balances = 1200000000
        balance = random.randint(min_balances, max_balances) 
        return balance