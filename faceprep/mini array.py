r=int(input())
c=int(input())
n=r*c
l=[]
for i in range (r):
    li=list(map(int,input().split()))
    l.append(li)

for i in range (n):
    for j in range (n-1):
        cur_i,cur_j=divmod(j,c)
        next_i=(j+1)//c
        next_j=(j+1)%c
        
        if l[cur_i][cur_j]>l[next_i][next_j]:
            l[cur_i][cur_j],l[next_i][next_j]=l[next_i][next_j],l[cur_i][cur_j]
            
print(l)
        
