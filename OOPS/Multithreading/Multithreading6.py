import threading

def first():
    print("First method is executed by {}".format(threading.current_thread().name))

def second():
    print("Second method is executed by {}".format(threading.current_thread().name))

print("Program execution started by",threading.current_thread().name)
t1obj=threading.Thread(target=first)
t2obj=threading.Thread(target=second)
t1obj.start()
t2obj.start()
t1obj.join()
t2obj.join()
print("Program execution ended by",threading.current_thread().name)