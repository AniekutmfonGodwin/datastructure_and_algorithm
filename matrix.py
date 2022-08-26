
import string as strinner
from collections import OrderedDict
from unittest import result

class Matrix:

    def __init__(self,array) -> None:
        self.row_count = len(array)
        self.column_count = 0
        self.array = array
        tem = set()

        for arr in self.array:
            tem.add(len(arr))


        if len(tem) > 1:
            raise Exception("column length are unequal")
        self.column_count = tem.pop()

    def __repr__(self) -> str:
        res = "\n{} X {} matrix\n\n".format(self.column_count,self.row_count,)
        for arr in self.array:
            res +=str(arr)+"\n"

        return res

    def rotate_right_90(self):
        empty = self.generate_empty_matrix(self.column_count,self.row_count)

        for r in range(self.row_count):

            for c in range(self.column_count):
                # print("{},{} = {}".format(r,c,self.array[r][c]))
                empty[c][r] = self.array[r][c]

        for r in empty:
            r:list = r
            r.sort(reverse=True)
            print(r)

        return empty

    def generate_empty_matrix(self,row:int,column:int):
        result = list()
        for _ in range(row):
            result.append([0 for _ in range(column)])

        return result
    

    def insert(self,row_index,column_index,data):
        
        self.array[row_index][column_index] = data
        print(self)
        
    
    
# matrix  = Matrix([
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
# ])
# print(matrix)
# print("insert ",matrix.insert(0,1,10))
# print("insert ",matrix.insert(1,1,10))
# print("rotate right ",matrix.rotate_right_90())

# recursive Python Program to copy one String
# to another.

# Function to copy one string to other


def copy_str(x, y):
	if len(y) == 0:
		return x
	else:
		c = copy_str(x, (y)[1:-1])
		return c


# x = input("enter the value for x: ")
# y = input("enter a value for y: ")
# print(copy_str(x, y))

# This code contributed by deeksha20049@iiid.ac.in

def is_true(string:str):
    unique = set(string.lower().replace(" ",''))
    return len(unique) == 26

def is_true2(string:str):
    unique = set([ x for x in string.lower() if x in strinner.ascii_lowercase])
    return len(unique) == 26

# sentence = "The quick brown fox jumps over the little lazy dog"
sentence = "ddfgh hhgtdd"
# print("pangram ",is_true(sentence))

def check_difference(sentence:str):
    return "".join(set(strinner.ascii_lowercase).difference([ x for x in sentence.lower() if x in strinner.ascii_lowercase]))


# print("result ",check_difference(sentence))



def check_for_duplicate_without_extra_space(array):
    """check for duplicate without using extra space

    Args:
        array (_type_): _description_

    Returns:
        _type_: _description_
    """
    result = []
    for index,x in enumerate(array):

        # if str(x) in array:
        #     if x not in result:
        #         result.append(x)
            
        # else:
        #     array[index] = str(x)
        if array[abs(x)-1] < 0:
            result.append(abs(x))
        array[abs(x)-1] = -1 * array[abs(x)-1]
    return result


# print("check duplicate ",check_for_duplicate_without_extra_space([1,3,8,4,5,7,8,8]))

def first_non_repeated(string:str):
    """return first non repeated character

    Args:
        string (str): _description_

    Returns:
        _type_: _description_
    """
    result = OrderedDict()

    for char in string:
        result[char] = result.get(char,0) + 1
    
    for key,value in result.items():
        if value == 1:
            return key
    
    return ""

print("first non repeated character ",first_non_repeated("absbdgg"))



def find_number(matrix,number):
    c = len(matrix[0])
    r = len(matrix)

    ri = 0
    ci = c-1

    while ri < r and ci >=0:
        item = matrix[ri][ci]

        if number > item:
            ri +=1
        elif number < item:
            ci -=1

        else:
            return ri,ci

    return -1,-1


# print(
#     "find ",
#     find_number(
#     [
#         [1,2,3,4],
#         [5,6,7,8],
#         [9,10,11,12]
#     ],
#     7
# )
# )



def permute(LIST):
    length=len(LIST)
    if length <= 1:
        yield LIST
    else:
        for n in range(0,length):
             for end in permute( LIST[:n] + LIST[n+1:] ):
                 yield [ LIST[n] ] + end

# for x in permute(["3","3","4"]):
#     print(x)


