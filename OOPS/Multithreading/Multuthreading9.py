#Program for Generating 1 to N Number after each and evry second by using threads-Functional Programming
#EvenOddNumberGenOopEx1.py
import threading,time

class odd:
    def oddnum(self,n,lockobj):
        with lockobj:
            if(n<=0):
                print(f"{n} is not greater than 0, so aborting the operation")
            else:
                for i in range(1,n+1,2):
                    print(f"Odd number is {i} {threading.current_thread().name}")
                    time.sleep(1)
class even:
    def evennum(self,n,lockobj):
        with lockobj:
            if(n<=0):
                print(f"{n} is not greater than 0, so aborting the operation")
            else:
                for i in range(2,n+1,2):
                    print(f"Even number is {i} {threading.current_thread().name}")
                    time.sleep(1)
lockobj=threading.Lock()
a=int(input("Enter the range of number you want odd number in"))
b=int(input("Enter the range of number you want even number in"))
oddobj=threading.Thread(target=odd().oddnum,args=(a,lockobj))
evenobj=threading.Thread(target=even().evennum,args=(b,lockobj))

oddobj.start()
evenobj.start()