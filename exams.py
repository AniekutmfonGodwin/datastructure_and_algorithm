
from typing import Any, List


from compute_time import compute_time




def find_sum_of_two(A, val):
    """O(n)

    Args:
        A (_type_): _description_
        val (_type_): _description_

    Returns:
        _type_: _description_
    """
    for item in A:
        diff = val - item
        if diff in A and diff != item:
            return True
    return False


# def merge_sorted(head1, head2):
#   return sorted(head1 + head2)
def merge_sorted(head1, head2):
    new_array = list()
    for x,y in head1,head2:
        new_array


def check_if_opening_and_closing_match(brackets:str):
    stack = list()

    for char in brackets:

        if char == "(":
            stack.append(char)
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    
    return not stack




class Add:

    def __init__(self,value) -> None:
        self.value = value


    def __call__(self,value:Any) -> Any:
        return self + value

    def __add__(self,value):
        return Add(self.value + value)

    def __sub__(self,value):
        return Add(self.value - value)

    def __repr__(self) -> str:
        return str(self.value)



a = [1,2,3,[2,3]]


def flatten(a:List[Any]):

    if type(a)!=list:
        return str
    else:
        return [str if type(x) !=list else flatten(x) for x in a]



def CountWays(n):
 
    # table[i] will be storing the number of
    # solutions for value i. We need n+1 rows
    # as the table is constructed in bottom up
    # manner using the base case (n = 0)
    # Initialize all table values as 0
    table =[0] * (n + 1)
 
    # Base case (If given value is 0)
    # Only 1 way to get 0 (select no integer)
    table[0] = 1
    print(table)
    # Pick all integer one by one and update the
    # table[] values after the index greater
    # than or equal to n
    for i in range(1, n ):
 
        for j in range(i , n + 1):
 
            table[j] +=  table[j - i]  
            print(table,"n",n)
                 
 
    return table[n]



# stack = LifoQueue()

# stack.put(1)
# stack.put(2)
# stack.put(3)
# stack.put(4)
# stack.put(5)

# stack.queue[-1]

class stack(list):

    def top(self):
        return self[-1]

    def peek(self):
        return self.top()

    def push(self,value):
        self.append(value)
        return self

    def pop(self):
        return super().pop()

    def empty(self):
        return not self

    def size(self):
        return len(self)



def right_or_left(arr,low,high,number):
    if low > high:
        return -1
    mid = (low + high)//2
    mid_element = arr[mid]
    if mid_element == number:
        return mid
    elif mid_element>number:
        return right_or_left(arr,low,mid - 1,number)
    else:
        return right_or_left(arr,mid+1,high,number)



def binary_search(arr,number):
    """O(log n)

    Args:
        arr (_type_): _description_
        number (_type_): _description_

    Returns:
        _type_: _description_
    """
    low,high = 0,len(arr)-1
    return right_or_left(arr,low,high,number)

# print("binary search ",binary_search([1,2,3,4,5,6,7]))



"""
n = 14

2 x 7

7 x 2



"""



def is_prime(n:int):
    if n == 1:
        return False

    count = 2

    while count*count <=n:
        if n%count == 0:
            return False
        count +=1
    return True


def max_for_contegent_arr(arr,k):
    res = list()
    for i in range(len(arr)):
        tem = arr[i:i+k]
        if len(tem) < 3:
            break
        res.append(max(tem))
    print(res)
    return res

# print("array ",max_for_contegent_arr([2,5,3,7,6,4,8],3))

def merge_sorted(head1, head2):
    
    res = []

    while True:
        
        if (not head2 and head1):
            res.append(head1)
            head1 = head1.next

        if (not head1 and head2):
            res.append(head2)
            head2 = head2.next

        if head2 and head1:
            if head2.data > head1.data:
                res.append(head1)
                head1 = head1.next
            else:
                res.append(head2)
                head2 = head2.next

        

        if not head1 and not head2:
            break

        
            
    head = res[0]
    
    for index,node in enumerate(res):
        if index == len(res) -1:
            node.next = None
        else:
            node.next = res[index+1] 

    return head

# def number_of_iland():



def format_paragraph(paragraphs,width):
    results = []

    for i,items in enumerate(paragraphs):
        line = " ".join(items)
        if len(line) > width:
            inner = ""
            for item in items:
                if len(inner+item)>width:
                    if inner!="":
                        results.append(inner)
                        inner = ""
                else:
                    inner +=" "+item
            if inner:
                results.append(inner)

        else:
            results.append(line)

    return results


# print(format_paragraph([
#     ["hello","world"],
#     ["how","areYou","doing"],
#     ["please look","and align","to center"]
# ],16))


def get_median_of_metrix(m):
    result = list()


    for row in m:
        for column in row:
            result.append(column)

    

    result.sort()
    if len(result)%2==0:
        mid = (len(result)-1)//2
        return (result[mid] + result[mid+1])//2
    else:
        mid = (len(result)-1)//2
        return result[mid]

    


# print("median of a matrix ",get_median_of_metrix([
#     [1,2,3],
#     [4,5,6],
#     [6,7,8]
# ]))







class Tree:

    def __init__(self,data=None,left = None,right = None) -> None:
        self.left = left
        self.right = right
        self.data = data


    

def printInOrder(node:Tree):


    if node:

        printInOrder(node.left)

        print(node.data)

        printInOrder(node.right)


def findMaxHeight(node):

    if node is None:
        return 0

    lh = findMaxHeight(node.left)
    rh = findMaxHeight(node.right)

    if lh > rh:
        return 1 + lh
    return 1 + rh

def printInOrderUsingStack(node:Tree):

    stack = [node]

    while stack:
        temp_node:Tree = stack.pop()
        print(temp_node.data)
        if temp_node.right:
            stack.append(temp_node.right)
        if temp_node.left:
            stack.append(temp_node.left)



node = Tree(
    data=10,
    left=Tree(
        data = 20,
        left=Tree(
            data=30
        )
    ),
    right=Tree(
        data = 33,
        left = Tree(
            data = 50
        )
    )
)


printInOrderUsingStack(node)



# mirror tree

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        # Code here
        if root is None:
            return
        
        temp = root
        self.mirror(root.left)
        self.mirror(root.right)
        
        temp=root.left
        root.left=root.right
        root.right=temp





a = [1,2,3]
print("a ref ",id(a))

b = [1,2,3]
print("b ref ",id(b))

a,b = b,a

print("a ref ",id(a))

print("b ref ",id(b))



def height(root:Tree):

    if root is None:
        return 0

    lh = height(root.left)
    rh = height(root.right)

    if lh > rh:
        return 1 + height(root.left)

    return 1 + height(root.right)


# print(" node ",height(node))




def reverse_string(string:str):

    if not string:
        return ''

    return string[-1] + reverse_string(string[:-1])



def sort_recur(arr:list):

    if not arr:
        return []
    mi = min(arr)
    arr.remove(mi)
    return [mi] + sort_recur(arr)

a = [2,3,1,5,6,2,1]

# print("sorted array ",sort_recur(a))



def find_min(arr):

    start_pointer = 0
    end_pointer = len(arr) -1
    mi = float("inf")

    while start_pointer < end_pointer:
        
        if arr[end_pointer] < mi:
            mi = arr[end_pointer]
            end_pointer -=1
        else:
            mi = arr[start_pointer]
            start_pointer +=1

    print("min ",mi)
    return mi


print("find min ",find_min([2,4,2,3,6]))



def palindrom_check(string,start,end):

    if start > end:
        return True

    if string[start] == string[end]:
        return True and palindrom_check(string,start+1,end-1)

    return False



string = "racecar"

start = 0
end = len(string) -1

print("palindrom check ",palindrom_check(string,start,end))

        


    
    



# print("reverse string ",reverse_string("hello world"))



def decimal_to_binary(number):

    if number == 0:
        return ""
    
    res = number//2
    rem = number%2
    return  decimal_to_binary(res) + str(rem)



# print("binary number ",decimal_to_binary(20))


def target_exists(node:Tree,target):
    if node is None:
        return False
    stack = [node]


    while stack:
        current = stack.pop(0)
        if current.data == target:
            return True

        if current.left:
            stack.append(current.left)

        if current.right:
            stack.append(current.right)

    return False


# print("target exists ",target_exists(node,100))



def tree_sum(node:Tree):
    
    if node is None:
        return 0


    return node.data + tree_sum(node.left) + tree_sum(node.right)


# print("sum ",tree_sum(node))

mi = float("inf")

def min_of_tree(node:Tree):
    global mi
    if node is None:
        return float("inf")
    
    if node.data < mi:
        mi = node.data

    min_of_tree(node.left)
    min_of_tree(node.right)


# min_of_tree(node)

# print("mi ",mi)



def first_duplicate(arr,index=0):

    if not arr:
        return -1

    if arr[index] in arr[:index]:
        return arr[index]

    return first_duplicate(arr,index+1)


# print(" dd",first_duplicate([1,2,3,4,5,6,2,7,5]))


def flippingMatrix(matrix):
    # Write your code here
    result = 0
    for i in range(n):
        for j in range(n):
            list = [matrix[i][j],matrix[i][2*n-1-j],matrix[2*n-1-i][j],matrix[2*n-1-i][2*n-1-j]]
            result +=max(list)
    return result
