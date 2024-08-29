"""n=input()
k=n.replace("g","")
h=k.replace("ef","")
print(h)
"""
n=5
l=list(map(int,input().split()))
for i in range(1,n):
    key=l[i]
    j=i-1
    while j>=0 and l[j]>key:
        l[j+1]=l[j]
        j=j-1
    l[j+1]=key
print(l)
c=0
j=0
f = l[0] - l[1]
for i in range (n):
    if l[0]+j*f==l[i]:
        print("true")
        c=0
        j+=1
    else:
        c=1
        break
if c==0:
    print(1)
else:
    print(0)




