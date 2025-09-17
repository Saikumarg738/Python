import threading

def first():
    print("First function is executed by ",threading.current_thread().name)
def second():
    print("Second function is executed by ",threading.current_thread().name)

print("-"*20)
first()
print("-"*20)
second()
