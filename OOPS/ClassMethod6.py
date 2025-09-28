class Bankaccount:
    bank_name="Python"
    account_count=0
    @classmethod
    def edit(cls,holder_name):
        cls.holder_name=holder_name
        Bankaccount.account_count+=1
    @classmethod
    def get_bank_info(cls):
        print(f"Name of bank is {cls.bank_name} and number of account as {cls.account_count}")

Bankaccount.edit("Sai")
Bankaccount.edit("Kumar")
Bankaccount.get_bank_info()