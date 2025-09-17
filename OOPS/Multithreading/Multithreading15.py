import threading

def welcome():
    print(f"Hello is from {threading.current_thread().name}")

t1=threading.Thread(target=welcome)

print(f"{t1.is_alive()}")
t1.start()
print(f"{t1.is_alive()}")