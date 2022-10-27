import time

def timeme(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        run_time = time.time() - start
        print(f'Total time {run_time}')
    return wrapper

