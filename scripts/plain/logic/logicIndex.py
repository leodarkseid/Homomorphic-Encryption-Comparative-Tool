

import sys
import os
import time
from typing import TypedDict

from Pyfhel import Pyfhel

from memory.main import Measure
from type.type import AllData, AllData_Type 
from ..client.createMultipleClient import createMultiple
from ..client.index import ClientObject
from rich.console import Console
console = Console()

def addVal(a, b, desc:str):
    time_start = time.perf_counter()
    result = a + b
    time_end = time.perf_counter()
    return {"result":result, "time": time_end-time_start}

def subVal(a, b, desc:str):
    time_start = time.perf_counter()
    result = a - b
    time_end = time.perf_counter()
    return {"result":result, "time": time_end-time_start}

class Logic:
    def __init__(self, client:int, balance:list[int]) -> None:
        with console.status(f'[bold green] Plain Client Initialization', spinner='aesthetic') as status:
            self.listOfClient: list[ClientObject] = createMultiple(numberOfClients=client, balances=balance)

            self.allD = list[AllData_Type]
    
            x = self.listOfClient["result"]
            self.allD = [{
                "id":x[i].client.id, 
                "name":x[i].client.name, 
                "plain_balance":x[i].client.balance, 
                "plain_balance_size":sys.getsizeof(x[i].client.balance), "plain_initialization_time":x[i].client.initTime,
                "plain_client_initialization_ram_cost":self.listOfClient["initData"][i]['mem']
                }
                for i in range(len(self.listOfClient["result"]))]
            # print(self.allD)
            
            
            #id
            #balance


    def creditBalance(self, proposedCreditList:list[int]):
        with console.status(f'[bold green] Processing Plain Credit Balance ', spinner='aesthetic') as status:
            #use the proposef Credit list as the length to update the client, it shoould be the same length as the client i.e self.listOfClient
            for i in range(len(proposedCreditList)):
                m = Measure()
                c = self.listOfClient["result"][i].client
                v = proposedCreditList[i]
                # print({"balanceBefore":c.balance, "credit":v})
                # update balance
                
                
                result = m.measure_memory_time(addVal, c.balance, v, desc='Plain Addition')
                
                c.balance = result["result"]["result"]
                self.allD[i].update({
                    'credit_amount':v,
                    'plain_credit_amount_size':sys.getsizeof(v),
                    'new_plain_balance_after_credit': c.balance,
                    'new_plain_balance_after_credit_size': sys.getsizeof(c.balance), 
                    'time_to_compute_plain_credit':result["time"],
                    'plain_compute_credit_ram_cost': result['memory'],
                    })
                # ['new_plain_balance'] = c.balance
                # print(self.allD)
            
          
        

    def debitBalance(self, proposedDebitList):
        with console.status(f'[bold green] Processing Plain Debit Balance', spinner='aesthetic') as status:
            #use the proposef Credit list as the length to update the client, it shoould be the same length as the client
            for i in range(len(proposedDebitList)):
                m = Measure()
                c = self.listOfClient["result"][i].client
                v = proposedDebitList[i]
                # print({"balanceBefore":c.balance, "credit":v})
                # update balance
                
                result = m.measure_memory_time(subVal, c.balance, v, desc='Plain Substraction')
                
                c.balance = result["result"]["result"]
                self.allD[i].update({
                    "debit_amount":v,
                    'plain_debit_amount_size':sys.getsizeof(v),'new_plain_balance_after_debit': c.balance, 
                    'new_plain_balance_after_debit_size': sys.getsizeof(c.balance),
                    'plain_compute_debit_ram_cost': result['memory'],
                    'time_to_compute_plain_debit':result["time"],

                        })
                # print(self.allD)

    