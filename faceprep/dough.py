n=6
l=[1,0,2,2,0,1]
low,mid,high=0,0,n-1
while mid<=high:
    if l[mid]==0:
        l[low],l[mid]=l[mid],l[low]
        low+=1
        mid+=1
    elif l[mid]==1:
        mid+=1
    elif l[mid]==2:
        l[mid],l[high]=l[high],l[mid]
        high-=1
print(l)
        
    
