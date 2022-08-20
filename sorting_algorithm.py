
def insertion_sort(A):
    """insertion sort

    Args:
        A (_type_): _description_

    Returns:
        _type_: _description_
    """
    for i in range(1, len(A)):
        while A[i-1] > A[i] and i > 0:
            A[i-1], A[i] = A[i], A[i-1]
            i -= 1


# a  = [4,3,2,6,7]
# insertion_sort(a)
# print("insertion sort ",a)


def selection_sort(arr):
    
    for i in range(0,len(arr)-1):
        p=0
        mini=arr[-1]
        for j in range(i,len(arr)):
            if arr[j]<=mini:
                mini=arr[j]
                p=j
        arr[i],arr[p]=arr[p],arr[i]
    


a  = [4,3,2,6,7]
selection_sort(a)
print("selection sort ",a) 
