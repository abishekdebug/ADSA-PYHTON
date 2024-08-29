"""
from abc import ABC,abstractmethod
class briyani(ABC):
    @abstractmethod
    def making(self):
        pass
class chef(briyani):
    def making(self):
        print("hgfd")
c=chef()
c.making()

class Bank:
    def __init__(self,bal):
        self.__bal=bal
    def dep(self,value):
        self.__bal+=value
    def wid(self,amt):
        if self.__bal>=amt:
            self.__bal-=amt
        else:
            print("nahi")
    def viewbal(self):
        return self.__bal
b=Bank(100)
b.dep(500)
b.wid(200)
print(b.viewbal())    
"""
n=int(input())
for i in range(2,n):
    for j in range (1,i):
        if i%j==0:
            break
        else:
            print(i)
            













































































     
