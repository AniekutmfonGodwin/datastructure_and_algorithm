

from typing import Any, Optional, Union


class NodeInterface:
    data:Any
    next:Optional[Union[None,object]] = None
    


class Node:
    def __init__(self,data,next:NodeInterface=None) -> None:
        self.data = data
        self.next = next


    def __repr__(self) -> str:
        if self.next:
            return "[ {} ]".format(self.data) +"->"+ str(self.next)
        return "[ {} ]".format(self.data)





class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def push(self,data:Any):
        """add a node at the beginning of a node

        Args:
            data (Any): _description_
        """
        new_node = Node(data)
        self.head,new_node.next = new_node,self.head

    def insertAfter(self,prev_node:NodeInterface,new_data):
        """insert a new node after a particular node

        Args:
            prev_node (NodeInterface): _description_
            new_data (_type_): _description_
        """
        if prev_node is None:
            print("prev_node does not exists")
            return 
        
        new_node = Node(new_data)

        new_node.next,prev_node.next = prev_node.next,new_node
        print(self)

    def append(self,data:Any):
        """add a new node to the end

        Args:
            data (Any): _description_
        """
        if self.head is None:
            self.head = Node(data)
            return 

        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(data)
        print(self)

    def deleteStart(self):
        """delete first node
        """
        if self.head is None:
            print("linked list is empty")
            return 
        
        self.head = self.head.next
        print(self)


    def deleteEnd(self):
        """delete the last node
        """
        if self.head is None:
            print("linked list is empty")
            return 
        
        current_node = self.head
        prev_node = None
        while current_node.next:
            prev_node,current_node = current_node,current_node.next

        if self.head == prev_node or not prev_node:
            self.head = None

        else:
            prev_node.next = None

        print(self)
        
    def deleteNode(self,key):
        
        if self.head is None:
            print("linked list is empty")
            return 
        current_node,prev_node = self.head,None
        prev_node:Node
        while current_node.next:
            if current_node.data == key:
                if  prev_node:
                    prev_node.next=current_node = current_node.next
                    continue
                    
                elif not prev_node and current_node.next:
                    self.head =current_node =  current_node.next
                    continue
            
            prev_node,current_node = current_node,current_node.next

        if not current_node.next and current_node.data == key and prev_node:
            prev_node.next = current_node = None
            
        print(self)

    def deleteIndex(self,index):

        if self.head is None:
            print("linked list is empty")
            return 

        if index == 0:
            self.head = self.head.next
        else:
            current_node,prev_node = self.head,None
            for _ in range(index):
                prev_node,current_node = current_node,current_node.next
                if not current_node.next:
                    print(self)
                    return

            if current_node and prev_node:
                prev_node.next = current_node.next

        print(self)
        
            
    def is_a_loop(self):
        """check if a linked list is a loop

        Returns:
            _type_: _description_
        """
        if self.head is None:
            print("linked list is empty")


        visited = set()
        current = self.head
        while current:
            if current in visited:
                return True

            else:
                visited.add(current)

            current = current.next

        return False 
            
            
    def remove_duplicate(self):
        values = set()
        current:Node = self.head
        if not current:
            return
        prev_node:Node = None
        
        while current:
            if current.data in values:
                prev_node.next = current.next
            else:
                values.add(current.data)
            prev_node,current = current,current.next

            


    
    def __repr__(self) -> str:
        if self.head:
            return "#" +"."+ str(self.head)
        return "#"
        

def mergeLinkedList(headA:Node,headB:Node):
    """merge 2 linked list together

    Args:
        headA (Node): _description_
        headB (Node): _description_

    Returns:
        LinkedList: _description_
    """
    dummyNode = Node(0)
    tail = dummyNode

    while True:

        if headA is None:
            tail.next = headB
            break
        if headB is None:
            tail.next = headA
            break

        if headA.data <= headB.data:
            tail.next,headA = headA,headA.next
        else:
            tail.next,headB = headB,headB.next

        tail = tail.next

    return dummyNode.next



def linkedListIsPalindrome(head:Node):
    stack = []
    


    while head:


        if head:
            stack.append(head.data)
            head = head.next

    
    main = stack.copy()
    if main == stack:
        print("is a palindrome")
    else:
        print("is not a palindrome")
    return main == stack



def reverse_linked_list(head:Node):
    """reverse linked list

    Args:
        head (Node): _description_

    Returns:
        _type_: _description_
    """

    if head is None:
        return head

    main:Node = Node(head.data)
    

    head = head.next
    

    while head:

        
        new_node = Node(head.data)
        new_node.next,main = main,new_node
        
        
        head = head.next

    return main


    


linked_list = LinkedList()

linked_list.head = Node(22,Node(23,Node(33,Node(22,Node(2)))))

main = Node(22,Node(23,Node(33,Node(22,Node(2)))))
print("main ",main)


def reverse_a_link_list_without_createing_new(main:Node):
    if not main :return main

    data = [main]

    while main.next:
        data.append(main.next)
        main = main.next

    new_node = None

    for node in data:
        node:Node
        node.next = new_node
        new_node = node

    print("new node",new_node)

    return new_node

reverse_a_link_list_without_createing_new(main)



# linked_list.head = Node(22)
# linked_list.head.next.next = linked_list.head #make linked list a loop
# linked_list.remove_duplicate()
# print(linked_list)
# linked_list.insertAfter(linked_list.head.next,20)
# linked_list.append(20)
# linked_list.append(3330)

# print("linked list is a loop",linked_list.is_a_loop())
# linked_list.deleteStart()
# linked_list.deleteEnd()

# linked_list.deleteIndex(2)
# linked_list.deleteNode(22)




# merge 2 linked list

# linked_list1,linked_list2 = LinkedList(),LinkedList()

# linked_list1.head = Node(1,Node(3,Node(10)))
# linked_list2.head = Node(2,Node(4,Node(5)))


# print("merged list ",mergeLinkedList(linked_list1.head,linked_list2.head))
    


# # test for palindrome
# linked_list = LinkedList()

# linked_list.head = Node(4,Node(1,Node(1,Node(4))))

# print("merged list ",linkedListIsPalindrome(linked_list.head))


# reverse linked list

# print("reverse list ",reverse_linked_list(Node(1,Node(2,Node(3,Node(4,Node(20)))))))



