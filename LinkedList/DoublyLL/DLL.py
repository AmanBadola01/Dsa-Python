class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) :
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next:
                result += " <-> "
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # type: ignore
            new_node.prev = self.tail # type: ignore
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # type: ignore
            self.head.prev = new_node # type: ignore
            self.head = new_node
        self.length += 1

    def traverse(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.next

    def reverse_traverse(self):
        temp_node = self.tail
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.prev

    def search(self, target_value):
        temp_node = self.head
        index = 0
        while temp_node:
            if temp_node.value == target_value:
                return index
            temp_node = temp_node.next
            index += 1
        return -1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index < self.length // 2:
            curr_node = self.head
            for _ in range(index):
                curr_node = curr_node.next # type: ignore

        else:
            curr_node = self.tail
            for _ in range(self.length -1, index, -1):
                curr_node = curr_node.prev  # type: ignore
        return curr_node

    def set_value(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return "Index out of range."
        
        new_node = Node(value)
        if index == 0:
            self.prepend(value)
            return 

        if index == self.length:
            self.append(value)
            return 

        temp_node = self.get(index -1)
        new_node.next = temp_node.next # type: ignore
        new_node.prev = temp_node # type: ignore
        temp_node.next.prev = new_node # type: ignore
        temp_node.next = new_node # type: ignore
        self.length += 1
        return True

    def pop_first(self):
        popped_node = self.head
        if self.length == 0 :
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next # type: ignore
            self.head.prev = None # type: ignore
            popped_node.next = None # type: ignore
        self.length -= 1
        return popped_node

    def pop(self):
        popped_node = self.tail
        if not self.head:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev # type: ignore
            self.tail.next = None # type: ignore
            popped_node.prev = None # type: ignore
        self.length -= 1
        return popped_node

    def remove(self, index):
        popped_node = self.get(index)
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        popped_node.prev.next = popped_node.next # type: ignore
        popped_node.next.prev = popped_node.prev # type: ignore
        popped_node.next = None # type: ignore
        popped_node.prev = None # type: ignore
        self.length -= 1
        return popped_node
    


newDLL = DoublyLinkedList()
newDLL.append(10)
newDLL.append(20)
newDLL.append(30)
newDLL.append(40)
newDLL.append(50)
newDLL.prepend(100)
print(newDLL)
# newDLL.reverse_traverse()
print(newDLL.search(50))