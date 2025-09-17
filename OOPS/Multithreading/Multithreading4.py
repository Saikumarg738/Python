import threading

def first():
    print("The is first method in",threading.current_thread())
def second():
    print("This is second method in",threading.current_thread().name)
def third():
    print("This is third method in",threading.current_thread().name)

firstthread=threading.Thread(target=first)
firstthread.start()