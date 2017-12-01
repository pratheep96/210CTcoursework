class Node(object):
      def __init__(self, value):
          self.value=value
          self.next=None
          self.previous=None
 
class List(object):
      def __init__(self):
          self.head=None
          self.tail=None
      def insert(self,n,x):
          #Not actually perfect: how do we prepend to an existing list?
          if n!=None:
              x.next=n.next
              n.next=x
              x.previous=n
              if x.next!=None:
                  x.next.previous=x              
          if self.head==None:
              self.head=self.tail=x
              x.previous=x.next=None
          elif self.tail==n:
              self.tail=x

      #Function to remove duplicate value nodes
      def deleteDuplicate(self):
            x = self.head
            duplicate = {}
            while x is not None:
                  if x.value in duplicate:
                        if x.previous is not None:
                              x.previous.next = x.next
                        if x.next is not None:
                              x.next.previous = x.previous
                        temporary = x
                        x=x.next
                        del temporary

                  else:
                        duplicate [x.value] = True
                        x = x.next        

      def display(self):
          values=[]
          n=self.head
          while n!=None:
              values.append(str(n.value))
              n=n.next
          print ("List: ",",".join(values))
         
if __name__ == '__main__':
      l=List()
      l.insert(None, Node(4))
      l.insert(l.head,Node(6))
      l.insert(l.head,Node(8))
      l.insert(l.head,Node(5))
      l.insert(l.head,Node(3))
      l.insert(l.head,Node(8))
      #Removes duplicate value from list
      l.deleteDuplicate()
    
      l.display()


#Title: Python Double Linked List Source Code
#Author: Hintea, D.
#Date: 2017
#Availability: http://cumoodle.coventry.ac.uk 

