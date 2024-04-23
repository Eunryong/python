
def ft_filter(fun, iterable):
    '''filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.'''
    if fun is None:
        return [i for i in iterable if i]
    return [i for i in iterable if fun(i)]
