"""
n=input().split()
k=input().split()
m=[]
for i in n:
  if i==k[0]:
    m+=k[1]
  else:
    m+=i
print(m)

def su(n):
    if n==0:
        return 0
    return n+su(n-1)
n=5
f=su(n)
print(f)
# replace
n = input().split()  
k, h = input().split()  

m = []
for i in n:
    if i in k: 
        m.append(h) 
    else:
        m.append(i)  

print(*m)

#search
def find(n,t,l,i=0):
    if i>n:
        return
    if l[i]==t:
        print(i)
    return find(n,t,l,i+1)
l=[5,3,5,2,5,3]
n=len(l)
t=5
find(n-1,t,l)

power sum

def pro(a,n):
    if n==0:
        return 1 
    return a*pro(a,n-1)
a=2
n=3
print(pro(a,n))

def pali(p,n):
    if n==-1:
        return ""
    return p[n]+pali(p,n-1)
p="malayalam"
n=len(p)
k=pali(p,n-1)
if k==p:
    print("true")
else:
    print("false")

"""
def repla(n,k,r):
    if k<0:
        return h
    if h[k]==r:
        h.pop(k)
    return repla(n,k-1,r)
         
n="abixehk"
h=[]
for i in n:
    h+=i
k=len(h)-1
r="x"
print(*(repla(h,k,r)))





















