import threading

class MyThread(threading.Thread):
    def runs(self):
        print("Run the thread")

a=MyThread()
a.runs()