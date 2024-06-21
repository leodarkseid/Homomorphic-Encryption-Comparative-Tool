import random
import time
from memory.main import Measure
from scripts.plain.logic.logicIndex import Logic as PlainLogic
from scripts.encrypt.logic.logicIndex import Logic as EncryptedLogic
import numpy as np
import pandas as pd
from rich.console import Console

console = Console()

def genBalance(length:int, max:int=300000, min: int=0)->list[int]:
        # num_balances = 10000000
        balances = [random.randint(min, max) for _ in range(int(length))]
        return balances

def init(clients:int):
    # print('Enter Amount of Clients : ')
    # clients = console.input('Enter Amount of Clients : ')
    start_time = time.perf_counter()
    originalBalance = genBalance(clients)
    proposedCreditBalances = genBalance(clients)
    proposedDebitBalances = genBalance(clients)
    Data_CKKS = []
    Data_BGV = []
    Data_BFV = []
    HE_TYPES = ["BGV", "BFV","CKKS"]
    plain = PlainLogic(int(clients), originalBalance)
    # credit
    plain.creditBalance(proposedCreditList=proposedCreditBalances)

    # debit
    plain.debitBalance(proposedDebitList=proposedDebitBalances)
    end_time = time.perf_counter()
    result=''
    plain_PD = pd.DataFrame(plain.allD)
    plain_PD.set_index('id', inplace=True)
    for i in HE_TYPES:
        encrypted = EncryptedLogic(i, int(clients), originalBalance)
        # start encrypt logic

        # credit
        encrypted.creditBalance(proposedCreditList=proposedCreditBalances)

        #debit 
        encrypted.debitBalance(proposedDebitList=proposedDebitBalances)
        
        
        # start plain logic
        attr = f'allD_{i}'
        data = getattr(encrypted, attr, None)
        if data is not None:
            attr = pd.DataFrame(data)
           
            if i == "BGV":
                Data_BGV = pd.merge(plain_PD, attr, on='id')
                Data_BGV.to_excel('data_bgv.xlsx', index=False)
            elif i == "BFV":
                Data_BFV = pd.merge(plain_PD, attr, on='id')
                Data_BFV.to_excel('data_bfv.xlsx', index=False)
            elif i == "CKKS":
                Data_CKKS = pd.merge(plain_PD, attr, on='id')
                Data_CKKS.to_excel('data_ckks.xlsx', index=False)
            
        else:
            print(f"Attribute {attr} not found in encrypted")
    return {"result":result,"time":end_time-start_time }

if __name__ == "__main__":
    clients = console.input('Enter Amount of Clients : ')
    with console.status("[bold green]Computing...") as status:
        init(clients=clients)
    console.log(f'[bold][blue]Done Computing, Excel Files have been saved!')