top=-1
l=[]
def push(c):
    value=int(input())
    l.append(c)
    top+=1
def pop():
    if top==-1:
        print("dfghj")
    else:
        l.pop(0)
        top-=1
n=int(input())
for i in range (n):
    c=input()
    if c=="push":
        push(value)
    else:
        pop()
