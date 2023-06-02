# -*- coding: utf-8 -*-
# Implementing Deque

from collections import deque
d = deque()

option=0
while option<7:
    print("Deque operations: ")
    print("1 Add element at front")
    print("2 Remove element from front")
    print("3 Add element at rear")
    print("4 Remove element from rear")
    print("5 Remove element from middle")
    print("6 Search element")
    print("7 Exit")
    
    option = int(input("Enter your choice: "))
    
    if option==1:
        print("Operation : adding element at front")
        print("Before: ", d)
        ele = input("Enter element:")
        d.appendleft(ele)
        print("After: ", d)
    elif option==2:
        print("Operation : deleting element at front")
        print("Before: ", d)
        if len(d) == 0:
            print("Deque is empty!")
        else:
            d.popleft()
        print("After: ", d)
    elif option==3:
        print("Operation : adding element at rear")
        print("Before: ", d)
        ele = input("Enter element:")
        d.append(ele)       
        print("After: ", d)           
    elif option==4:
        print("Operation : deleting element at rear")
        print("Before: ", d)
        if len(d) == 0:
            print("Deque is empty!")
        else:
            d.pop()
        print("After: ", d)
    elif option==5:
        print("Operation : deleting element from middle")
        print("Before: ", d)
        ele = input("Enter element: ")
        try:
            d.remove(ele)
        except ValueError:
            print("Element not found!")
        print("After: ", d)
    elif option==6:
        print("Operation : searching element")
        print("Before: ", d)
        ele = input("Enter element:")
        n = d.count(ele)
        print(ele, ' is found ', n, ' times')
        print("After: ", d)
    else:
        break
    
    
    print("Deque = ", end='')
    for x in d: 
        print(x, ' ', end='')
    print()
    
"""
Output from sample run

Deque operations: 
1 Add element at front
2 Remove element from front
3 Add element at rear
4 Remove element from rear
5 Remove element from middle
6 Search element
7 Exit

Enter your choice: 1
Operation : adding element at front
Before:  deque([])

Enter element:32
After:  deque(['32'])
Deque = 32  
Deque operations: 
1 Add element at front
2 Remove element from front
3 Add element at rear
4 Remove element from rear
5 Remove element from middle
6 Search element
7 Exit

Enter your choice: 1
Operation : adding element at front
Before:  deque(['32'])

Enter element:34
After:  deque(['34', '32'])
Deque = 34  32  
Deque operations: 
1 Add element at front
2 Remove element from front
3 Add element at rear
4 Remove element from rear
5 Remove element from middle
6 Search element
7 Exit

Enter your choice: 1
Operation : adding element at front
Before:  deque(['34', '32'])

Enter element:55
After:  deque(['55', '34', '32'])
Deque = 55  34  32  
Deque operations: 
1 Add element at front
2 Remove element from front
3 Add element at rear
4 Remove element from rear
5 Remove element from middle
6 Search element
7 Exit

Enter your choice: 3
Operation : adding element at rear
Before:  deque(['55', '34', '32'])

Enter element:567
After:  deque(['55', '34', '32', '567'])
Deque = 55  34  32  567  
Deque operations: 
1 Add element at front
2 Remove element from front
3 Add element at rear
4 Remove element from rear
5 Remove element from middle
6 Search element
7 Exit

Enter your choice: 3
Operation : adding element at rear
Before:  deque(['55', '34', '32', '567'])

Enter element:65
After:  deque(['55', '34', '32', '567', '65'])
Deque = 55  34  32  567  65  
Deque operations: 
1 Add element at front
2 Remove element from front
3 Add element at rear
4 Remove element from rear
5 Remove element from middle
6 Search element
7 Exit

Enter your choice: 2
Operation : deleting element at front
Before:  deque(['55', '34', '32', '567', '65'])
After:  deque(['34', '32', '567', '65'])
Deque = 34  32  567  65  
Deque operations: 
1 Add element at front
2 Remove element from front
3 Add element at rear
4 Remove element from rear
5 Remove element from middle
6 Search element
7 Exit

Enter your choice: 4
Operation : deleting element at rear
Before:  deque(['34', '32', '567', '65'])
After:  deque(['34', '32', '567'])
Deque = 34  32  567  
Deque operations: 
1 Add element at front
2 Remove element from front
3 Add element at rear
4 Remove element from rear
5 Remove element from middle
6 Search element
7 Exit

Enter your choice: 32

"""
    