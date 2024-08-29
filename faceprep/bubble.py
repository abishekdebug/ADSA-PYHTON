def bubble_sort(l, n):
    for i in range(n-1):
        for j in range(n-1-i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

l = list(map(int, input().split()))
n = len(l)
bubble_sort(l, n)
print(l)

