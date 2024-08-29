### factorial
"""
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
n=int(input())
print(fact(n))
"""
### fibonacci series
"""
def fibbo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibbo(n-1)+fibbo(n-2)
n=int(input())
print(fibbo(n))
"""
### prime No
def prime(n, i=2):
    if n <= 2:
        return n == 2 
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return prime(n, i + 1)

n = int(input("Enter a number: "))

if prime(n):
    print("prime")
else:
    print("not prime")

