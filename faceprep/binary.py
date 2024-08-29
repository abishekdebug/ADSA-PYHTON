ele=int(input())
l=[10,2,7,3,1,9,8,4,6,5]
l.sort()
n=len(l)
left=0
right=n-1
while left<=right:
    d=(left+right)//2
    mid=l[d]
    if mid==ele:
        print(mid)
        break
    if mid<ele:
        left=d+1
    elif mid > ele:
        right=d-1
else:
    print("no")
    

