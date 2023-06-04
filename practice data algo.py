class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class lisklist:
    def __init__(self):
        self.head = None

    def insert_at_begginning(self, data):
        new_node  = Node(data,self.head)
        self.head = new_node

    def printlinklist(self):
        if(self.head ==None):
            print("Empty list")
        lisklist = ""
        iterator = self.head
        while iterator:
            lisklist = lisklist + str(iterator.data) + "-------->"
            iterator = iterator.next
        return lisklist

    def insert_end(self, data):
        if(self.head is None):
            self.head = Node(data, None)
        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        iterator.next = Node(data,None)

    def size(self):
        count  = 0
        iterator = self.head
        while iterator:
            count = count +1
            iterator = iterator.next
        return count

    def remove_index(self, index):
        if (index<0 or index>=self.size()):
            print("that index not in list")
            return
        if index == 0:
            self.head = self.head.next
        count = 0
        iterator = self.head
        while iterator:
            if (count == index-1):
                iterator.next = iterator.next.next
                break
            iterator = iterator.next
            count = count +1

    def insert_middle(self,index, data):
        if( index<0 or index>=self.size()):
            print("that type of index not in list")
        if index == 0:
            self.head = self.insert_at_begginning(data)

        count = 0
        iterator = self.head
        while iterator:
            if(count == index-1):
                new_node = Node(data,iterator.next)
                iterator.next = new_node
                break
            iterator = iterator.next
            count+=1


l1 = lisklist()
l1.insert_at_begginning(10)
l1.insert_at_begginning(20)
l1.insert_at_begginning(30)
l1.insert_at_begginning(40)
print(l1.printlinklist())
l1.insert_end(200)
print(l1.printlinklist())
print(l1.size())
l1.remove_index(1)
print(l1.printlinklist())
l1.insert_middle(3,400)
print(l1.printlinklist())

