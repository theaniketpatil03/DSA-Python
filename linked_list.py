class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next



# class LinkedList:
#     def __init__(self) -> None:
#         self.head = None

#     def append_beg(self, data):
#         node = Node(data, self.head)
#         self.head = node
#     def append_end(self, data):
#         node = Node(data)

#         current = self.head

class LinkedList:
    def __init__(self) -> None:
        self.head = Node()

    def append(self, data):
        current = self.head

        while current.next != None:
            current = current.next

        current.next = Node(data)
    
    def append_start(self, data):

        new_node = Node(data, self.head.next)

        self.head.next = new_node

    def display(self):

        current =  self.head
        display_list = []
        while current.next != None:
            
            current = current.next
            display_list.append(current.data)
        
        return display_list
    
    def insert_all(self, data_list):
        for data in data_list:
            self.append(data)

    def insert_all_start(self, data_list):
        for data in data_list:
            self.append_start(data)

    def get_length(self):
        length = 0

        current = self.head

        while current.next != None:
        
            current = current.next
            length += 1

        return length


    def remove_at(self, index):
        
        if index < 0 or index >= self.get_length():
            raise Exception('Invalide index')

        if index == 0:
            self.head.next  = self.head.next.next
            return 
        
        current = self.head
        for _ in range(index):
            current = current.next

        current.next =  current.next.next

        return
    
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalide index')

        if index == 0:
            self.head.next  = Node(data, self.head.next)
            return 

        current = self.head
        for _ in range(index):
            current = current.next

        current.next =  Node(data, current.next)

        return
    

    def insert_after_value(self, data_after, data_to_insert):
        pass
    
    def remove_by_value(self, data):
        pass



l1 = LinkedList()

l1.append(1)
l1.append(2)
l1.append_start(0)
l1.insert_all([3, 4, 5])
l1.insert_all_start([-1, -2, -3])
l1.remove_at(5)
print(l1.display())
l1.insert_at(2, 9)
print(l1.display())
print(l1.get_length())