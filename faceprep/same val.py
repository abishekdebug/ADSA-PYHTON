"""
n=6
l=[3,1,4,5,3,8]
t=3
i=0
s=0
while i<=n-1:

    if t==l[i]:
        i+=1
    elif t>l[i]:
        s+=t-l[i]
        i+=1
    elif t<l[i]:
        s+=l[i]-t
        i+=1

print(s)

c=int(input())
r=int(input())
l=[]
for i in range (r):
    lis=list(map(int,input().split()))
    l.append(lis)
for i in range (r):
    if    i%2==0:
        for j in range(r):
            print(l[j][i],end=" ")
    else:
        for k in range(r-1,-1,-1):
            print(l[k][i],end=" ")
"""
c=int(input())
r=int(input())
l=[]
for i in range (r):
    lis=list(map(int,input().split()))
    l.append(lis)
s=0
for i in range (r):
    for j in range (r):
        if  i==0 or i==r-1 or i+j==r-1:
            s+=l[i][j]
print(s)




    
    
              
        
        

        
    
