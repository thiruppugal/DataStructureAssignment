
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
# Class for doubly Linked List
class doublyLinkedList:
    def __init__(self):
        self.Thead = None
    # --------Insert Element to Empty list--------------------
    def append(self, data):
        if self.Thead is None:
            new_node = Node(data)
            new_node.prev = None
            self.Thead = new_node
           
        else:
            new_node = Node(data)
            current_node = self.Thead
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
            new_node.next = None
           
    # ---------Insert element at the end------------------
    def prepend(self, data):
        # Check if the list is empty
        if self.Thead is None:
            new_node = Node(data)
            new_node.prev = None
            self.Thead = new_node
        else:
            new_node = Node(data)
            self.Thead.prev = new_node
            new_node.next = self.Thead
            self.Thead = new_node
       
    def DeleteAtStart(self):
        if self.Thead is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.Thead.next is None:
            self.Thead = None
            return
        self.Thead = self.Thead.next
        self.head.prev = None;
    # Delete the elements from the end
    def delete_at_end(self):
        # Check if the List is empty
        if self.Thead is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.Thead.next is None:
            self.start_node = None
            return
        current_node = self.Thead
        while current_node.next is not None:
            current_node = current_node.next
        current_node.prev.next = None
    # Traversing and Displaying each element of the list
    def Display(self):
        if self.Thead is None:
            print("The list is empty")
            return
        else:
            current_node = self.Thead
            while current_node is not None:
                print(current_node.data , end=" ")
                current_node = current_node.next
    def search(self, data):
        i=0
        if self.Thead is None:
            print("The list is empty")
            return
        else:
            current_node = self.Thead
            if current_node.data == data:
                print(i)
            else:
                i+=1
            while current_node.next is not None:
                current_node = current_node.next
                if current_node.data == data:
                    print("\n value present in position is:",i)
                    return
                i+=1
           
       
# Create a new Doubly Linked List
NewDoublyLinkedList = doublyLinkedList()
# Insert the element to empty list
NewDoublyLinkedList.append(10)
# Insert the element at the end
NewDoublyLinkedList.append(20)
NewDoublyLinkedList.append(30)
NewDoublyLinkedList.append(40)
NewDoublyLinkedList.prepend(50)
NewDoublyLinkedList.prepend(60)
NewDoublyLinkedList.Display()
NewDoublyLinkedList.search(30)
NewDoublyLinkedList.delete_at_end()
NewDoublyLinkedList.Display()








