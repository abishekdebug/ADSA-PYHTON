"""
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class globe:
    def __init__(self):
        self.head=None
        self.tail=None
    def create(self):
        value=int(input())
        while value!=-1:
            newnode=Node(value)
            if self.head is None:
                self.head=newnode
                self.tail=newnode
            else:
                self.tail.next=newnode
                self.tail=newnode
            value=int(input())
    def insertbeg(self):
        value=int(input())
        newnode=Node(value)
        newnode.next=self.head
        self.head=newnode
    def printlist(self):
        temp=self.head
        while temp is not None:
            k=(temp.value)
            if k%2==0:
                print(k)
            temp=temp.next
        temp=self.head
        while temp is not None:
            k=(temp.value)
            if k%2!=0:
                print(k)
            temp=temp.next
c=globe()
c.create()
c.insertbeg()
c.printlist()
        
 """
####insert begining
"""
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class globe:
    def __init__(self):
        self.head=None
        self.tail=None
    def create(self):
        value=int(input())
        while value!=-1:
            newnode=Node(value)
            if self.head is None:
                self.head=newnode
                self.tail=newnode
            else:
                self.tail.next=newnode
                self.tail=newnode
            value=int(input())
    def insertbeg(self):
        value=int(input())
        newnode=Node(value)
        newnode.next=self.head
        self.head=newnode
    def insertmid(self):
        pos=int(input())
        value=int(input())
        newnode=Node(value)
        i=0
        temp=self.head
        while i<pos:
            if i==pos-1:
                newnode.next=temp.next
                temp.next=newnode
            i+=1    
            temp=temp.next       
    def printlist(self):
        temp=self.head
        while temp is not None:
            k=(temp.value)
            print(k)
            temp=temp.next

c=globe()
c.create()
c.insertmid()
c.printlist()
"""
### max element linked list
"""
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class globe:
    def __init__(self):
        self.head=None
        self.tail=None
    def create(self):
        value=int(input())
        while value !=-1:
            newnode=Node(value)
            if self.head is None:
                self.head=newnode
                self.tail=newnode
            else:
                self.tail.next=newnode
                self.tail=newnode
            value=int(input())
    def printlist(self):
        temp=self.head
        s=temp.value
        while temp is not None:
            k=temp.value
            if k>s:
                s=k    
            temp=temp.next
        print(s)
c=globe()
c.create()
c.printlist()
"""
### deletion
"""
class Node:
  def __init__(self,value):
    self.value=value
    self.next=None
class globe:
  def __init__(self):
    self.head=None
    self.tail=None
  def create(self):
    value=int(input())
    while value>0:
      newnode=Node(value)
      if self.head is None:
        self.head=newnode
        self.tail=newnode
      else:
        self.tail.next=newnode
        self.tail=newnode        
      value=int(input())
  def delete(self):
      if self != None:
          self.head=self.head.next
  def printlist(self):
    temp=self.head
    while temp is not None:
      print(temp.value)
      temp=temp.next
c=globe()
c.create()
c.delete()
c.printlist()
"""
### deletion mid
"""
class Node:
  def __init__(self,value):
    self.value=value
    self.next=None
class globe:
  def __init__(self):
    self.head=None
    self.tail=None
  def create(self):
    value=int(input())
    while value>0:
      newnode=Node(value)
      if self.head is None:
        self.head=newnode
        self.tail=newnode
      else:
        self.tail.next=newnode
        self.tail=newnode        
      value=int(input())
  def deletemid(self):
    pos=int(input())
    temp=self.head
    for i in range(pos):
      if i==pos-1:
        temp.next=temp.next.next
      temp=temp.next
  def printlist(self):
    temp=self.head
    while temp is not None:
      print(temp.value)
      temp=temp.next
c=globe()
c.create()
c.deletemid()
c.printlist()
"""
###nth node
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class globe:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def create(self):
        value = int(input())
        while value != -1:
            newnode = Node(value)
            if self.head is None:
                self.head = newnode
                self.tail = newnode
            else:
                self.tail.next = newnode
                self.tail = newnode
            value = int(input())
    
    def findnode(self):
        g = int(input())
        temp = self.head
        i = 0
        while temp is not None:
            if g == i:
                print(temp.value)
                return
            temp = temp.next
            i += 1
        print(0)

c = globe()
c.create()
c.findnode()
"""
### remove duplicate
"""
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class globe:
    def __init__(self):
        self.head=None
        self.tail=None
    def create(self):
        value=int(input())
        while value!=-1:
            newnode=Node(value)
            if self.head is None:
                self.head=newnode
                self.tail=newnode
            else:
                self.tail.next=newnode
                self.tail=newnode
            value=int(input())
    def dupli(self):
      curr=self.head
      while curr is not None:
        pre=curr
        after=curr.next
        while after is not None:
          if curr.value==after.value:
            pre.next=after.next
            after=after.next
          else:
            after=after.next
            pre=pre.next
        curr=curr.next
    def printlist(self):
        temp=self.head
        while temp is not None:
            k=(temp.value)
            print(k)
            temp=temp.next
c=globe()
c.create()
c.dupli()
c.printlist()
"""
### reverse
"""
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class globe:
    def __init__(self):
        self.head=None
        self.tail=None
    def create(self):
        value=int(input())
        while value!=-1:
            newnode=Node(value)
            if self.head is None:
                self.head=newnode
                self.tail=newnode
            else:
                self.tail.next=newnode
                self.tail=newnode
            value=int(input())
    def rev(self):
      pre=None
      curr=self.head
      after=curr
      while after is not None:
        after=curr.next
        curr.next=pre
        pre=curr
        curr=after 
    def printlist(self):
        temp=self.tail
        while temp is not None:
            k=(temp.value)
            print(k)
            temp=temp.next
c=globe()
c.create()
c.rev()
c.printlist()
"""

##reverse k
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Globe:
    def __init__(self):
        self.head = None
        self.tail = None
        self.pre = None

    def create(self):
        value = int(input("Enter node value (-1 to stop): "))
        while value != -1:
            new_node = Node(value)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            value = int(input("Enter node value (-1 to stop): "))
        return self.head

    def rev(self, head, k):
        self.pre = None
        curr = head
        after = None
        c = 0
        while curr is not None and c < k:
            after = curr.next
            curr.next = self.pre
            self.pre = curr
            curr = after
            c += 1
        if after is not None:
            head.next = self.rev(after, k)
        return self.pre
    
    def printlist(self, head):
        temp = self.pre
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next
        print()

c = Globe()
h = c.create()
k = int(input("Enter the value of k: "))
new_head = c.rev(h, k)
c.printlist(new_head)
"""




        

        

































        



