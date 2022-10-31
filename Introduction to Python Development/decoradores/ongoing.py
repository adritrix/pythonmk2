def inspect(func, *args):
    def warpped_func(*args, **kwargs):
        print(f"Running {func.__name__}")
        val = func(*args)
        print(val)
        return val
    return warpped_func


@inspect
def combine(a, b):
    return a + b

# class User:
#     base_url = 'https://example.com/api'

#     def__init__(self, first_name)