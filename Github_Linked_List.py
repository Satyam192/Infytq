# Creating Linked List

class node:
    def __init__(self , dataval = None):
        self.dataval = dataval
        self.nextval = None

class slinkedlist:
    def __init__(self):
        self.headval = None
    def printlist(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

linkedlist = slinkedlist()

linkedlist.headval = node("monday")
linkedlist.headval.nextval = e2
e2 = node("tudesday")
e2.nextval = e3
e3 = node("Wednesday")

linkedlist.printlist()





#Traverse Linked List

class node:
    def __init__(self , dataval = None):
        self.dataval = dataval
        self.nextval = None

class slinkedlist:
    def __init__(self):
        self.headval = None
    def printlist(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

linkedlist = slinkedlist()

linkedlist.headval = node("monday")
linkedlist.headval.nextval = e2
e2 = node("tudesday")
e2.nextval = e3
e3 = node("Wednesday")

linkedlist.printlist()

# Inserting an item in linked list

class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None
# Print the linked list
   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval
   def AtBegining(self,newdata):
      NewNode = Node(newdata)
   NewNode.nextval = self.headval
   self.headval = NewNode

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.headval.nextval = e2
e2.nextval = e3

list.AtBegining("Sun")
list.listprint()


#Removing an item in linked list

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode

    # Function to remove node
    def RemoveNode(self, Removekey):
        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next
        HeadVal = None


def LListprint(self):
    printval = self.head
    while (printval):
        print(printval.data),
        printval = printval.next


llist = SLinkedList()
llist.Atbegining("Mon")
llist.Atbegining("Tue")
llist.Atbegining("Wed")
llist.Atbegining("Thu")
llist.RemoveNode("Tue")
llist.LListprint()