import random
import os
import sys
import time
from typing import Dict, TypedDict
from Pyfhel import Pyfhel

from memory.main import Measure

from .index import Client, ClientObject, He_type

class InitData(TypedDict):
     id: int
     time: float
     mem: float

class CreateMultipleResultDict(TypedDict):
     result: list[ClientObject]
     time:float
     memory: int
     initData: list[InitData]

def createMultiple(he_type:list[He_type], balances:list[int],numberOfClients:int = 1) -> Dict[CreateMultipleResultDict, any]:
    initTotalTimer = 0
    initTotalMemory = 0
    start_time = time.perf_counter()
    clientsInstance: list[ClientObject] = []
    initDATA: list[InitData] = []
    
    for i in range(numberOfClients):
        profiler = Measure()
        c = profiler.measure_memory_time(Client, id=i+1, balance=balances[i], he_type=he_type, desc='Client Initialization')
        client = c["result"]
        clientsInstance.append(client)
        initD = {"id":client.client.id, "time":client.initTime, "mem":c["memory"]}
        initDATA.append(initD)
        initTotalTimer += client.initTime
        initTotalMemory += c["memory"]
    end_time = time.perf_counter()
    result = {"result":clientsInstance, "time":end_time-start_time, "memory":initTotalMemory, "initData":initDATA}
    return result
    # [print({"client_id": client.id, "client_balance": client.balance, "client_he": client.client.HE}) for client in clientsInstance]
    # return clientsInstance

    # for i in range(len(clientInstance)):
    #     client = clientInstance[i]
    #     print(client.sizeof_public_key())
# def genBalance():
#         # num_balances = 10000000
#         min_balances = 10000
#         max_balances = 1200000000
#         balance = random.randint(min_balances, max_balances)
         
#         return balance

if __name__ == "__main__":
    createMultiple()