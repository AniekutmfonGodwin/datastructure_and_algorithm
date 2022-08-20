
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

print("array ",max_for_contegent_arr([2,5,3,7,6,4,8],3))

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
