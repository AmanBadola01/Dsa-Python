class Node:
    def __init__(self, value):
        self.value = value 
        self.next : Node 

class CSLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        new_node.next = new_node
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def __str__(self):
        temp_node = self.head
        result = ''

        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += ' -> '
        return result
    
    def append(self, value): #Adding node at the end
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node# type: ignore
            new_node.next = self.head# type: ignore
            self.tail = new_node
        self.length += 1
        return True
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head # type: ignore
            self.head = new_node
            self.tail.next = new_node# type: ignore
        self.length += 1
        return True
    
    def insert(self, value, index):
        new_node = Node(value)
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        elif index > (self.length + 1) or index < 0:
            raise Exception("Index out of rage.")
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next # type: ignore
            new_node.next = temp.next  # type: ignore
            temp.next = new_node # pyright: ignore[reportOptionalMemberAccess]
        self.length += 1
        return True
    
    def traversal(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            if temp == self.head:
                break

    def search(self, target_value):
        current = self.head
        while current is not None:
            if target_value == current:
                return True
            current = current.next
            if current == self.head:
                break
        return False
    
    def get(self, index):
        if index == 0:
            return self.head.value # type: ignore
        elif index == self.length -1:
            return self.tail.value# type: ignore
        elif index >= self.length or index < 0:
            raise Exception("Index out of range.")
        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next # type: ignore
        return temp_node.value # type: ignore
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        if self.length == 0:
            return None
        
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0

        else:
            temp_node = self.head
            self.head = self.head.next # type: ignore
            self.tail.next = self.head # type: ignore
            temp_node.next = None # type: ignore
            self.length -= 1
        return temp_node
    
    def pop(self):
        popped_node = self.tail
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp_node = self.head
            while temp_node.next is not  self.tail:# type: ignore
                temp_node = temp_node.next # type: ignore
            self.tail = temp_node
            temp_node.next = self.head # type: ignore 
            popped_node.next = None # type: ignore
        self.length -= 1
        return popped_node

    def remove(self, index):
        if index == 0:
            return self.pop_first()
        elif index == self.length -1:
            return self.pop()
        elif index < 0 or index >= self.length:
            return None
        else:
            prev_node = self.get(index-1)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def delete_all(self):
        if self.length == 0 :
            return 
        self.tail.next = None  # type: ignore
        self.head = None
        self.tail = None
        self.length = 0





csl = CSLinkedList(10)
csl.append(20)
csl.append(30)
csl.append(40)
print(csl)
# csl.traversal()
# print(csl.search(10))
# print(csl.get(0))
# csl.set_value(-1,200)
csl.delete_all()
print(csl)
# print(csl.tai) # type: ignore