

import sys
import os
import time
from typing import Literal
from Pyfhel import Pyfhel
from rich.console import Console

console = Console()

from memory.main import Measure
from type.type import AllData_Type 
from ..client.createMultipleClient import createMultiple
from ..client.index import ClientObject
import numpy as np


def addVal(a, b, desc='Encryption Addition'):
    time_start = time.perf_counter()
    result = a + b
    time_end = time.perf_counter()
    return {"result":result, "time": time_end-time_start}

def subVal(a, b,  desc='Encryption Substraction'):
    time_start = time.perf_counter()
    result = a - b
    time_end = time.perf_counter()
    return {"result":result, "time": time_end-time_start}


class Logic:
    m = Measure()
    def __init__(self, he_type: Literal["BGV", "BFV", "CKKS"], clients:int, balances:list[int]) -> None:
        with console.status(f'[bold green] Encrypted Client Initialization', spinner='aesthetic') as status:
            self.allD_BGV = list[AllData_Type]
            self.allD_BFV = list[AllData_Type]
            self.allD_CKKS = list[AllData_Type]
            self.he_type:Literal["BGV", "BFV", "CKKS"] = he_type
            self.listOfClient: list[ClientObject] = createMultiple(he_type=he_type,numberOfClients=clients, balances=balances)
            x = self.listOfClient["result"]
            if he_type == 'BFV':
                self.allD_BFV = [{
                    "id":x[i].client.id, 
                    "name":x[i].client.name,
                    "enc_client_initialization_ram_cost":self.listOfClient["initData"][i]["mem"],
                    "encrypted_balance_size": x[i].client.balance.sizeof_ciphertext(),
                    "encrypted_initialization_time":x[i].client.initTime,
                    "enc_client_size":sys.getsizeof(x[i].client),
                    "HE_size": x[i].client.HE.sizeof_context()
                }for i in range(len(self.listOfClient["result"]))]
            elif he_type == 'BGV':
                self.allD_BGV = [{
                    "id":x[i].client.id, 
                    "name":x[i].client.name,
                    "enc_client_initialization_ram_cost":self.listOfClient["initData"][i]["mem"],
                    "encrypted_balance_size": x[i].client.balance.sizeof_ciphertext(),
                    "encrypted_initialization_time":x[i].client.initTime,
                    "enc_client_size":sys.getsizeof(x[i].client),
                    "HE_size": x[i].client.HE.sizeof_context()
                }for i in range(len(self.listOfClient["result"]))]
            elif he_type == 'CKKS':
                self.allD_CKKS = [{
                    "id":x[i].client.id, 
                    "name":x[i].client.name,
                    "enc_client_initialization_ram_cost":self.listOfClient["initData"][i]["mem"],
                    "encrypted_balance_size": x[i].client.balance.sizeof_ciphertext(),
                    "encrypted_initialization_time":x[i].client.initTime,
                    "enc_client_size":sys.getsizeof(x[i].client),
                    "HE_size": x[i].client.HE.sizeof_context()
                }for i in range(len(self.listOfClient["result"]))]



    def creditBalance(self, proposedCreditList):
        with console.status(f'[bold green] Processing Encrypted Credit Balance', spinner='aesthetic') as status:
            for i in range(len(proposedCreditList)):
                m = Measure()
                # initialize the long client list as c to make it shsorter
                c = self.listOfClient["result"][i].client
                v = proposedCreditList[i]
                # this is supposed to encrypt the value to be added
                encryptedProposedCredit = m.measure_memory_time(self.encryptInt, he_type=self.he_type, HE=c.HE, value=v, desc='Credit Amount Encryption')

            
                # result = c.balance + encryptedProposedCredit['result']
                result = m.measure_memory_time(addVal, c.balance, encryptedProposedCredit['result'], desc='Encryption Addition')
            
                c.balance = result["result"]["result"]
                if self.he_type == "BFV":
                    self.allD_BFV[i].update({
                        'enc_credit_amount_size':encryptedProposedCredit["result"].sizeof_ciphertext(),
                        'new_enc_balance_after_credit_size':result["result"]["result"].sizeof_ciphertext(),
                        'time_to_compute_enc_credit':result['time'],
                        'enc_credit_ram_cost':encryptedProposedCredit["memory"],
                        'time_to_encrypt_credit':encryptedProposedCredit['time'],
                        'enc_compute_credit_ram_cost':result['memory']
                    })
                elif self.he_type == "BGV":
                    self.allD_BGV[i].update({
                        'enc_credit_amount_size':encryptedProposedCredit["result"].sizeof_ciphertext(),
                        'new_enc_balance_after_credit_size':c.balance.sizeof_ciphertext(),
                        'time_to_compute_enc_credit':result['time'],
                        'enc_credit_ram_cost':encryptedProposedCredit["memory"],
                        'time_to_encrypt_credit':encryptedProposedCredit['time'],
                        'enc_compute_credit_ram_cost':result['memory']
                    })
                elif self.he_type == "CKKS":
                    self.allD_CKKS[i].update({
                        'enc_credit_amount_size':encryptedProposedCredit["result"].sizeof_ciphertext(),
                        'new_enc_balance_after_credit_size':c.balance.sizeof_ciphertext(),
                        'time_to_compute_enc_credit':result['time'],
                        'enc_credit_ram_cost':encryptedProposedCredit["memory"],
                        'time_to_encrypt_credit':encryptedProposedCredit['time'],
                        'enc_compute_credit_ram_cost':result['memory']
                    })
            

    def debitBalance(self, proposedDebitList):
        with console.status(f'[bold green] Processing Encrypted Debit Balance', spinner='aesthetic') as status:
            for i in range(len(proposedDebitList)):
                m = Measure()
                # initialize the long client list as c to make it shsorter
                c = self.listOfClient["result"][i].client
                v = proposedDebitList[i]
                # this is supposed to encrypt the value to be added
                encryptedProposedDebit = m.measure_memory_time(self.encryptInt, he_type=self.he_type, HE=c.HE, value=v, desc='Debit Amount Encryption')

            
                # result = c.balance + encryptedProposedDebit['result']
                result = m.measure_memory_time(subVal, a=c.balance, b=encryptedProposedDebit['result'], desc='Encryption Substraction')
            
                c.balance = result["result"]["result"]
                if self.he_type == "BFV":
                    self.allD_BFV[i].update({
                        'enc_debit_amount_size':encryptedProposedDebit["result"].sizeof_ciphertext(),
                        'new_enc_balance_after_debit_size':result["result"]["result"].sizeof_ciphertext(),
                        'time_to_compute_enc_debit':result['time'],
                        'enc_debit_ram_cost':encryptedProposedDebit["memory"],
                        'time_to_encrypt_debit':encryptedProposedDebit['time'],
                        'enc_compute_debit_ram_cost':result['memory']
                    })
                elif self.he_type == "BGV":
                    self.allD_BGV[i].update({
                        'enc_debit_amount_size':encryptedProposedDebit["result"].sizeof_ciphertext(),
                        'new_enc_balance_after_debit_size':result["result"]["result"].sizeof_ciphertext(),
                        'time_to_compute_enc_debit':result['time'],
                        'enc_debit_ram_cost':encryptedProposedDebit["memory"],
                        'time_to_encrypt_debit':encryptedProposedDebit['time'],
                        'enc_compute_debit_ram_cost':result['memory']
                    })
                elif self.he_type == "CKKS":
                    self.allD_CKKS[i].update({
                        'enc_debit_amount_size':encryptedProposedDebit["result"].sizeof_ciphertext(),
                        'new_enc_balance_after_debit_size':result["result"]["result"].sizeof_ciphertext(),
                        'time_to_compute_enc_debit':result['time'],
                        'enc_debit_ram_cost':encryptedProposedDebit["memory"],
                        'time_to_encrypt_debit':encryptedProposedDebit['time'],
                        'enc_compute_debit_ram_cost':result['memory']
                    })

    def encryptInt(self, he_type: Literal["BGV", "BFV", "CKKS"], HE: Pyfhel, value:int, desc:str):
       
        if he_type == "BGV":
            msgArray = np.array([value], dtype=np.int64)
            
            encryptedProposedCredit = HE.encryptBGV(msgArray)
            return encryptedProposedCredit
        elif he_type == "BFV":
            msgArray = np.array([value], dtype=np.int64)
            plainTxt = HE.encodeInt(msgArray) 
            encryptedProposedCredit = HE.encryptPtxt(plainTxt)
            return encryptedProposedCredit
        elif he_type == "CKKS":
             msgArray = np.array([value], dtype=np.float64)
             plainTxt = HE.encodeFrac(msgArray)
             encryptedProposedCredit = HE.encryptPtxt(plainTxt)
             return encryptedProposedCredit


    def decrypt(self, he_type: Literal["BGV", "BFV", "CKKS"], HE: Pyfhel, value:any, desc:str):
        if he_type == "BFV":
            decryptedPlainTxt = HE.decryptInt(value)
            # decrypted = HE.decodeInt(decryptedPlainTxt)
            return decryptedPlainTxt
        elif he_type == "BGV":
            decrypted = HE.decryptBGV(value)
            return decrypted
        elif he_type == "CKKS":
            decryptedPlainTxt = HE.decryptFrac(value)
            # decrypted = HE.decodeFrac(decryptedPlainTxt)
            return decryptedPlainTxt
        
    def set_credit_score(self, value):
        for i in range(len(value)):
            m = Measure()
            c = self.listOfClient["result"][i]
            v = c.client.HE.encrypt(value[i])
            result = m.measure_memory_time(self.add_creditScore, value =v,HE=c.client.HE,client=c, desc="set enc credit score")
            # if self.he_type == "BFV":
            #     result = m.measure_memory_time(self.add_creditScore, v,c.client.HE, desc="set enc credit score")
            # elif self.he_type == "BGV":
            #     result = m.measure_memory_time(self.add_creditScore, value=v,HE=c.client.HE, desc="set enc credit score")
            # elif self.he_type == "CKKS":
            #     result = m.measure_memory_time(self.add_creditScore, v,c.client.HE, desc="set enc credit score")
            
            if self.he_type == "BFV":
                self.allD_BFV[i].update({
                "enc_credit_score_size":sys.getsizeof(v),
                "enc_credit_score_computation_ram_cost":result["memory"],
                "enc_credit_score_computation_time":result["time"],
            })
            elif self.he_type == "BGV":
                self.allD_BGV[i].update({
                "enc_credit_score_size":sys.getsizeof(v),
                "enc_credit_score_computation_ram_cost":result["memory"],
                "enc_credit_score_computation_time":result["time"],
            })
            elif self.he_type == "CKKS":
                self.allD_CKKS[i].update({
                    "enc_credit_score_size":sys.getsizeof(v),
                    "enc_credit_score_computation_ram_cost":result["memory"],
                    "enc_credit_score_computation_time":result["time"],
                })

        return result
        
    def add_creditScore(self, value,HE,client, desc:str):
        
        result = client.client.creditScore + value
        d100 = HE.encrypt(HE.encode(np.array([100])))
        if self.greaterThan(x=result, y=d100, HE=HE, desc="add_CreditScore"):
            client.client.creditScore = d100
        else:
            client.client.creditScore = result
        # self.client.creditScore = min(result, d100)
        return client.client.creditScore

    def greaterThan(self, x , y, HE, desc:str):
        result = x - y
        numba = HE.decrypt(result)
        return numba.all() > 0

    def update_transaction_count(self, value):
        m = Measure()
        for i in range(len(value)):
            c = self.listOfClient["result"][i].client 
            v = c.HE.encrypt(c.HE.encode(np.array([value[i]])))
            y = c.transactionsCount
            result = m.measure_memory_time(addVal, a=v,b=y,  desc="transaction count update")
            c.transactionsCount = result["result"]["result"]
            if self.he_type == "BFV":
                self.allD_BFV[i].update({
                "enc_transaction_count_size":sys.getsizeof(v),
                "enc_transaction_count_computation_ram_cost":result["memory"],
                "enc_transaction_count_computation_time":result["time"],
            })
            elif self.he_type == "BGV":
                self.allD_BGV[i].update({
                "enc_transaction_count_size":sys.getsizeof(v),
                "enc_transaction_count_computation_ram_cost":result["memory"],
                "enc_transaction_count_computation_time":result["time"],
            })
            elif self.he_type == "CKKS":
                self.allD_CKKS[i].update({
                "enc_transaction_count_size":sys.getsizeof(v),
                "enc_transaction_count_computation_ram_cost":result["memory"],
                "enc_transaction_count_computation_time":result["time"],
                })

    
            