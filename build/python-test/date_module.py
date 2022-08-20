



from datetime import timedelta


class TimeNode:
    ...

    def generate_slot(self,interval:timedelta):
        ...


class DateNode:
    
    def __init__(self,opening,closing) -> None:
        self.opening = opening
        self.closing = closing
    
    def exclude_range(self,opening,closing):
        ...

