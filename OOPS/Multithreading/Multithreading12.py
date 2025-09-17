import threading,time

class count:
    def seq(self):
        n=int(input("Enter seq : "))
        print("-"*50)
        for i in range(1,n+1):
            print(f"{threading.current_thread().name} : Number is {i}")
            time.sleep(0.5)
        else:
            print("-"*50)

a=threading.Thread(target=count().seq)
a.start()