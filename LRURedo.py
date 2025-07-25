from collections import OrderedDict

class DoubleLinkedNode:
    def __init__(self,key=0,value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    

class LRU:
    dict = {int: DoubleLinkedNode}
    size = 0
    capacity = 0
    def __init__(self,capacity:int):
        self.capacity = capacity
        self.head = DoubleLinkedNode()
        self.tail = DoubleLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dict = {}
    def add_node(self,node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove(self,node: DoubleLinkedNode):
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev
        return node

    def move_to_front(self,key:int, node: DoubleLinkedNode):
        self.remove(node)
        self.add_node(node)
        # if key in self.dict:
        #     rmv = self.remove(node.key, node)
        #     self.head.next.prev = rmv
        #     rmv.next = self.head.next
        #     self.head.next = rmv
        #     rmv.prev = self.head
        # else:
        #     node.next = self.head.next
        #     self.head.next.prev = node
        #     self.head.next = node
    def popTail(self):
        res = self.tail.prev
        self.remove(res)
        return res

    def get(self, key:int):
        node = self.dict[key]
        if not node:
            return -1
        self.move_to_front(key,node)
        return node.value
    
    def put(self,key:int,value):
        node = self.dict.get(key, None)
        if not node:
            new = DoubleLinkedNode(key,value)
            self.dict[key] = new
            self.add_node(new)
            self.size +=1
            if self.size > self.capacity:
                tail = self.poptail()
                del self.dict[tail.key]
                self.size -=1
      
        else:
            node.value = value
            self.move_to_front(node)

            

        
    
