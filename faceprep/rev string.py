"""
s=input()
temp=0
for i in s:
    temp=temp*26+ord(i)-64
print(temp)
"""
n=input()
k=n.split()
s=len(k[0])
f=0
for i in range (1,len(k)):
    if len(k[i])<s:
        s=len(k[i])
        f=i
print(k[f],s)
    
