"""
n=8
k=[0]*n
l=[73,74,75,71,69,72,76,73]
for i in range (n-1):
    c=1
    for j in range (i+1,n):        
        if l[i]<l[j]:
            k[i] = c
            break
        else:
            c+=1
print(k)
"""

l=[73,74,75,71,69,72,76,73]
n=len(l)
ans=[0]*n
k=[]
for i in  range (n):
    while k and l[i]>l[k[-1]]:
        j=k.pop()
        ans[i]=i-j
    k.append(i)
print(ans)
        


