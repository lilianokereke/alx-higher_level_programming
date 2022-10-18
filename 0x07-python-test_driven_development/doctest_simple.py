#import doctest

def myfunc(a,b):
    """
    >>> myfunc(2,3)
    5
    >>> myfunc(3, 'd')
    'ddd'
    Traceback (most recent call last):
        ...
    TypeError: can only concatenate str (not "int") to str

    """

    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
