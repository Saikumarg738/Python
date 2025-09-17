import threading,time

def square(sai):
    for i in sai:
        print("The square of {} is {}, it is executing in {}".format(i,i**2,threading.current_thread().name))
        time.sleep(1)

def cube(teja):
    for i in teja:
        print("The cube of {} is {}, it is executing in {}".format(i, i**3,threading.current_thread().name))
        time.sleep(1)


starttime=time.time()
print("Execution started by main program in thread",threading.current_thread().name)
nums=[1,2,3,4,5,6,7,8]
t1=threading.Thread(target=square,args=(nums,))
t2=threading.Thread(target=cube,args=(nums,))
t1.start()
t2.start()
t1.join()
t2.join()
endtime=time.time()
print("Execution ended")
print("Execution time is ",endtime-starttime)