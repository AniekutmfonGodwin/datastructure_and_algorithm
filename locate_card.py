
from typing import List


def locate_card_bruteforce(cards:List[int],query:int):
    """return the index at which the index exists

    Args:
        cards (List[int]): a list of number representing cards
        query (int): the card number to find
    Return:
        the index at which the card exist ,return -1 if not exists
    
    """
    
    for index,card in enumerate(cards):
        if card == query:
            return index


    return -1




    
def locate_card_binary_search(cards:List[int],query:int):
    low,high = 0,len(cards) - 1

    while True:
        mid = len(cards[low:high+1])//2
        mid_item = cards[mid]
        
        if mid_item == query:
            return mid
        elif mid_item > query:
            low = mid + 1
        else:
            high = mid - 1

        if low >= high:
            return -1
        
        import pdb;pdb.set_trace()
        print("high ",high," low ",low," mid ",mid," query ",query," mid_item ",mid_item)

        

    






if __name__ == "__main__":
    # print("card location ",locate_card_bruteforce([3,5,2,7,55,3,3],3))
    print("card location ",locate_card_binary_search([5,4,3,2,1],1))