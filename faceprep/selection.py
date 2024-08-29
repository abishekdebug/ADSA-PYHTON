l = [45, 3, 99, 66, 8]
n = len(l)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if l[j] < l[min_index]:
            min_index = j
    l[i], l[min_index] = l[min_index], l[i]

print(l)


            
            
        
