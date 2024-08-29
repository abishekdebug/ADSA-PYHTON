"""
n=int(input())
l=list(map(int,input().split()))
m=min(l)
k=0
h=[]
for i in range(n):
    if m==l[i]:
        k=i
for i in range (k+1,n):
        d=l[i]-m
        h.append(d)

f=max(h)
print(f)

n=int(input())
h=[]
l=list(map(int,input().split()))
for i in range(n):
    for j in range(1,n):
        if i!=j:
            d=l[j]-l[i]
            h.append(d)
print(max(h))

n=int(input())
a=list(map(int,input().split()))
max=0
for i in range (n):
    for j in range(1,n):
        d=a[j]-a[i]
        if a[i]<a[j] and max<d:
            max=d
print(max)
n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    count=1
    for j in range(i+1,n):
        if l[i]==l[j]:
             count+=1
    if count>=2:
        print(l[i])

n=5
l=[2,3,1,1,4]
i=0
while i<n:
    k=l[i]
    if k==0:
          print("False")
        break
    if i==n-1:
        print("True")
    i+=k

k=int(input())
l=[2,3,1,1,4]
for i in range(k):
    d=l.pop()
    l.insert(0,d)
print(l)


t=4
l=[1,2,3,4]
n=len(l)
for i in range(n):
    if l[i]==4:
        print(i)

"""
n=int(input())
l=list(map(int,input().split()))
r=[]
for i in range(n):
    product=1
    for j in range(n):
        if i!=j:
            product*=l[j]
    r.append(product)
for r in r:
    print(r,end=" ")
    


        
    
             
    


    
    
        
    

