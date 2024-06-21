from typing import TypedDict

class ResultDict(TypedDict):
    result: any
    time: float
    memory: int

class AllData_Type(TypedDict):
    id:int
    name: str
    plain_balance : int
    plain_balance_size : float
    plain_initialization_time : float
    encrypted_initialization_time :float
    encrypted_balance_size : float
    HE_size : float
    credit_amount: int
    debit_amount: int
    plain_credit_amount_size: float
    plain_debit_amount_size: float
    enc_credit_amount_size: float
    enc_debit_amount_size: float
    time_to_encrypt_credit: float
    time_to_encrypt_debit: float
    time_to_compute_plain_credit: float
    time_to_compute_plain_debit: float
    time_to_compute_enc_credit: float
    time_to_compute_enc_debit: float
    enc_credit_ram_cost: float
    enc_debit_ram_cost: float
    new_plain_balance_after_credit: int
    new_plain_balance_after_credit_size: float
    new_plain_balance_after_debit: int
    new_plain_balance_after_debit_size: float
    new_enc_balance_after_credit_size: float
    new_enc_balance_after_debit_size: float
    time_to_decrypt_new_enc_balance_size: float
    enc_client_initialization_ram_cost: float
    client_initialization_ram_cost: float
    plain_compute_credit_ram_cost:float
    enc_compute_credit_ram_cost:float
    plain_compute_debit_ram_cost:float
    enc_compute_debit_ram_cost:float

class AllData:
    def __init__(self) -> None:
        self.id=0
        self.plain_balance=0
        self.plain_balance_size = 0
        self.encrypted_balance_size = 0
        self.HE_size = 0
        self.encryption_initialization_time = 0
        self.plain_initialization_time = 0
        self.credit_amount = 0
        self.debit_amount = 0
        self.plain_credit_bal_size = 0
        self.plain_debit_bal_size = 0
        self.enc_credit_bal_size = 0
        self.enc_debit_bal_size = 0
        self.time_to_encrypt_credit = 0
        self.time_to_encrypt_debit = 0
        self.time_to_compute_addition = 0
        self.time_to_compute_substraction = 0
        self.new_plain_balance = 0
        self.new_plain_balance_size = 0
        self.new_enc_balance_size = 0
        self.time_to_decrypt_new_enc_balance_size = 0

    def result(self) -> AllData_Type:
        return self.__dict__
    