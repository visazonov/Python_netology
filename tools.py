
# def cached(old_function):
#     cache = {}
#     number_off_calls = 0
#
#     def new_function(*args, **kwargs):
#         nonlocal number_off_calls
#         number_off_calls += 1
#         key = f'{args}_{kwargs}'
#         if key in cache:
#             return cache[key]
#
#         result = old_function(*args, **kwargs)
#
#         cache[key] = result
#         return result
#
#     return new_function

##################################################

def cached(max_size):
    def _cached(old_function):
        cache = {}
        number_off_calls = 0

        def new_function(*args, **kwargs):
            nonlocal number_off_calls
            number_off_calls +=1
            key = f'{args}_{kwargs}'
            if key in cache:
                return cache[key]

            result = old_function(*args, **kwargs)

            if len(cache) >= max_size:
                cache.popitem()
            cache[key] = result
            return result

        return new_function
    return _cached

cached_50 = cached(50)


# @cached_50
@cached(50)
def foo(a):
    return 42
