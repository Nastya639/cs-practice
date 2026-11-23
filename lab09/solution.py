import numpy as np
def make_hours():
    return np.arange(0,22,3).tolist()
def vector_report(values):
    a=np.array(values)
    b= { 
        'Третий элемент': a[2],
        'Последний элемент': a[-1],
        'Срез со 2 по 6 элемент': a[2:7],
        'Каждый второй элемент': a[::2],
        'Развернутый вектор': a[::-1]
    }
    return b