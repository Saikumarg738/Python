#Program for Generating 1 to N Number after each and evry second by using threads-Functional Programming
#EvenOddNumberGenOopEx2.py
import threading,time
class Numbers:
	def oddgenerate(self,n):
		if(n<=0):
			print("\t{}: {} is Invalid Input".format(threading.current_thread().name,n))
		else:
			for i in range(1,n+1,2):
				print("\t{}: Odd Value={}".format(threading.current_thread().name,i))
				time.sleep(0.5)
	def evengenerate(self,n):
		if(n<=0):
			print("\t{}: {} is Invalid Input".format(threading.current_thread().name,n))
		else:
			for i in range(2,n+1,2):
				print("\t{}: Even Value={}".format(threading.current_thread().name,i))
				time.sleep(0.5)

#Main Program
on=int(input("Enter How Many Odd Numbers U want to generate:"))
en=int(input("Enter How Many Even Numbers U want to generate:"))
t1=threading.Thread(target=Numbers().oddgenerate,args=(on,))
t2=threading.Thread(target=Numbers().evengenerate,args=(en,))
t1.start()
t2.start()