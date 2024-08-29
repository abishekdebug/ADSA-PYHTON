"""
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
top=None
size=0
def push():
    global top,size
    value=int(input())
    newnode=Node(value)
    newnode.next=top
    top=newnode
    size+=1
def pop():
    global top,size
    print(top.value)
    if top is None:
        print("stack is empty")
    else:
        top=top.next
        size-=1
def stacksize():
    print(size)
def empty():
    global size
    if top is None:
        print("stack is empty")
    else:
        print(" stack size is",size)  

n=int(input())
def printlist():
    global top
    temp=top
    while temp is not None:
        print(temp.value)
        temp=temp.next
for i in range (n):
    c=input()
    if c=="push":
        push()
    elif c=="pop":
        pop()
    elif c=="size":
        stacksize()
    elif c=="is empty":
        empty()
    
printlist()
"""
### STACK ARRAY
"""
top=-1
size=0
l=[]
def push():
    global top
    value=int(input())
    l.append(value)
    top+=1
    size+=1
def pop():
    global top
    print(l[top])
    if top==-1:
        print("stack is empty")
    else:
        l.pop()
        top-=1
        size-=1
def stacksize():
    print(top)
def empty():
    global top
    if top==-1:
        print("stack is empty")
    else:
        print(" stack size is",top)  
def printlist():
    global top
    print(l)

n=int(input())
for i in range (n):
    c=input()
    if c=="push":
        push()
    elif c=="pop":
        pop()
    elif c=="size":
        stacksize()
    elif c=="is empty":
        empty()
    
printlist()
"""
### PARANTHESES
top=-1
l=[]
def push(value):
    global top
    l.append(value)
    top+=1
def pop(value):
    global top
    if top==-1:
        l.append(value)
        top+=1
    else:
        l.pop()
        top-=1
def empty():
    global top
    if top==-1:
        print("Balanced")
    else:
        print("unbalanced") 
n=int(input())
for i in range (n):
    c=input()
    if c=="(":
        push(c)
    elif c==")":
        pop(c)
empty()



        
    
        
