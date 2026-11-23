import numpy as np
def make_hours():
    return np.arange(0,22,3).tolist()
def vector_report(values):
    a = np.array(values, dtype=float)
    b = {
        "third": float(a[2]),
        "last": float(a[-1]),
        "middle": a[2:6].tolist(),
        "every_second": a[::2].tolist(),
        "reversed": a[::-1].tolist()
    }
    return b
def change_vector(values):
    a=np.asarray(values).copy()
    a[2:5]=99
    a[::2]=-1
    return a.tolist()
def cap_above(values, limit):
    a=np.asarray(values).copy()
    mask = a > limit
    a[mask] = limit
    return a.tolist()
def celsius_to_fahrenheit(values):
    a=np.asarray(values).copy()
    a = (a * 9/5) + 32
    return a.tolist()