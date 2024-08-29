
"""
def eucl(a,b,r):
    if b!=0:
        return 1
    return a%b
    
a=24
b=36
eucl(a,b)



a=24
b=36
if a<b:
    a,b=b,a
while b!=0:
    r=a%b
    a,b=b,r
print(a)
"""
n=[24,36,48,2,60,12]
a=n[0]
for i in range(1,len(n)):
    b=n[i]
    if a<b:
        a,b=b,a
    while b!=0:
        r=a%b
        a,b=b,r
    a=a
print(a)

def gcd(a,b):
    if b==0:
        return a
    r=a%b
    return gcd(b,r)
l=[2,12,48,36]
d=l[0]
for i in range(1,len(l)):
    d=gcd(d,l[i])
print(d)

























    
