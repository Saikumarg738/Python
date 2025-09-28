class Bankaccount:
    bank_name="Python"
    account_count=0
    def __init__(self,holder_name):
        self.holder_name=holder_name
        Bankaccount.account_count+=1
    @classmethod
    def get_bank_info(cls):
        print(f"Name of bank is {cls.bank_name} and number of account as {cls.account_count}")

Bankaccount("Sai")
Bankaccount("Kumar")
Bankaccount("Gangupamu")
Bankaccount.get_bank_info()