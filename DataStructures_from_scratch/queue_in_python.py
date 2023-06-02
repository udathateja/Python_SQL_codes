# -*- coding: utf-8 -*-
# Creating Queue class
class Queue:
    def __init__(self):
        self.queue_1 = []
        
    def isempty(self):
        return self.queue_1 == []
    
    def add(self, element):
        self.queue_1.append(element)
        
    def delete(self):
        if self.isempty():
            return -1
        else:
            return self.queue_1.pop(0)
        
    def search(self, element):
        if self.isempty():
            return -1
        else:
            try: 
                n = self.queue_1.index(element)
                return n+1
            except ValueError:
                return -2
            
    def display(self):
        return self.queue_1
    
# creating queue object from Queue class
# and perform some basic operations
q1 = Queue()

# display menu
option = 0 
while option < 4:
    print('Queue Operations: ')
    print("1 Add element")
    print("2 Delete element")
    print("3 Search for element")
    print("4 Exit")
    option = int(input("Enter your choice: "))
    
    if option==1:
        print("Operation: Add element")
        print("Before: ", q1)
        ele = float(input("Enter element: "))
        q1.add(ele)
        print("After: ", q1)
        
    elif option==2:
        print("Operation: Delete element")
        print("Before: ", q1)
        ele = q1.delete()
        if ele == -1:
            print('The queue is empty!')
        else:
            print("Removed element: ", ele)
        print("After: ", q1)
    
    elif option==3:
        print("Operation: Search for an element")
        print("Before: ", q1)
        ele = float(input("Enter element: "))
        idx=q1.search(ele)
        if idx==-1:
            print("The queue is empty!")
        else:
            print("The element found at position: ", idx)
        print("After: ", q1)
    else:
        break
    
    #display the queue 
    print("queue: ", q1.display())
    
    
"""
Output of sample run

runfile('C:/Users/######/.spyder-py3/DSA from scratch/queue_in_python.py', wdir='C:/Users/######/.spyder-py3/DSA from scratch')
Queue Operations: 
1 Add element
2 Delete element
3 Search for element
4 Exit

Enter your choice: 1
Operation: Add element
Before:  <__main__.Queue object at 0x0000023BCBE48040>

Enter element: 23
After:  <__main__.Queue object at 0x0000023BCBE48040>
queue:  [23.0]
Queue Operations: 
1 Add element
2 Delete element
3 Search for element
4 Exit

Enter your choice: 1
Operation: Add element
Before:  <__main__.Queue object at 0x0000023BCBE48040>

Enter element: 34
After:  <__main__.Queue object at 0x0000023BCBE48040>
queue:  [23.0, 34.0]
Queue Operations: 
1 Add element
2 Delete element
3 Search for element
4 Exit

Enter your choice: 1
Operation: Add element
Before:  <__main__.Queue object at 0x0000023BCBE48040>

Enter element: 56
After:  <__main__.Queue object at 0x0000023BCBE48040>
queue:  [23.0, 34.0, 56.0]
Queue Operations: 
1 Add element
2 Delete element
3 Search for element
4 Exit

Enter your choice: 1
Operation: Add element
Before:  <__main__.Queue object at 0x0000023BCBE48040>

Enter element: 5678
After:  <__main__.Queue object at 0x0000023BCBE48040>
queue:  [23.0, 34.0, 56.0, 5678.0]
Queue Operations: 
1 Add element
2 Delete element
3 Search for element
4 Exit

Enter your choice: 1
Operation: Add element
Before:  <__main__.Queue object at 0x0000023BCBE48040>

Enter element: 6789
After:  <__main__.Queue object at 0x0000023BCBE48040>
queue:  [23.0, 34.0, 56.0, 5678.0, 6789.0]
Queue Operations: 
1 Add element
2 Delete element
3 Search for element
4 Exit

Enter your choice: 1
Operation: Add element
Before:  <__main__.Queue object at 0x0000023BCBE48040>

Enter element: 566
After:  <__main__.Queue object at 0x0000023BCBE48040>
queue:  [23.0, 34.0, 56.0, 5678.0, 6789.0, 566.0]
Queue Operations: 
1 Add element
2 Delete element
3 Search for element
4 Exit

Enter your choice: 2
Operation: Delete element
Before:  <__main__.Queue object at 0x0000023BCBE48040>
Removed element:  23.0
After:  <__main__.Queue object at 0x0000023BCBE48040>
queue:  [34.0, 56.0, 5678.0, 6789.0, 566.0]
Queue Operations: 
1 Add element
2 Delete element
3 Search for element
4 Exit

Enter your choice: 3
Operation: Search for an element
Before:  <__main__.Queue object at 0x0000023BCBE48040>

Enter element: 6789
The element found at position:  4
After:  <__main__.Queue object at 0x0000023BCBE48040>
queue:  [34.0, 56.0, 5678.0, 6789.0, 566.0]
Queue Operations: 
1 Add element
2 Delete element
3 Search for element
4 Exit

Enter your choice: 4

"""
