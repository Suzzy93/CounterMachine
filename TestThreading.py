import threading
def hello():
    print("hello")

t= threading.Timer(10.0,hello)
t.start()
print ("Hi")
i=10
i=i+20
print (str(i))