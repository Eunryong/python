from numpy import array, int64, float64


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    '''get bmi
parameter:
height: list[int | float], weight: list[int | float]

return list[int | float]
    '''
    try:
        h = array(height)
        w = array(weight)
        assert h.dtype == (float64 or int64), 'sad'
        assert w.dtype == (float64 or int64), 'sad'
        assert h.shape == w.shape, 'sad'
        return (w / h * h).tolist()
    except AssertionError as e:
        print("AssertionError:", e)
        exit(1)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''checking bmi limit
parameter:
bmi: list[int | float]
limit: int

return list[bool]
    '''
    ret = []
    for i in bmi:
        ret.append(True if i >= limit else False)
    return ret
