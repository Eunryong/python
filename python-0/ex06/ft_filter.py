
def ft_filter(fun, iterable):
    if fun is None:
        return [i for i in iterable if i]
    return [i for i in iterable if fun(i)]