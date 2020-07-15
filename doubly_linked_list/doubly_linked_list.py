"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        # Initialize new node - previous and next default to none.
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        # Delete head
        if self.prev == None:
            self.next.prev = None
        # Delete tail
        elif self.next == None:
            self.prev.next == None
        # Else case
        else:
            self.prev.next == self.next
            self.next.prev == self.prev
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        # Keep track of length, if none passed in
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # Create instance of ListNode with value
        self.new_node = ListNode(value)
        # If DLL is empty
        if self.length == 0:
            # Set head and tail to the new node instance
            self.head = self.new_node
            self.tail = self.new_node
        # If DLL is not empty
        else:
            # Set new node's next to current head
            self.new_node.next = self.head
            # Set head's prev to new node
            self.head.prev = self.new_node
            # Set head to the new node
            self.head = self.new_node
        # Increment the DLL length attribute
        self.length += 1
        
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # Store the value of the head
        head = self.head.value  
        # Delete the head
        # If head.next is not None
        if self.head.next != None:
            # Set head.next prev to self's prev
            self.head.delete()
            # Set head to head.next
            self.head = self.head.next
        # Else if head.next is None
        else:
            # Set head to None
            self.head = None
            # Set tail to None
            self.tail = None
        # Decrement the length of the DLL
        self.length -= 1
        # Return the value
        return head
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # Create instance of ListNode with value
        self.new_node = ListNode(value)
        # If DLL is empty
        if self.length == 0:
            # Set head and tail to the new node instance
            self.head = self.new_node
            self.tail = self.new_node
        # If DLL is not empty
        else:
            # Set new node's prev to current tail
            self.new_node.prev = self.tail
            # Set tails's next to new node
            self.tail.next = self.new_node
            # Set tail to the new node
            self.tail = self.new_node            
        # Increment the DLL length attribute
        self.length += 1
                   

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # Store the value of the tail
        tail = self.tail.value 
        # Delete the tail
        # If tail.prev is not None
        if self.tail.prev != None:
            # Set tail.prev next to self's next
            self.tail.delete()
            # Set tail to tail.prev
            self.tail = self.tail.prev
        # Else if tail.prev is None
        else:
            # Set head to None
            self.head = None
            # Set tail to None
            self.tail = None
        # Decrement the length of the DLL
        self.length -= 1
        # Return the value
        return tail


    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # If node is not head or None
        if (node != self.head) and (node != None):
            # If node is tail
            if node == self.tail:
                # Set new tail 
                self.tail = self.tail.prev
            # Remove node/ reset pointers
            node.delete()
            # Set current head's prev
            self.head.prev = node
            # Set node's next
            node.next = self.head
            # Set node's prev
            node.prev = None
            # Set new head 
            self.head = node
      
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # If node is not tail or None
        if (node != self.tail) and (node != None):
            # If node is head
            if node == self.head:
                # Set new head 
                self.head = self.head.next
            # Remove node / reset pointers
            node.delete()
            # Set current tail's next
            self.tail.next = node
            # Set node's prev
            node.prev = self.tail
            # Set node's next
            node.next = None
            # Set new tail 
            self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 1:
            self.head = None
            self.tail = None
        elif self.length != 0:
            if node == self.head:
                self.remove_from_head()
            elif node == self.tail:
                self.remove_from_tail()
            else:
                node.delete()
                # Decrement the length of the DLL
                self.length -= 1


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # Start at head node
        node = self.head
        # Set value to max
        max_node = node.value
        # Run through list
        while node.next != None:
            # If next node is bigger
            if node.value < node.next.value:
                # Reset max_node
                max_node = node.next.value
            # Move to next node
            node = node.next
        return max_node


if __name__ == "__main__":
   dll = DoublyLinkedList()
    # dll.add_to_tail(10)
    # dll.add_to_tail(15)
    # dll.add_to_tail(45)
    # dll.add_to_tail(20)
    # head = dll.head
    # second = dll.head.next
    # tail = dll.tail