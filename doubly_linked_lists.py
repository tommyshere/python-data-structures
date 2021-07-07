class Node:
	def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.prevNode = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.numOfNodes = 0
            
    # inserts at the ends
    # O(n)
    def insert(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)
        
        # if there are no starts
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # because it's doubly linked, have to think of the prev node
            new_node.previous = self.tail
            self.tail.nextNode = new_node
            self.tail = new_node
