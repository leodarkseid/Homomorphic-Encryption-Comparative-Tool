import random
import time
from distributedRandom import DistributedRandom
from memory.main import Measure
from scripts.plain.logic.logicIndex import Logic as PlainLogic
from scripts.encrypt.logic.logicIndex import Logic as EncryptedLogic
import numpy as np
import pandas as pd
from rich.console import Console

console = Console()

# def genBalance(length:int, max:int=30000000000, min: int=0)->list[int]:
#         # num_balances = 10000000
#         balances = [random.randint(min, max) for _ in range(int(length))]
#         return balances
def genB(length:int, min_amount=-100000, max_amount=500000000000, distribution=7834333):
    genBalance = DistributedRandom(client=int(length), min_amount=min_amount, max_amount=max_amount, distribution=distribution)
    balances = [genBalance.next() for _ in range(int(length))]
    return balances

def init(clients:int):
    # print('Enter Amount of Clients : ')
    # clients = console.input('Enter Amount of Clients : ')
    start_time = time.perf_counter()
    originalBalance = genB(clients)
    proposedCreditBalances = genB(clients)
    proposedDebitBalances = genB(clients)
    creditScores = genB(length=int(clients), min_amount=5, max_amount=30, distribution=1)
    txVals = genB(length=int(clients), min_amount=1, max_amount=12, distribution=1)
    # print("ob", originalBalance)
    # print("pcb", proposedCreditBalances)
    # print("pdb", proposedDebitBalances)
    # print("cds", creditScores)

    Data_CKKS = []
    Data_BGV = []
    Data_BFV = []
    HE_TYPES = ["BGV", "BFV","CKKS"]
    plain = PlainLogic(int(clients), originalBalance)

    # set credit_score
    plain.set_credit_score(creditScores)
    plain.update_transaction_count(txVals)
    # credit
    # plain.creditBalance(proposedCreditList=proposedCreditBalances)

    # # debit
    # plain.debitBalance(proposedDebitList=proposedDebitBalances)
    result=''
    plain_PD = pd.DataFrame(plain.allD)
    plain_PD.set_index('id', inplace=True)
    for i in HE_TYPES:
        encrypted = EncryptedLogic(i, int(clients), originalBalance)
        # start encrypt logic
        # set credit_score
        encrypted.set_credit_score(creditScores)
        encrypted.update_transaction_count(txVals)
        # credit
        # encrypted.creditBalance(proposedCreditList=proposedCreditBalances)

        # #debit 
        # encrypted.debitBalance(proposedDebitList=proposedDebitBalances)
        
        
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
    end_time = time.perf_counter()
    return {"result":result,"time":end_time-start_time }

if __name__ == "__main__":
    clients = console.input('Enter Amount of Clients : ')
    with console.status("[bold green]Computing...") as status:
        x = init(clients=clients)
        console.log("time", x["time"])
    console.log(f'[bold][blue]Done Computing, Excel Files have been saved!')