def log_args(func):
    print(func.__name__)

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@log_args
def sum_it(*args):
    return sum(args)


sum_3 = sum_it(1, 2, 13)
print(sum_3)
