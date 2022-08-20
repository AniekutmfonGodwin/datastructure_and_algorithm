import unittest
from locate_card import locate_card_bruteforce




class TestLocateCard(unittest.TestCase):

    def test_1(self):

        self.assertEqual(locate_card_bruteforce([1,2,2,2,5,3,6],2),1)
        self.assertEqual(locate_card_bruteforce([5,3,4,7],3),1)
        self.assertEqual(locate_card_bruteforce([],3),-1)


if __name__ == "__main__":
    unittest.main()