import random
import time

from type.type import ResultDict


class ClientObject:
    def __init__(self, id: int,  balance: int, name: str = '') -> None:
        start_time = time.perf_counter()
        self.id = id
        self.name = name
        self.balance = balance
        end_time = time.perf_counter()
        self.initTime = end_time-start_time
        
     

class Client:
    def __init__(self, id: int, balance: int, desc:str) -> None:
        start_time = time.perf_counter()
        self.client = ClientObject(id=id, balance=balance)
        end_time = time.perf_counter()
        self.initTime = end_time-start_time
        
      

    @property
    def balance(self):
        return self.client.balance

    @property
    def id(self):
        return self.client.id

    def genBalance(self):
        num_balances = 10000000
        min_balances = 10000
        max_balances = 1200000000
        balance = random.randint(min_balances, max_balances) 
        return balance