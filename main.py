import time
from rich.console import Console
import pandas as pd
from distributedRandom import DistributedRandom
from scripts.plain.logic.logicIndex import Logic as PlainLogic
from scripts.encrypt.logic.logicIndex import Logic as EncryptedLogic

console = Console()


def generate_balance(length: int, min_amount=-100000,
                     max_amount=500000000000,
                     distribution=7834333):
    """Generate a list of balances using a distributed random generator."""
    balance_generator = DistributedRandom(client=int(length), min_amount=min_amount,
                                          max_amount=max_amount, distribution=distribution)
    return [balance_generator.next() for _ in range(int(length))]


def initialize_clients(clients: int):
    """Initialize client balances and perform operations using both plain and encrypted logic."""
    start_time = time.perf_counter()
    originalBalance = generate_balance(clients)
    proposedCreditBalances = generate_balance(clients)
    proposedDebitBalances = generate_balance(clients)
    creditScores = generate_balance(length=int(clients),
                                    min_amount=5,
                                    max_amount=30,
                                    distribution=1)
    txVals = generate_balance(length=int(clients), min_amount=1, max_amount=12, distribution=1)

    he_types = ["BGV", "BFV", "CKKS"]

    # Data_All = plain_PD
    for he_type in he_types:
        encrypted_logic = EncryptedLogic(he_type, int(clients), originalBalance)
        encrypted_logic.set_credit_score(creditScores)
        encrypted_logic.update_transaction_count(txVals)
        encrypted_logic.creditBalance(proposedCreditList=proposedCreditBalances)
        encrypted_logic.debitBalance(proposedDebitList=proposedDebitBalances)

    # Process with plain logic
    plain_logic = PlainLogic(int(clients), originalBalance)
    plain_logic.set_credit_score(creditScores)
    plain_logic.update_transaction_count(txVals)
    plain_logic.creditBalance(proposedCreditList=proposedCreditBalances)
    plain_logic.debitBalance(proposedDebitList=proposedDebitBalances)

    # Save the plain logic data to an Excel file
    plain_df = pd.DataFrame(plain_logic.allD)
    plain_df.set_index('id', inplace=True)
    plain_df.to_excel('all.xlsx', index=False)

    end_time = time.perf_counter()
    return {"time": end_time - start_time}


if __name__ == "__main__":
    clients = int(console.input('Enter number of clients : '))
    with console.status("[bold green]Computing...") as status:
        x = initialize_clients(clients=clients)
        console.log("time", x["time"])
    console.log('[bold][blue]Done Computing, Excel File has been saved!')
