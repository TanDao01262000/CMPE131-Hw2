import time


def timestamp(func):
    def wrapper(*args, **kwargs):
        print(time.ctime())
        func(*args, **kwargs)
    return wrapper


