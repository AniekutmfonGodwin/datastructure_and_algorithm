from typing import Any, Dict, List, Union



def missing_number_in_array(array:List[int]):
    maximum = max(array)
    minimum = min(array)
    total = sum(range(minimum,maximum+1))
    return total - sum(array)


def find_missing(input):
  # calculate sum of all elements 
  # in input list
  sum_of_elements = sum(input)
  
  # There is exactly 1 number missing 
  n = len(input) + 1
  actual_sum = (n * ( n + 1 ) ) // 2 # fomular uses arithmetic progression
  return actual_sum - sum_of_elements



def find_sum_of_two(A, val):
    #TODO: Write - Your - Code
    for x in A:
        check = val - x
        
        if check in A and check !=x:
            return True
    return False


# find_sum_of_two([5, 7, 1, 2, 8, 4, 3],2)

def compress_image(array:Union[List[str],str]) -> str:
    """function to compress string 

    Args:
        array (Union[List[str],str]): _description_

    Returns:
        str: _description_
    """

    result = str()
    data = list()

    for char in array:
        if not data:
            data = [char,1]
        elif data and char in data:
            # this means the char in the dict is the same char
            data[1] += 1

        elif data and char not in data:
            result +=str(data[1]) + data[0]
            data = [char,1]
    if data:
        result += str(data[1]) + data[0]
        data = list()
    return result

# compress_image("aabbccddeavaddrr")

def decompress(data:str)->str:
    """function to decompress a string

    Args:
        data (str): _description_

    Returns:
        str: _description_
    """
    result = str()
    count = 0
    
    for item in data:
        item:str
        if item.isnumeric():
            count = int(item)
        else:
            result +="".join([item for _ in range(count)])
            count = 0
        

    return result

# print("result ",decompress("2a3b1s1f3r"))


def two_sum(array,val):
    data = set(array)
    for number in data:
        check = val - number
        if check in data and check != number:
            return True
    
    return False





def ratio_of_numbers(array):
    
    numbers = dict()

    for number in array:
        if numbers.get(str(number)):
            numbers[str(number)] +=1
        else:
            numbers[str(number)] = 1

    for value in numbers.values():
        print("{0:.4f}".format(value/len(array)))
    

# ratio_of_numbers([-4,3,-9,0,4,1])



def hex2rgb(color:str):
    """function convert from HEX color code to RGB

    Args:
        color (str): _description_

    Returns:
        _type_: _description_
    """
    color = color.lstrip("#")
    res = [str(int(color[i:i+2],16)) for i in range(0,len(color),2)]
    return "rgb({0})".format(", ".join(res))


# print("rgb value =",hex2rgb("#FFA501"))


def rgb2hex(r:int,g:int,b:int)->str:
    """convert from rgb color code to hex color code

    Args:
        r (int): _description_
        g (int): _description_
        b (int): _description_

    Returns:
        str: _description_
    """
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))



# print("rgb to hex = ",rgb2hex(-20,275,125))


#chain add function
class add(int):
    def __call__(self, n):
        return add(self + n)



class add2(object):
    """implementing all the magic method for number operation

    Args:
        object (_type_): _description_
    """
    def __init__(self, n):
        self.value = n

    def __add__(self, n):
        return add2(self.value + n)
        
    def __sub__(self, n):
        return add2(self.value - n)
        
    def __call__(self, n):
        return add2(self.value + n)
        
    def __eq__(self, other):
        if isinstance(other, add2):
            return self.value == other.value
        else:
            return self.value == other



import math


class Sudoku(object):
    """
    Given a Sudoku data structure with size NxN, N > 0 and √N == integer, write a method to validate if it has been filled out correctly.

    The data structure is a multi-dimensional Array, i.e:

    [
    [7,8,4,  1,5,9,  3,2,6],
    [5,3,9,  6,7,2,  8,4,1],
    [6,1,2,  4,3,8,  7,5,9],
    
    [9,2,8,  7,1,5,  4,6,3],
    [3,5,7,  8,4,6,  1,9,2],
    [4,6,1,  9,2,3,  5,8,7],
    
    [8,7,6,  3,9,4,  2,1,5],
    [2,4,3,  5,6,1,  9,7,8],
    [1,9,5,  2,8,7,  6,3,4]
    ]
    Rules for validation

    Data structure dimension: NxN where N > 0 and √N == integer
    Rows may only contain integers: 1..N (N included)
    Columns may only contain integers: 1..N (N included)
    'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)
    """

    def __init__(self, board):
        self.board = board
        
    def is_valid(self):
        if not isinstance(self.board, list):
            return False
        n = len(self.board)
        rootN = int(round(math.sqrt(n)))
        if rootN * rootN != n:
            return False
        isValidRow = lambda r : (isinstance(r, list) and
                                 len(r) == n and
                                 all(map(lambda x : type(x) == int, r)))
        if not all(map(isValidRow, self.board)):
            return False
        oneToN = set(range(1, n + 1))
        isOneToN = lambda l : set(l) == oneToN
        tranpose = [[self.board[j][i] for i in range(n)] for j in range(n)]
        squares = [[self.board[p+x][q+y] for x in range(rootN) 
                                         for y in range(rootN)] 
                                         for p in range(0, n, rootN)
                                         for q in range(0, n, rootN)] 
        return (all(map(isOneToN, self.board)) and
                all(map(isOneToN, tranpose)) and
                all(map(isOneToN, squares)))

# print(Sudoku([
#   [[0, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
# ]).is_valid())

# print("001".isdigit())

import re


"""
DESCRIPTION:
In this kata, your task is to create a regular expression capable of evaluating binary strings (strings with only 1s and 0s) and determining whether the given string represents a number divisible by 3.

Take into account that:

An empty string might be evaluated to true (it's not going to be tested, so you don't need to worry about it - unless you want)
The input should consist only of binary digits - no spaces, other digits, alphanumeric characters, etc.
There might be leading 0s.
Examples (Javascript)
multipleof3Regex.test('000') should be true
multipleof3Regex.test('001') should be false
multipleof3Regex.test('011') should be true
multipleof3Regex.test('110') should be true
multipleof3Regex.test(' abc ') should be false
You can check more in the example test cases

Note
There's a way to develop an automata (FSM) that evaluates if strings representing numbers in a given base are divisible by a given number. You might want to check an example of an automata for doing this same particular task here.

If you want to understand better the inner principles behind it, you might want to study how to get the modulo of an arbitrarily large number taking one digit at a time.
"""
PATTERN = re.compile(r'^(0|1(01*0)*1)*$')


def get_first_occurance(array:List[Any],value):
    """get the last occurance of an element 

    Args:
        array (List[Any]): _description_
        value (_type_): _description_

    Returns:
        _type_: _description_
    """
    if value not in array:
        return -1
    return array.index(value)


def get_last_occurance(array:List[Any],value):
    """get the last occurance of an element

    Args:
        array (List[Any]): _description_
        value (_type_): _description_

    Returns:
        _type_: _description_
    """
    array.reverse()
    if value not in array:
        return -1
    
    index = array.index(value)
    return len(array) -1 - index



def get_index_of_element_binary_search(array:List[Any],element:Any,low:int,high:int):
    """find and index of an element using binary search

    Args:
        array (List[Any]): _description_
        element (Any): _description_
        low (int): _description_
        high (int): _description_

    Returns:
        _type_: _description_
    """
    if not array or low>high  or not element  or low==high or len(array)-1<high:
        return -1
    else:
        mid = (low + high)//2
        if array[mid] == element:
            return mid
        elif mid>element:
            return get_index_of_element_binary_search(array,element,low,mid -1)
        else:
            return get_index_of_element_binary_search(array,element,mid+1,high)


def get_first_index_of_element_binary_search(array:List[Any],element:Any,low:int,high:int):
    """find and index of an element using binary search

    Args:
        array (List[Any]): _description_
        element (Any): _description_
        low (int): _description_
        high (int): _description_

    Returns:
        _type_: _description_
    """
    if not array or low>high  or not element or len(array)-1<high:
        return -1
    else:
        mid = (low + high)//2
        if array[mid] == element:
            if mid != 0 and array[mid-1] != element:
                print("\ngotta you \n")
                return mid
            else:
                print("\nmoving left not first occurrence ",low," - ",mid-1,"\n")
                return get_first_index_of_element_binary_search(array,element,low,mid -1)
        elif array[mid]>element:
            print("\nmoving left ",low," - ",mid-1,"\n")
            return get_first_index_of_element_binary_search(array,element,low,mid -1)
        else:
            print("\nmoving right ",mid+1," - ",high,"\n")
            return get_first_index_of_element_binary_search(array,element,mid+1,high)

def get_last_index_of_element_binary_search(array:List[Any],element:Any,low:int,high:int):
    """find and index of an element using binary search

    Args:
        array (List[Any]): _description_
        element (Any): _description_
        low (int): _description_
        high (int): _description_

    Returns:
        _type_: _description_
    """
    if not array or low>high  or not element or len(array)-1<high:
        return -1
    else:
        mid = (low + high)//2
        if array[mid] == element:
            if mid != len(array)-1 and array[mid+1] != element:
                print("\ngotta you \n")
                return mid
            else:
                print("\nmoving right not last occurence ",mid+1," - ",high,"\n")
            return get_first_index_of_element_binary_search(array,element,mid+1,high)
        elif array[mid]>element:
            print("\nmoving left ",low," - ",mid-1,"\n")
            return get_first_index_of_element_binary_search(array,element,low,mid -1)
        else:
            print("\nmoving right ",mid+1," - ",high,"\n")
            return get_first_index_of_element_binary_search(array,element,mid+1,high)



def strong_password_checker(password):
    if password <6 or password > 20:
        return False

    uppercase = []
    lowercase = []
    digit = []

    for char in password:
        char:str
        if char.isupper():
            uppercase.append(char)
        elif char.islower():
            lowercase.append(char)
        elif char.isdigit():
            digit.append(char)
    if not all([uppercase,lowercase,digit]):
        return False

    return True


def balance_bracket(data:str):

    stack = []
    try:
        for char in data:
            if char in ["(","[","{"]:
                stack.append(char)
            else:
                if not stack:
                    return False
                last_char = stack.pop()
                if last_char == "(" and char != ")":
                    return False
                if last_char == "[" and char != "]":
                    return False
                if last_char == "{" and char != "}":
                    return False
        if stack:
            return False
        else:
            return True
    except IndexError:
        return False


# print("perfect ",balance_bracket("()()({{{)}}}"))


def next_greatest(arr):
    #code here
    output = []
    last_element = arr[-1]
    
    for number in arr:
        print("first loop ",number," output ",output)
        if number == last_element:
            output.append(-1)
            break
        found = False
        for element in arr[arr.index(number)+1:]:
            print("second loop ",element," output ",output)
            if element > number:
                output.append(element)
                found = True
                break

        if not found:
            output.append(-1)
        
    return output

print(next_greatest([1, 3, 2, 4]))
# 3 4 4 -1