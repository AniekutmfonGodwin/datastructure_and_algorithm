

def first_missing_positive(array):
    """find the first missing positive number with space O(1) and time O(n)
    steps:
        given and array arr
        missing positive number is going to be 1 >= x <= len(arr) + 1

        pseudocode
        * loop through the list and replace every number less than or equal to 0 , 
        and also number greater than len(arr) + 1 with len(arr)+1
        * loop throught the list and for each item i negate the value at the index |i| - 1 
        and perform same for all the values
        * loop through the array the first element still having the possitive number is the result, else return len(arr) + 1

    Args:
        array (_type_): _description_
    """
    # cleaning up the array
    for indx in range(len(array)):
        if array[indx] <= 0 or array[indx] > len(array):
            array[indx] = len(array) + 1
    
    # placing our marker to see what numbers have been accounted for
    for num in array:
        num = abs(num)
        if num <= len(array) and array[num - 1] >= 0:
            array[num - 1] *= -1
    
    # final step for getting the answer
    for indx in range(len(array)):
        if array[indx] > 0:
            return indx + 1
    
    return len(array) + 1


def find_unique_path(row,column):
    """for finding a unique path
    ref = https://www.youtube.com/watch?v=4Zq2Fnd6tl0&list=PLtQWXpf5JNGJagakc_kBtOH5-gd8btjEW

    psuedocode:
    * create a matrix with size equal to the 
    row and column all cell containing zero as thier value.
    *traverse through all the cell in that matrix
    *if the cell is at the boarder mark it value as one
    * if not at the boarder, mark its value as the sum of the
     value above it and the value by the left of it.
    *once all item is marked return the element at the most bottom right coner

    Args:
        matrix (_type_): _description_
    """
    empty = [ [0]*column ] * row #this create an empty matrix
    for rowindex in range(row):
        for columnindex in range(column):
            if rowindex == 0 or columnindex == 0:
                empty[rowindex][columnindex] = 1
            else:    
                print("row ",rowindex," column ",columnindex)
                empty[rowindex][columnindex] = empty[rowindex-1][columnindex] + empty[rowindex][columnindex-1]

    return empty[row-1][column-1]



# print("unique path ",find_unique_path(40,60))


def mark_as_visited(grid,rowindex,columnindex,row,column):

    if rowindex < 0 or rowindex >= row or columnindex < 0 or columnindex >= column or grid[rowindex][columnindex] !="1":
        return
    grid[rowindex][columnindex] = "2"


    mark_as_visited(grid,rowindex+1,columnindex,row,column)
    mark_as_visited(grid,rowindex,columnindex+1,row,column)
    mark_as_visited(grid,rowindex-1,columnindex,row,column)
    mark_as_visited(grid,rowindex,columnindex-1,row,column)




def number_of_island(grid):
    """find the number of island
    pseudocode:
    * create a variable call number_of_island
    * go through all the cell in the matrix for each cell
    * for each cell check if the cell is not visited  (value is not 2) and the value is not zero (water)
    * if condition is true mark island with mark_island_function and increment the number
    of island variable else skip to the next cell.

    https://www.youtube.com/watch?v=__98uL6wst8

    Args:
        grid (_type_): _description_
    """
    row = len(grid)

    if row == 0:
        return 0

    column = len(grid[0])

    island_count = 0
    for rowindex in range(row):
        for columnindex in range(column):
            if grid[rowindex][columnindex] == "1":
                mark_as_visited(grid,rowindex,columnindex,row,column)
                island_count +=1


    return island_count




print("number of island ",number_of_island([
    ["1","1","0","0"],
    ["1","0","0","0"],
    ["0","0","1","0"],
    ["0","0","1","0"],
]))




# get unique island



def find_min_max(array):
    """get the mininmum sum and the maximum sum of an array

    psuedo:
    create variable for total sum , minimum and maximum 
    Args:
        array (_type_): _description_
    """
    total = 0
    minimum = float("inf")
    maximum = float("-inf")



    for i in range(len(array)):
        total +=array[i]

        minimum = min(minimum,array[i])
        maximum = max(maximum,array[i])


    print("min = ",total - maximum," max = ",total - minimum)
    

# print("min and max sum ",find_min_max([2,3,4,6,7]))




def birthdayCakeCandle(arr):
    """maximum candle she can blow

    Args:
        arr (_type_): _description_

    Returns:
        _type_: _description_
    """
    candles = {}
    maximum = float("-inf")

    for item in arr:
        candles[str(item)] = candles.get(str(item),0) + 1


        maximum = max(maximum,item)

    return candles.get(str(maximum))


# print("maximum she can blow ",birthdayCakeCandle([1,5,6,7,7,3,4,5]))



def gradingStudents(grades):
    """
    student receive grade form 0 - 100

    conditions:
        grade < 40 is fail
        |grade - [next multiple of 5]| < 3 round grade up to the next multiple of 5

    Args:
        grades (_type_): _description_
    """
    results = []



    for item in grades:
        f = (item + 5) - (item + 5)%5
        if (f - item) < 3 and item >= 38:
            results.append(f)
        else:
            results.append(item)

    return results



# print("result ",gradingStudents([73,67,38,33]))



def sum_of_two_from_two_array(array1,array2,target):
    """check if its possible to combine number from array1 and array2
    to return the sum of the target

    Args:
        array1 (_type_): _description_
        array2 (_type_): _description_
        target (_type_): _description_
    """
    for item in array1:

        if (max(target,item) - min(target,item)) in array2:
            return True

    return False


# print("is possible ",sum_of_two_from_two_array([-1,2,3],[10,20,30],-9))



def countAppleAndOranges(s,t,a,b,apples:list,oranges:list):
    """
    d distane from the tree where the tree falls (negative number of d means fruit fall to the left)
    s is the distance between the tree and starting of sam house
    t is the distance between the tree and ending of sam house
    a distance of apple tree from the origin 
    b distance of orange tree from the origin 




    Args:
        s (_type_): _description_
        t (_type_): _description_
        a (_type_): _description_
        b (_type_): _description_
        apple (_type_): _description_
        oranges (_type_): _description_
    """

    apple_count = orange_count = 0


    
    while apples or oranges:

        if apples:
            apple = apples.pop()
            if s <= a + apple <=t:
                apple_count +=1

        
        if oranges:
            orange = oranges.pop()
            if s <= b + orange <=t:
                orange_count +=1

    # print("orange and apple count ",orange_count,apple_count)
    






def find_contigous_subarray_sum(array):
    

    max_sum = float("-inf")

    for i,_ in enumerate(array):

        for subi,_ in enumerate(array[i:]):
            temp_sum = sum(array[i:subi+1])
            if temp_sum>max_sum:
                max_sum = temp_sum

    return max_sum
        

print("answer ",find_contigous_subarray_sum([-2,3,4,1]))