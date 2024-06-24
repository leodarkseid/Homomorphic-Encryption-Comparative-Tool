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
        self.transactionsCount = 0
        self.creditScore = 0
        
     

class Client:
    def __init__(self, id: int, balance: int, desc:str) -> None:
        start_time = time.perf_counter()
        self.client = ClientObject(id=id, balance=balance)
        end_time = time.perf_counter()
        self.initTime = end_time-start_time
        
    def add_creditScore(self, value, desc:str):
        result = self.client.creditScore + value
        self.client.creditScore = min(result, 100)
        return self.client.creditScore

    def genBalance(self):
        num_balances = 10000000
        min_balances = 10000
        max_balances = 1200000000
        balance = random.randint(min_balances, max_balances) 
        return balance