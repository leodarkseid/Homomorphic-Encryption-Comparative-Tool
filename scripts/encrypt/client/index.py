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
                    't_bits': 54,
                    'sec': 256,
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
            self.client.creditScore = HE.encryptBGV(np.array([0], dtype=np.int64))
            self.client.transactionsCount = HE.encryptBGV(np.array([0], dtype=np.int64))
        elif he_type == 'BFV':
            bfv_params = {
                'scheme': 'BFV',
                'n': 2**13,
                't':65537,
                't_bits':54,
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
            self.client.creditScore = HE.encryptPtxt(HE.encode(np.array([0], dtype=np.int64)))
            self.client.transactionsCount = HE.encryptPtxt(HE.encode(np.array([0], dtype=np.int64)))
        elif he_type == "CKKS":
            ckks_params = {
                'scheme':'ckks',
                'n':2**13, 
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
            self.client.creditScore = HE.encryptPtxt(HE.encodeFrac(np.array([0], dtype=np.float64)))
            self.client.transactionsCount = HE.encryptPtxt(HE.encodeFrac(np.array([0], dtype=np.float64)))

    def add_creditScore(self, value,HE, desc:str):
    
        result = self.client.creditScore + value
        d100 = HE.encrypt(HE.encode(np.array([100])))
        if self.greaterThan(result, d100, HE, "add_CreditScore"):
            self.client.creditScore = d100
        else:
            self.client.creditScore = result
        # self.client.creditScore = min(result, d100)
        return {'result':self.client.creditScore, "time":0}

    def greaterThan(self, x , y, HE, desc:str):
        result = x - y
        numba = HE.decrypt(HE.decode(result))
        return numba > 0

    def genBalance(self):
        num_balances = 10000000
        min_balances = 10000
        max_balances = 1200000000
        balance = random.randint(min_balances, max_balances) 
        return balance