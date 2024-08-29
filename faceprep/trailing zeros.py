
"""
n=25
pow=5
res=0
while n>=pow:
    res=res+n//pow
    pow=pow*5
print(res)
prime number
n=7
flag=0
i=2
while i**2<=n:
    if n%i==0:
        flag+=1
    else:
        flag+=0
    i+=1
if flag==0:
    print("yes")
else:
    print("no")

n=7
flag=0
i=2
while i<=n//2:
    if n%i==0:
        flag+=1
    else:
        flag+=0
    i+=1
if flag==0:
    print("yes")
else:
    print("no")

n=int(input())
k=int(input())
for i in range (n,k+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")
"""
l=[1,2,3,4]
n=len(l)
k=[]
for i in range (n-1,-1,-1):
    s=0
    for j in range (i+1):
        s+=l[j]
    k.insert(0,s)
print(k)

    
    
    





































































