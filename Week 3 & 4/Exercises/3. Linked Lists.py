# # Exercise: Linked List

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head, None)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr.prev)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        current = self.head # Assign head to current node
        while current.data!=data_after: 
            # While current node is not equal to data_after or -1
            current = current.next # Assign the next node to the current node
        node = Node(data_to_insert) # Create a new node to insert after current node
        node.next = current.next
        current.next = node # Data_After now points to current
    
    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head == None:
            print("List doesn't exist.")
        current = self.head
        if current.data == data: # If the first node contains the data
            self.head = self.head.next # Assign the head to the next node
        else:
            while current.data != data: 
                # While current node is not equal to data_after or -1
                previous = current
                current = current.next # Assign the next node to the current node
                if current is None:
                    break
            
            if current == None: # If node doesn't exist
                print("Node could not be found!")
            else:
                previous.next = None

    def print_forward(self):
        # This method prints list in forward direction. Use node.next
        current = self.head
        while current != None:
            print(current.data, "--> ", end="")
            current = current.next
        print("")

    def print_backward(self):
        # Print linked list in reverse direction. Use node.prev for this.
        current = self.head
        while current.next != None:
            current = current.next
        while current != None:
            print(current.data, "--> ", end="")
            current = current.prev
        print("")


# 1. In [LinkedList class] that we implemented in our tutorial add following two methods,

# def insert_after_value(self, data_after, data_to_insert):
#     # Search for first occurance of data_after value in linked list
#     # Now insert data_to_insert after data_after node

# def remove_by_value(self, data):
#     # Remove first node that contains data

# Now make following calls,

# ll = LinkedList()
# ll.insert_values(["banana","mango","grapes","orange"])
# ll.print()
# ll.insert_after_value("mango","apple") # insert apple after mango
# ll.print()
# ll.remove_by_value("orange") # remove orange from linked list
# ll.print()
# ll.remove_by_value("figs")
# ll.print()
# ll.remove_by_value("banana")
# ll.remove_by_value("mango")
# ll.remove_by_value("apple")
# ll.remove_by_value("grapes")
# ll.print()

# 2. Implement doubly linked list. The only difference with regular linked list is that 
# double linked has prev node reference as well. 
# That way you can iterate in forward and backward direction.
# Your node class will look this this,

# class Node:
#     def __init__(self, data=None, next=None, prev=None):
#         self.data = data
#         self.next = next
#         self.prev = prev

# Add following new methods,

# def print_forward(self):
#     # This method prints list in forward direction. Use node.next

# def print_backward(self):
#     # Print linked list in reverse direction. Use node.prev for this.

# Implement all other methods in [regular linked list class] and make necessary changes 
# for doubly linked list (you need to populate node.prev in all those methods)

ll = LinkedList()
ll.insert_values(["banana","mango","grapes","orange"])
ll.print_backward()