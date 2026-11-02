import numpy as np
def reshape_rows(values, width):
    if len(values)%width!=0:
        return []
    arr=np.asarray(values)
    reshaped_arr=arr.reshape(-1,width)
    return reshaped_arr.tolist()