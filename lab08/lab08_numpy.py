import numpy as np
##1 задание
hours=np.arange(0,22,3)
line=np.linspace(0,1,5)
zeros=np.zeros(6)
unknown_table=np.full((2,3),-1)
identity=np.eye(3)
print("Задание 1")
print("hours:", hours)
print("shape:", hours.shape, "ndim:", hours.ndim, "size:", hours.size, "dtype:", hours.dtype)