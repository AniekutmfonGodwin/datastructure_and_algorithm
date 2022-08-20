import timeit




def compute_time(func):
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()

        res = func(*args, **kwargs)

        stop = timeit.default_timer()
        print('Time: ', stop - start," ms")
        return res
    return wrapper



@compute_time
def add_two(*args):
    return sum(args)


