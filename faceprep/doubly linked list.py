#palindrome
class Node:
    def __init__(self,value):
        self.value=value
        self.pre=None
        self.next=None
class globe:
    def __init__(self):
        self.head=None
        self.tail=None
    def create (self):
        value=int(input())
        while value!=-1:
            newnode=Node(value)
            if self.head is None:
                self.head=newnode
                self.tail=newnode
            else:
                self.tail.next=newnode
                newnode.pre=self.tail
                self.tail=newnode               
            value=int(input())
    def check(self):
        temp=self.head
        temp1=self.tail
        flag=0
        while temp is not None and temp1 is not None:
            if temp.value==temp1.value:
                temp=temp.next
                temp1=temp1.pre
            else:
                flag=1
                break
        if flag==0:
            print("palindrom")
        else:
            print("not palindrom")
c=globe()
c.create()
c.check()

        
    
