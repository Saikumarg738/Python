import threading,time

class calculate:
    def square(self,ls):
        for i in ls:
            print("The square of {} is {}".format(i,i**2))
            print("The thread name is ", threading.current_thread().name)
            time.sleep(2)

starttime=time.time()

print("The thread name is ",threading.current_thread())

ls=[1,2,3,4,5,6,7,8,9]

calculate().square(ls)

endtime=time.time()

print("Total execution time is {}".format(endtime-starttime))