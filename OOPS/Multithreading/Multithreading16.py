import threading

def first(lo):
    print("Current thread name is",threading.current_thread().name)
    for i in range(50):
        lo.acquire()
        print("This is line from first")
        lo.release()

def second(lo):
    print("Current thread name is",threading.current_thread().name)
    for i in range(50):
        lo.acquire()
        print("This is line from Secong")
        lo.release()

lo=threading.Lock()
a=threading.Thread(target=first,args=(lo,))
b=threading.Thread(target=second,args=(lo,))
a.start()
b.start()