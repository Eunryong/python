import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''
Slices the given list from the start index to the end index (inclusive).

Parameters:
    family (list): The list to be sliced.
    start (int): The starting index of the slice.
    end (int): The ending index of the slice.

Returns:
    list: The sliced portion of the list.

Example:
    >>> slice_list([1, 2, 3, 4, 5], 1, 3)
    [2, 3, 4]
    '''
    try:
        assert type(family) is list, 'Invalid parameters'
        if len(family) == 0:
            return family
        size = len(family[0])
        for x in family:
            assert type(x) is list, 'Invalid parameters'
            assert len(x) == size, 'Invalid parameters'
        ret = np.array(family)
        print(f"My shape is : {ret.shape}")
        ret = ret[start:end]
        print(f"My new shape is : {ret.shape}")
        return ret.tolist()
    except AssertionError as e:
        print("AssertionError:", e)
        exit(1)


if __name__ == "__main__":

    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
