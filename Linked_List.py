# Node class
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
 
# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None

# Computes the length of a linked list
def getLength(head):
    length = 0
    
    while head:
        length = length + 1
        head = head.next
    return length
    
# Computes the middle element of a linked list
def getMiddle(head):
  slowNode = head
  fastNode = head
  if head == None:
      return
      
  while True:
      if fastNode == None or fastNode.next == None:
          break
      slowNode = slowNode.next
      fastNode = fastNode.next.next
  return slowNode
    
    
# Computes whether linked list is even or odd
def isLengthEvenOrOdd(head):
    length = getLength(head)
    
    if length % 2 == 0:
        return print('Even')
    else:
        return print('Odd')
        
    
    
