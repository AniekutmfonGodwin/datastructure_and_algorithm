

from collections import Counter
from dataclasses import dataclass
from typing import Any, List
import unittest
import test


# name = "racecsr"
# reversed_name = name[::-1]

# print("revered+name ",reversed_name)
# if reversed_name == name:
#     print("it is a palendrom")

# else:
#     print("it is not a palendrom")


@dataclass
class Stack:
    data:List[str]
    

    def peek(self):
        return self.data[-1]

    def push(self,value:Any):
        self.data.append(value)

    def pop(self):
        return self.data.pop()
    def count(self):
        return len(self.data)



    



stack = Stack([1,2,3,4,5])


def scramble(s1, s2):
    s1,s2 = str(s1),str(s2)

    return all([x.lower() in s1.lower() for x in s2])
    

print(scramble('rkqodlw', 'world'))
print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))
print(scramble('scriptjava', 'javascript'))
print(scramble('scriptingjava', 'javascript'))

