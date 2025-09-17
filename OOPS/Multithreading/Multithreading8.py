import threading,time

def square(sai,lockobj):
    for i in sai:
        with lockobj:
            print(f"The square of {i} is {i**2}, it is executing in {threading.current_thread().name}")
        time.sleep(1)

def cube(teja,lockobj):
    for i in teja:
        with lockobj:
            print("The cube of {} is {}, it is executing in {}".format(i, i**3,threading.current_thread().name))
        time.sleep(1)


starttime=time.time()
print("Execution started by main program in thread",threading.current_thread().name)
nums=[1,2,3,4,5,6,7,8]
lockobj=threading.Lock()
t1=threading.Thread(target=square,args=(nums,lockobj))
t2=threading.Thread(target=cube,args=(nums,lockobj))
t1.start()
t2.start()
t1.join()
t2.join()
endtime=time.time()
print("Execution ended")
print("Execution time is ",endtime-starttime)