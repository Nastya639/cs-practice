import numpy as np
def reshape_rows(values, width):
    if len(values)%width!=0:
        return []
    arr=np.asarray(values)
    reshaped_arr=arr.reshape(-1,width)
    return reshaped_arr.tolist()
def block(matrix, rows, columns):
    if not matrix or not matrix[0]:
        return []
    arr=np.asarray(matrix)
    grid=np.ix_(rows,columns)
    sub_matrix=arr[grid]
    return sub_matrix.tolist()
def column_means(matrix):
    if not matrix or not matrix[0]:
        return []
    arr=np.asarray(matrix)
    means=arr.mean(axis=0)
    rounded_means=np.round(means,6)
    return rounded_means.tolist()
