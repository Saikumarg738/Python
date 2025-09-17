#This Program Sets and Gets the Name of the Sub Thread
#SetGetNameSubThreadEx1.py
import threading

def hello():
    print(f"Hello sai, this is {threading.current_thread().name}")

t1=threading.Thread(target=hello)

print(f"Default name of thread  : {threading.current_thread().name}")

t1.name="ThreadSai"
t1.start()
print(f"Custom name of thread  : {threading.current_thread().name}")
