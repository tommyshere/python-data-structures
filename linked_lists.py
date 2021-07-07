class Node:
	def __init__(self, data):
        self.data = data
        self.nextNode = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.numOfNodes = 0
    
    
    # O(1)
    def insert_start(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node
            
            
    # O(n)
    def insert_end(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)
        
        curr = self.head
        
        while curr is not None:
            curr = curr.nextNode
        
        curr.nextNode = new_node
    
    
    def size_of_linkedList(self):
        return self.numOfNodes
        
    
    def traverse(self):
        curr = self.head
        
        while curr not None:
            print(curr)
            curr = curr.next
            
    
    def remove(self, data):
        if self.head is None:
            return
            
        curr = self.head
        prev = None
        
        while curr.data != data and curr is not None:
            prev = curr
            curr = curr.next
            
        # curr is at the data we are looking for
        # no nodes
        if curr is None:
            return
            
        self.numOfNodes = self.numOfNodes - 1
            
        # if there's only one node
        if prev is None:
            self.head = curr
        else:
            prev.next = curr.next