from AtmFunction import *

try:
    am=int(input("Enter amount to withdraw"))
    withdraw(am)
except Insufficient:
    print("You do not have sufficient balance")
except Multipleonly:
    print("Please enter multiples of 500 note only")
else:
    print("Withdrawing amount {}".format(am))
finally:
    print("Thank you for visiting")