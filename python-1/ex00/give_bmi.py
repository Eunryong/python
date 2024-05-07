import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    '''get bmi
parameter:
height: list[int | float], weight: list[int | float]

return list[int | float]
    '''
    try:
        h = np.array(height)
        w = np.array(weight)
        assert h.dtype == (np.float64 or np.int64), 'sad'
        assert w.dtype == (np.float64 or np.int64), 'sad'
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
