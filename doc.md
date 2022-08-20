### Validate binary tree

        def valid(node,left,right):
            if not node:
                return True
            if not (node.val < right and node.val > left ):
                return False

            return valid(node.left,left,node.val) and valid(node.right,node.val,right)

        
        def isValidBST(root):
            return valid(root,float("-inf),float("inf))


### String segmentation
You are given a dictionary of words and a large input string. You have to find out whether the input string can be completely segmented into the words of a given dictionary. The following two examples elaborate on the problem further.

Given a dictionary of words.
[ apple ,apple, pear ]
input = applepie
output is true
[ apple, pie]

        def can_segment_string(s, dictionary):
            for i in range(1, len(s) + 1):
                first = s[0:i]
                if first in dictionary:
                    second = s[i:]
                    if not second or second in dictionary or can_segment_string(second, dictionary):
                        return True
            return False


### Reverse Words in a Sentence
Reverse the order of words in a given sentence (an array of characters).

"Hello World" == "World Hello"


        def str_rev(str, start, end):
            if str == None or len(str) < 2:
                return

            while start < end:
                temp = str[start]
                str[start] = str[end]
                str[end] = temp

                start += 1
                end -= 1
            return str


        def reverse_words(sentence):

            # Here sentence is a null-terminated string ending with char '\0'.

            if sentence == None or len(sentence) == 0:
                return

            #  To reverse all words in the string, we will first reverse
            #  the string. Now all the words are in the desired location, but
            #  in reverse order: "Hello World" -> "dlroW olleH".

            str_len = len(sentence)
            sentence = str_rev(sentence, 0, str_len - 2)

            # Now, let's iterate the sentence and reverse each word in place.
            # "dlroW olleH" -> "World Hello"

            start = 0
            end = 0

            while True:

            # find the  start index of a word while skipping spaces.
                while start < len(sentence) and sentence[start] == ' ':
                start += 1

                if start == str_len:
                break

            # find the end index of the word.
                end = start + 1
                while end < str_len and sentence[end] != ' ' and sentence[end] != '\0':
                end += 1

            # let's reverse the word in-place.
                sentence = str_rev(sentence, start, end - 1)
                start = end
            return sentence



### How many ways can you make change with coins and a total amount
Suppose we have coin denominations of [1, 2, 5] and the total amount is 7. We can make changes in the following 6 ways:

        def solve_coin_change(denominations, amount):
            solution = [0] * (amount + 1)
            solution[0] = 1;
            for den in denominations:
                for i in range(den, amount + 1):
                solution[i] += solution[i - den] 

            return solution[len(solution) - 1]


### Find Kth permutation

Given a set of ‘n’ elements, find their Kth permutation. Consider the following set of elements:

1
2
3
All permutations of the above elements are (with ordering):



Here we need to find the Kth permutation.


        def factorial(n):
            if n == 0 or n == 1:
                return 1
            return n * factorial(n -1 )

        def find_kth_permutation(v, k, result):
            if not v:
                return
            
            n = len(v)
            # count is number of permutations starting with first digit
            count = factorial(n - 1)
            selected = (k - 1) // count
            
            result += str(v[selected])
            del v[selected]
            k = k - (count * selected)
            find_kth_permutation(v, k, result)



### Find all subsets of a given set of integers
We are given a set of integers and we have to find all the possible subsets of this set of integers. The following example elaborates on this further.

Given set of integers:

2
3
4
All possile subsets for the given set of integers:

2
3
2, 3
4
2, 4
3, 4
2, 3, 4


        def get_bit(num, bit):
            temp = (1 << bit)
            temp = temp & num
            if temp == 0:
            return 0
            return 1
                
        def get_all_subsets(v, sets):
            subsets_count = 2 ** len(v)
            for i in range(0, subsets_count):
            st = set([])
            for j in range(0, len(v)):
                if get_bit(i, j) == 1:
                    st.add(v[j])
            sets.append(st)


### Print balanced brace combinations
Print all braces combinations for a given value n so that they are balanced. For this solution, we will be using recursion.

        import copy 

        def print_all_braces_rec(n, left_count, right_count, output, result):

            if left_count >= n and right_count >= n:
                result.append(copy.copy(output));
                
            if left_count < n:
                output += '{'
                print_all_braces_rec(n, left_count + 1, right_count, output, result)
                output.pop()

            if right_count < left_count:
                output += '}'
                print_all_braces_rec(n, left_count, right_count + 1, output, result)
                output.pop()

        def print_all_braces(n):
            output = []
            result = []
            print_all_braces_rec(n, 0, 0, output, result)
            return result


## Clone a Directed Graph

Given the root node of a directed graph, clone this graph by creating its deep copy so that the cloned graph has the same vertices and edges as the original graph.

Let’s look at the below graphs as an example. If the input graph is G = (V, E)
G=(V,E)
 where V is set of vertices and E is set of edges, then the output graph (cloned graph) G’ = (V’, E’) such that V = V’ and E = E’. We are assuming that all vertices are reachable from the root vertex, i.e. we have a connected graph.


        class Node:
            def __init__(self, d):
                self.data = d
                self.neighbors = []

        def clone_rec(root, nodes_completed):
            if root == None:
                return None

            pNew = Node(root.data)
            nodes_completed[root] = pNew

            for p in root.neighbors:
                x = nodes_completed.get(p)
                if x == None:
                pNew.neighbors += [clone_rec(p, nodes_completed)]
                else:
                pNew.neighbors += [x]
            return pNew

        def clone(root):
            nodes_completed = {}
            return clone_rec(root, nodes_completed)



### Find Low/High Index
Given a sorted array of integers, return the low and high index of the given key. You must return -1 if the indexes are not found. The array length can be in the millions with many duplicates.

In the following example, according to the key, the low and high indices would be:

key: 1, low = 0 and high = 0
key: 2, low = 1 and high = 1
key: 5, low = 2 and high = 9
key: 20, low = 10 and high = 10


    def find_low_index(arr, key):
  
        low = 0
        high = len(arr) - 1
        mid = int(high / 2)

        while low <= high:

            mid_elem = arr[mid]

            if mid_elem < key:
            low = mid + 1
            else:
            high = mid - 1

            mid = low + int((high - low) / 2)

        if low < len(arr) and arr[low] == key:
            return low

        return -1

    def find_high_index(arr, key):
        low = 0
        high = len(arr) - 1
        mid = int(high / 2)

        while low <= high:
            mid_elem = arr[mid]

            if mid_elem <= key:
            low = mid + 1
            else:
            high = mid - 1

            mid = low + int((high - low) / 2);
        
        if high == -1:
            return high

        if high < len(arr) and arr[high] == key:
            return high

        return -1


### Search Rotated Array
Search for a given number in a sorted array, with unique elements, that has been rotated by some arbitrary number. Return -1 if the number does not exist. Assume that the array does not contain duplicates.


    def binary_search_rotated(arr, key):
        start = 0
        end = len(arr) - 1

        if start > end:
            return -1
            
        while start <= end:
            mid = start + (end - start) // 2

            if arr[mid] == key:
            return mid

            if arr[start] <= arr[mid] and key <= arr[mid] and key >= arr[start]:
            end = mid - 1
            
            elif (arr[mid] <= arr[end] and key >= arr[mid] and key <= arr[end]):
            start = mid + 1

            elif arr[start] <= arr[mid] and arr[mid] <= arr[end] and key > arr[end]:
            start = mid + 1 

            elif arr[end] <= arr[mid]:
            start = mid + 1  

            elif arr[start] >= arr[mid]:
            end = mid - 1
            
            else:
            return -1
            
        return -1


