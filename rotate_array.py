



def rotate_array(array,d):

    if d > len(array) -1:
        return array

    return array[d:] + array[:d]



if __name__ == "__main__":
    print("rotate ",rotate_array([2,4,5,6,2,3],2))



