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
def column_range(matrix, column):
    if not matrix or not matrix[0]:
        return 0.0
    arr=np.asarray(matrix)
    col=arr[:,column]
    scope=col.max()-col.min()
    return float(round(scope,6))

test_matrix=[[1,2,3],[4,5,6],[7,8,9]]
test_values=[10,20,30,40,50,60]
if __name__=="__main__":
    print('reshape_rows: ', reshape_rows(test_values,3))
    print('block: ', block(test_matrix,[0,2],[1]))
    print('column_means: ', column_means(test_matrix))
    print('column_range: ', column_range(test_matrix,2))
