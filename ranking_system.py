

class User:
    def __init__(self) -> None:
        self.totalProgress = 0

    @property
    def progress(self):
        return  self.totalProgress%100 if self.rank < 8 else 0

    @property
    def rank(self):
        rank = (self.totalProgress//100) - 8
        return rank + 1 if rank>=0 else rank

    def inc_progress(self,rank):
        if (rank==0 or rank < -8 or rank >8):
            raise Exception("Rank out of bounds")

        if rank > 0 and self.rank < 0:
            rank -=1

        diff = rank - self.rank
        self.totalProgress += (10*diff*diff) if diff > 0 else (1 if diff < 0 else 3)




    