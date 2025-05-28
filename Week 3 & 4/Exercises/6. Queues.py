import time
from collections import deque
import threading

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def front(self):
        return self.buffer[-1]
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)

queue = Queue()

# 1. Design a food ordering system where your python program will run two threads,
#     1. Place Order: This thread will be placing an order and inserting that into a queue. 
#        This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)

def place_order(orders):
    global queue
    for order in orders:
        time.sleep(0.5)
        print("Placing the following orders:", order)
        queue.enqueue(order)

#     1. Serve Order: This thread will server the order. 
#        All you need to do is pop the order out of the queue and print it. 
#        This thread serves an order every 2 seconds.
#        Also start this thread 1 second after place order thread is started.

def serve_order():
    global queue
    while not queue.is_empty():
        time.sleep(2)
        order = queue.dequeue()
        print("Your order is:", order)

#     Pass following list as an argument to place order thread,
orders = ['pizza','samosa','pasta','biryani','burger']

thread1 = threading.Thread(target=place_order,args=(orders,))
thread2 = threading.Thread(target=serve_order,args=())

thread1.start()
time.sleep(1)
thread2.start()

thread1.join()
thread2.join()

#     This problem is a producer,consumer problem where place_order thread is producing orders
#     whereas server_order thread is consuming the food orders.
#     Use Queue class implemented in a video tutorial.

# 2. Write a program to print binary numbers from 1 to 10 using Queue.
#  Use Queue class implemented in main tutorial.
# Binary sequence should look like,

#     1
#     10
#     11
#     100
#     101
#     110
#     111
#     1000
#     1001
#     1010

queue = Queue()
queue.enqueue("1")
for i in range(10):
    front = queue.front()
    print(" ", front, end=" ")
    queue.enqueue(front+"0")
    queue.enqueue(front+"1")
    queue.dequeue()


# Hint: Notice a pattern above. After 1 second and third number is 1+0 and 1+1.
#  4th and 5th number are second number (i.e. 10) + 0 and second number (i.e. 10) + 1.

# You also need to add front() function in queue class that can return the front element in the queue.
