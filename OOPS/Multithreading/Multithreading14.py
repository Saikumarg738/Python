#This Program shows How to Create sub Threads
#SubThreadCreateEx1.py
import threading
def  welcome(sname):
	print("{}--->Hi:{} Wel Come to Multi Threading".format(threading.current_thread().name,sname))

def  hello():
	print("{}--->All of U Read Notes".format(threading.current_thread().name))


#Main Program
print("Program execution Started:{}".format(threading.current_thread().name))
t1=threading.Thread(target=welcome,args=("Rossum",) )
t2=threading.Thread(target=hello)
#Dispatch the sub thread to the target function we use start()
t1.start()
t2.start()
print("Program execution ended:{}".format(threading.current_thread().name))
