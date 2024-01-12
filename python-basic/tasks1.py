import time

def retry(func):
    def wrapper(*args, **kwargs):
        attempts = 3
        timeout = 1
        retries = 0
        while retries < attempts:
            try:
                value = func(*args, **kwargs)
                return value
            except Exception as e:
                print("Got exception. Retrying \n{}".format(e))
                time.sleep(timeout)
                retries += 1
    return wrapper

@retry
def get_diff(a, b): 
    raise Exception("Wrong func")

a=[1,2,3,4,5]
b=[3,4]

get_diff(a, b)