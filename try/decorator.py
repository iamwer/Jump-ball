
def sum(a,b):
    return a + b

def logger(func):
    def wrapper(a,b):
        print(f'{func.__name__} started')
        result = func(a,b)
        print(f'{func.__name__} finished')
        return result

    return wrapper




if __name__ == '__main__':
    function = logger(sum)
    print(function(2,3))

    print(logger(sum)(2,3))
