# -*- coding: utf-8 -*-
# Creating Stack class
class Stack:
    def __init__(self):
        self.st = []
        
    def isempty(self):
        return self.st == []
    
    def push(self, element):
        self.st.append(element)
        
    def pop(self):
        if self.isempty():
            return -1
        else:
            return self.st.pop()
        
    def peep(self):
        n = len(self.st)
        return self.st[n-1]
    
    def search(self, element):
        if self.isempty():
            return -1
        else:
            try:
                n = self.st.index(element)
                return len(self.st) - n 
            except ValueError:
                return -2
            
    def display(self):
        return self.st
    
    
# using Stack class to create Stack object
s = Stack()

option=0
while option<5:
    print("Stack Operations : ")
    print("1 Push element")
    print("2 Pop element")
    print("3 Peep element")
    print("4 Search for element")
    print("5 Exit")
    option = int(input('Enter your choice: '))
    
    if option==1:
        print("Operation: Push element")
        print("Before operation : ", s)
        ele = int(input("Enter element: "))
        s.push(ele)
        print("After operation : ", s)
    elif option==2:
        print("Operation: Pop element")
        print("Before operation : ", s)
        ele = s.pop()
        if ele == -1:
            print("Stack is empty!")
        else:
            print("Elememt popped: ", ele)
            print("After operation : ", s)
    elif option==3:
        print("Operation: Peep element")
        print("Before operation : ", s)
        ele = s.peep()
        print("Topmost element: ", ele)
        print("After operation : ", s)
    elif option==4:
        print("Operation: Search element")
        print("Before operation : ", s)
        ele = int(input('Enter element: '))
        idx = s.search(ele)
        if idx == -1:
            print('The stack is empty')
        elif idx == -2:
            print('Element not found in stack!')
        else:
            print('Element found at position: ', idx)
            print("After operation : ", s)
            
    else:
        break
    
    print("stack : ", s.display())
    
"""
Output of sample run

runfile('C:/Users/######/.spyder-py3/DSA from scratch/stack_in_python.py', wdir='C:/Users/######/.spyder-py3/DSA from scratch')
Stack Operations : 
1 Push element
2 Pop element
3 Peep element
4 Search for element
5 Exit

Enter your choice: 1
Operation: Push element
Before operation :  <__main__.Stack object at 0x0000023BCBE46040>

Enter element: 11
After operation :  <__main__.Stack object at 0x0000023BCBE46040>
stack :  [11]
Stack Operations : 
1 Push element
2 Pop element
3 Peep element
4 Search for element
5 Exit

Enter your choice: 1
Operation: Push element
Before operation :  <__main__.Stack object at 0x0000023BCBE46040>

Enter element: 22
After operation :  <__main__.Stack object at 0x0000023BCBE46040>
stack :  [11, 22]
Stack Operations : 
1 Push element
2 Pop element
3 Peep element
4 Search for element
5 Exit

Enter your choice: 1
Operation: Push element
Before operation :  <__main__.Stack object at 0x0000023BCBE46040>

Enter element: 33
After operation :  <__main__.Stack object at 0x0000023BCBE46040>
stack :  [11, 22, 33]
Stack Operations : 
1 Push element
2 Pop element
3 Peep element
4 Search for element
5 Exit

Enter your choice: 1
Operation: Push element
Before operation :  <__main__.Stack object at 0x0000023BCBE46040>

Enter element: 44
After operation :  <__main__.Stack object at 0x0000023BCBE46040>
stack :  [11, 22, 33, 44]
Stack Operations : 
1 Push element
2 Pop element
3 Peep element
4 Search for element
5 Exit

Enter your choice: 1
Operation: Push element
Before operation :  <__main__.Stack object at 0x0000023BCBE46040>

Enter element: 55
After operation :  <__main__.Stack object at 0x0000023BCBE46040>
stack :  [11, 22, 33, 44, 55]
Stack Operations : 
1 Push element
2 Pop element
3 Peep element
4 Search for element
5 Exit

Enter your choice: 1
Operation: Push element
Before operation :  <__main__.Stack object at 0x0000023BCBE46040>

Enter element: 66
After operation :  <__main__.Stack object at 0x0000023BCBE46040>
stack :  [11, 22, 33, 44, 55, 66]
Stack Operations : 
1 Push element
2 Pop element
3 Peep element
4 Search for element
5 Exit

Enter your choice: 1
Operation: Push element
Before operation :  <__main__.Stack object at 0x0000023BCBE46040>

Enter element: 77
After operation :  <__main__.Stack object at 0x0000023BCBE46040>
stack :  [11, 22, 33, 44, 55, 66, 77]
Stack Operations : 
1 Push element
2 Pop element
3 Peep element
4 Search for element
5 Exit

Enter your choice: 1
Operation: Push element
Before operation :  <__main__.Stack object at 0x0000023BCBE46040>

Enter element: 88
After operation :  <__main__.Stack object at 0x0000023BCBE46040>
stack :  [11, 22, 33, 44, 55, 66, 77, 88]
Stack Operations : 
1 Push element
2 Pop element
3 Peep element
4 Search for element
5 Exit

Enter your choice: 2
Operation: Pop element
Before operation :  <__main__.Stack object at 0x0000023BCBE46040>
Elememt popped:  88
After operation :  <__main__.Stack object at 0x0000023BCBE46040>
stack :  [11, 22, 33, 44, 55, 66, 77]
Stack Operations : 
1 Push element
2 Pop element
3 Peep element
4 Search for element
5 Exit

Enter your choice: 3
Operation: Peep element
Before operation :  <__main__.Stack object at 0x0000023BCBE46040>
Topmost element:  77
After operation :  <__main__.Stack object at 0x0000023BCBE46040>
stack :  [11, 22, 33, 44, 55, 66, 77]
Stack Operations : 
1 Push element
2 Pop element
3 Peep element
4 Search for element
5 Exit

Enter your choice: 4
Operation: Search element
Before operation :  <__main__.Stack object at 0x0000023BCBE46040>

Enter element: 55
Element found at position:  3
After operation :  <__main__.Stack object at 0x0000023BCBE46040>
stack :  [11, 22, 33, 44, 55, 66, 77]
Stack Operations : 
1 Push element
2 Pop element
3 Peep element
4 Search for element
5 Exit

Enter your choice: 5

"""