


from turtle import left
from typing import Union


class NodeInterface:
    def __init__(self,value,left=None,right=None) -> None:
        """node interface

        Args:
            value (Union[int,float]): node value
            left (Union[NodeInterface,None], optional): node left child. Defaults to None.
            right (Union[NodeInterface,None], optional): node right child. Defaults to None.
        """
        self._left_child,self._right_child,self.value = left,right,value


    def left(self):
        """left node child
        """
        ...

    def right(self):
        """node right child
        """
        ...


class Node:
    def __init__(self,value,left=None,right=None) -> None:
        """class for creating a single node

        Args:
            value (Union[float,int]): node data
            left (Union[Node,None], optional): node left child. Defaults to None.
            right (Union[Node,None], optional): node right child. Defaults to None.

        Raises:
            ValueError: _description_
        """
        if left and type(left) != Node or right and type(right) != Node:
            raise ValueError("value must be of type Node")
        self._left_child,self._right_child,self.value = left,right,value

    @property
    def left(self):
        """node left child

        Returns:
            Node: return Node instance
        """
        return self._left_child

    @property
    def right(self):
        """node right child

        Returns:
            Node: return Node instance
        """
        return self._right_child

    @left.setter
    def left(self,value:Union[NodeInterface,int,str]):
        """left node setter method for setting left node

        Args:
            value (Union[NodeInterface,int,str]): _description_

        Raises:
            ValueError: if value is not an allowed type throw an error
        """
        if type(value) != Node:
            raise ValueError("value must be of type NodeInterface")
        self._left_child = value

    @right.setter
    def right(self,value:Union[NodeInterface,int,str]):
        """right node setter method for setting right node

        Args:
            value (Union[NodeInterface,int,str]): _description_

        Raises:
            ValueError: if value is not an allowed type throw an error
        """
        if type(value) != Node:
            raise ValueError("value must be of type NodeInterface")
        self._right_child = value

    def __add__(self,value:NodeInterface):
        main_value = self.value+value.value
        left_value = self.left+value.left if all([self.left,value.left]) else self.left or value.left
        right_value = self.right+value.right if all([self.right,value.right]) else self.right or value.right
        return Node(main_value,left_value,right_value)

    def __sub__(self,value:NodeInterface):
        main_value = self.value-value.value
        left_value = self.left-value.left if all([self.left,value.left]) else self.left or value.left
        right_value = self.right-value.right if all([self.right,value.right]) else self.right or value.right
        return Node(main_value,left_value,right_value)

    def __repr__(self) -> str:
        return str(self.value)



def set_node_value(node:Node,value:int) -> Node:
    """function to set a node at the appropriate position using binary search
    * `list 1`
    * list 2
    # her

            print("hello world")
    # this is it
    
    Args:
        node (Node): root node instance
        value (int): value for the new node

    Returns:
        Node: return node instance
    """
    if not node:
        return node
    if value>node.value:
        if not node.right:
            node.right = Node(value)
            return node
        else:
            return set_node_value(node.right,value)
    elif value<node.value:
        if not node.left:
            node.left = Node(value)
            return node
        else:
            return set_node_value(node.left,value)
    
    
    else:
        return node
    
    
node1 = Node(30,Node(30),Node(1))
node2 = Node(30,Node(30),Node(1))

node = node1+node2