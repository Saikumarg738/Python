from Python.Exception.ATM2Function import deposit, withdraw, balance
from ATM2Exception import *


print("Welcome to ATM")
print("For Deposit, enter 1")
print("For withdraw, enter 2")
print("For balance enquiry, enter 3")

option=int(input("ENter the options : "))

match(option):
    case 1:
        try:
            deposit()
        except DepositError:
            print("Enter appropriate amount")
        except Exception:
            print("Enter proper value")
        finally:
            balance()
    case 2:
        try:
            withdraw()
        except InsufficientFunds:
            print("Account does not have proper funds")
        except Exception:
            print("Emter proper value")
        finally:
            balance()
    case 3:
        balance()



