class Node:
    def __init__(self, value):
        self.value = value 
        self.next : Node | None = None

class LinkedList:
    #Creating of a LinkedList
    def __init__(self, value=None):
        if value is None:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
    
    #Printing a LinkedList
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result

    #Inserting an Node in LL

    #1. Inserting node at END 
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            assert self.tail is not None # The assert tells both Python and Pylance that self.tail cannot be None at that point.
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    #2. Inserting node at the start
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    # 3. Inserting node at the middle
    def insert(self, value, index ):
        new_node = Node(value)
        temp_node = self.head
        if index == 0:
            self.prepend(value)
        elif index < 0 or index > self.length:
            return False
        else:
            for _ in range(index-1):
                assert temp_node is not None
                temp_node = temp_node.next
            assert temp_node is not None
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True
    
    # Traversing in LinkedList
    def traverse(self):
        current = self.head
        while current :
            print(current.value)
            current = current.next
    
    #Searching for element in LinkedList
    def search(self, value):
        current = self.head 
        position = 0
        while current:
            if current.value == value:
                return f"{value} at {position}"
            position += 1
            current = current.next
        return "Value does not exist."
    
    # Get Method -> value at the index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        current = self.head
        for _ in range(index):
            assert current is not None
            current = current.next

        assert current is not None
        return current
    
    # Set_value Method -> Update value at the index
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    #POP first method 
    def pop_first(self):
        popped_node = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.length == 0:
            return None
        else:
            assert self.head is not None
            self.head = self.head.next

            assert popped_node is not None
            popped_node.next = None
            self.length -= 1    
        assert popped_node is not None
        return popped_node.value
    
    #Pop method -> remove last element and return the node
    def pop(self):
        popped_node = self.tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.length == 0:
            return None
        else:
            temp = self.head

            assert temp is not None
            while temp.next is not self.tail: # type: ignore
                assert temp is not None
                temp = temp.next

            self.tail = temp
            assert temp is not None
            temp.next = None
        self.length -= 1    
        return popped_node.value # type: ignore
    
    # Remove -> removing node at the given index
    def remove(self, index):
        pop_node = self.head
        prev_node = self.head
        if index == 0:
            self.pop_first()
        
        elif index >= self.length or index <0:
            return None

        elif index == self.length -1 :
            return self.pop()
        
        else:
            for _ in range(index):
                pop_node = pop_node.next # type: ignore
            
            while prev_node.next is not pop_node:   # type: ignore
                prev_node = prev_node.next          # type: ignore
            prev_node.next = pop_node.next          # type: ignore
            pop_node.next = None                    # type: ignore

        self.length -= 1
        return pop_node.value  # type: ignore

    #Deleting all node
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0




# new_ll= LinkedList(10)
# print(new_ll.head.value)
new_ll = LinkedList()
new_ll.append(10)
new_ll.append(20)
new_ll.append(30)

new_ll.append(40)
new_ll.append(50)
new_ll.append(60)

# print(new_ll)

new_ll.prepend(0)
# print(new_ll)

# new_ll.insert(1,1)
print(new_ll)
# new_ll.traverse()
# print(new_ll.search(100))
# print(new_ll.set_value(1, 23))
# print(new_ll.pop())
print(new_ll.remove(2))
print(new_ll)