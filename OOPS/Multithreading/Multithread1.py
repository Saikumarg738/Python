import threading

tname=threading.current_thread().name
print("Thread name is ",tname)
tcount=threading.active_count()
print("Active count is ",tcount)