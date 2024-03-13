def my_sum(x, y):
    """
    >>> my_sum(10, 20)
    30

    >>> my_sum('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float.

    >>> my_sum(10, '20')
    Traceback (most recent call last):
    ...
    AssertionError: y precisa ser int ou float.
    """

    assert isinstance(x, (int, float)), 'x precisa ser int ou float.'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float.'
    return x + y


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
