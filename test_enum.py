from dataclasses import dataclass
from enum import Enum



@dataclass
class Value:
    name:str
    path:str = None
    


    def url(self,id):
        if self.path:
            return self.path.format(id=id)
        return ""

    


class New(Enum):

    QUEUE = Value("Queue","/queue/{id}/")
    ORDER = Value("Order","/order/{id}/")
    JOB = Value("Job","/job/{id}/")