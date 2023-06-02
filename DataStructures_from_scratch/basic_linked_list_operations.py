'''
Linked List Basic Operation
'''

# a linked list that stores a group of strings
list_1 = []

# add some string elements to list_1
list_1.append('California')
list_1.append('Texas')
list_1.append('Florida')
list_1.append('Arizona')
list_1.append('Georgia')

# display the list
print("The existing list : ", list_1)


# display the menu
option = 0
while option < 5:
    print("Linked List Operations : ")
    print("1 Add element ")
    print("2 Remove element ")
    print("3 Replace element ")
    print("4 Search element ")
    print("5 Exit ")
    option = int(input('Enter your choice: '))
    
    if option == 1:
        print('Operation: add element')
        print('Before operation: ', list_1)
        ele = input('Enter the element: ')
        pos = int(input('Enter the position: '))
        list_1.insert(pos, ele)
        print('After operation: ', list_1)
    elif option == 2:
        print('Operation: remove element')
        print('Before operation: ', list_1)
        try:
            ele = input('Enter the element: ')
            list_1.remove(ele)
            print('After operation: ', list_1)
        except ValueError:
            print("Element not found")
    elif option == 3:
        print('Operation: replace element')
        print('Before operation: ', list_1)
        ele = input('Enter the element: ')
        pos = int(input('Enter the position: '))
        list_1.pop(pos)
        list_1.insert(pos, ele)
        print('After operation: ', list_1)
    elif option == 4:
        print('Operation: search element')
        print('Before operation: ', list_1)
        try:
            ele = input('Enter the element: ')
            pos = list_1.index(ele)
            print('Element found at position ', pos)
        except ValueError:
            print('Elemet not found')
        print('After operation: ', list_1)
    else:
        break
        
"""
### Output of Sample Run
runfile('C:/Users/######/.spyder-py3/basic_linked_list_operations.py', wdir='C:/Users/#######/.spyder-py3')
The existing list :  ['California', 'Texas', 'Florida', 'Arizona', 'Georgia']
Linked List Operations : 
1 Add element 
2 Remove element 
3 Replace element 
4 Search element 
5 Exit 

Enter your choice: 1
Operation: add element
Before operation:  ['California', 'Texas', 'Florida', 'Arizona', 'Georgia']

Enter the element: Washington

Enter the position: 4
After operation:  ['California', 'Texas', 'Florida', 'Arizona', 'Washington', 'Georgia']
Linked List Operations : 
1 Add element 
2 Remove element 
3 Replace element 
4 Search element 
5 Exit 

Enter your choice: 2
Operation: remove element
Before operation:  ['California', 'Texas', 'Florida', 'Arizona', 'Washington', 'Georgia']

Enter the element: Florida
After operation:  ['California', 'Texas', 'Arizona', 'Washington', 'Georgia']
Linked List Operations : 
1 Add element 
2 Remove element 
3 Replace element 
4 Search element 
5 Exit 

Enter your choice: 3
Operation: replace element
Before operation:  ['California', 'Texas', 'Arizona', 'Washington', 'Georgia']

Enter the element: Hawaii

Enter the position: 4
After operation:  ['California', 'Texas', 'Arizona', 'Washington', 'Hawaii']
Linked List Operations : 
1 Add element 
2 Remove element 
3 Replace element 
4 Search element 
5 Exit 

Enter your choice: 4
Operation: search element
Before operation:  ['California', 'Texas', 'Arizona', 'Washington', 'Hawaii']

Enter the element: Arizona
Element found at position  2
After operation:  ['California', 'Texas', 'Arizona', 'Washington', 'Hawaii']
Linked List Operations : 
1 Add element 
2 Remove element 
3 Replace element 
4 Search element 
5 Exit 

Enter your choice: 5

"""
        
