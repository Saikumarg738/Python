from AtmException import Multipleonly,Insufficient

balance=17849
def withdraw(amount):
    if(amount>balance):
        raise Insufficient
    elif(amount%500!=0):
        raise Multipleonly
