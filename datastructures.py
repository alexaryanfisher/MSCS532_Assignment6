'''
Assignment 6, Part 2 : Elementary Data Structures

implentation of different data structures in Python. Data structures include Arrays and Matrices, Stacks, Queues, and Linked Lists. 
This includes performanace testing and use cases. 

'''

# Array and Matrices with the use of a list.
def array_oper():
    print("Print Array and Matrices Operations ")

    # Array: One dimensional (List)
    arr = [5, 10, 15, 20, 25]
    print (f"Initial array: {arr}")

    # Showing element at a specific index.
    print(f"Element at Index 3: {arr[3]}")

    # Inserting into array.
    arr.insert(5, 30)
    print(f"Insert 30 at Index 5, Show Index 5: {arr[5]}")
    print(f"Printing Current array after insertion: {arr}")

    # Deletion at specific index.
    del arr[4]
    print(f"Printing array after deleting element at index 4: {arr}")

    # Matrix: Two dimensional (List of List)
    matrix = [[5, 10, 15],
              [20, 25, 30],
              [35, 40, 45]]
    print(f"\nInitial Matrix : \n {matrix[0]} \n {matrix[1]} \n {matrix[2]}")

    # Showing matrix element.
    print(f"Element at Row 2, Col 1: {matrix[1][0]}")


# Stack with use of a list. First In, First Out.
class Stack:
    def __init__(self):
        self.items = []
    
    # Check is stack is empty.
    def is_empty(self):
        return not self.items
    
    # Add item to top of the stack.
    def push(self, item):
        self.items.append(item)

    # Remove item to top of the stack.
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from Empty Stack.")
        return self.items.pop()

    # Return top (last) element on the stack.
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from Empty Stack.")
        return self.items[-1]

    # Find number of elements in stack.
    def size(self):
        return len(self.items)

    # Display stack.
    def __repr__(self):
        return f"Stack ({self.items})"

# Show stack operations.
def stack_oper():
    print("\nStack Operations ")
    stack = Stack()
    print(f"Stack Empty? {stack.is_empty()}")
    stack.push(5)
    stack.push(10)
    stack.push(15)
    print(f"Stack after pushes: {stack}")
    print(f"Peek (Top Element): {stack.peek()}")
    print(f"Pop Element: {stack.pop()}")
    print(f"Stack Size: {stack.size()}")

# Queue with use of Python List
class Queue:
    def __init__(self):
        self.items = []
    
    # Check is queue is empty.
    def is_empty(self):
        return not self.items
    
    # Add item to back of queue.
    def enqueue(self, item):
        self.items.append(item)

    # Remove item and return the first element from queue.
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from Empty Queue.")
        return self.items.pop(0)

    # Find number of elements in queue.
    def size(self):
        return len(self.items)

    # Display queue.
    def __repr__(self):
        return f"Queue ({self.items})"

# Show queue operations.
def queue_oper():
    print("\nQueue Operations ")
    queue = Queue()
    print(f"Queue Empty? {queue.is_empty()}")
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    print(f"Queue after pushes: {queue}")
    print(f"Dequeue element: {queue.dequeue()}")
    print(f"Queue after dequeue: {queue}")
    print(f"Queue Size: {queue.size()}")



# Linked List

# Node in singly linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node ({self.data})"
    
# SinglylinkedList implementation.
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    # Check if linked list is empty.
    def is_empty(self):
        return self.head is None
    
    # Insert a new node at beginning of list.
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert a new node at end of list.
    def insert_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return  

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    # Delete the first occurance of node with specific key
    def delete(self, key):   
        current_node = self.head

    # If node to be deleted is the head.
        if current_node is not None and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

    # If node to be deleted is not the head.
        previous_node = None
        while current_node is not None and current_node.data != key:
            previous_node = current_node
            current_node = current_node.next
    
    # If key not found.
        if current_node is None:
            return
        
    # Unlink the node.
        previous_node.next = current_node.next
        current_node = None
    
   # Traverse list and prints all. 
    def traverse(self):
        result = []
        current_node = self.head
        while current_node is not None:
            result.append(current_node.data)
            current_node = current_node.next
        return result

    def __repr__(self):
        nodes = self.traverse()
        return f"SinglyLinkedList({' --> '.join(map(str, nodes))})"

#Show Singly Linked List Operations.

def singlylinkedlist_oper():
    print("\nSingly Linked List Operations")
    singly = SinglyLinkedList()
    print(f"Linked List Empty? {singly.is_empty()}")

    singly.insert_end(35)
    singly.insert_beginning(4)
    singly.insert_end(40)

    print(f"Linked list after inserts: {singly}")

    singly.delete(4)
    print(f"Linked List after deleting 4: {singly}")

if __name__ == "__main__":
    array_oper()
    stack_oper()
    queue_oper()
    singlylinkedlist_oper()