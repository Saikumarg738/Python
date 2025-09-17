#Program for Generating 1 to N Number after each and evry second by using threads-Functional Programming
#NumberGenFunEx1.py
import threading,time
def generate(n):
	if(n<=0):
		print("\t{}: {} is Invalid Input".format(threading.current_thread().name,n))
	else:
		print("-"*50)
		print("Numbers within:{}".format(n))
		print("-"*50)
		for i in range(1,n+1):
			print("\t{}: Value of i={}".format(threading.current_thread().name,i))
			time.sleep(0.5)
		else:
			print("-"*50)

#Main Program
n=int(input("Enter How Many Numbers U want to generate:"))
t1=threading.Thread(target=generate,args=(n,))
t1.start()