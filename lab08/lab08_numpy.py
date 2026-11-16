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

##задание 2
print()
print("Задание 2")
print("Третий элемент: ", hours[2])
print("Последний элемент: ", hours[-1])
print("Элементы с индексами 2 - 5: ", hours[2:6])
print("Каждый второй элемент: ", hours[::2])
print("Массив в обратном порядке: ", hours[::-1])

##задание 3
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
print()
print("Задание 3")
print("Форма массива: ", temperatures.shape)
print("Число измерений: ", temperatures.ndim)
print("Число измерений: ", temperatures.ndim)
print("Значение из второй строки и третьего столбца: ", temperatures[1,2])
print("Первая строка: ", temperatures[0])
print("Последний столбец: ", temperatures[:, -1])
print("Первые две строки без первого столбца: ", temperatures[:2, 1:4])
print("Центральный фрагмент 2×2: ", temperatures[:2,1:3])

##задание 4
matrix = np.arange(1, 26).reshape(5, 5)
print()
print("Задание 4")
print("Первые 3 строки: ", matrix[:3], matrix[:3].shape)
print("Последние 2 строки: ", matrix[-2:], matrix[-2:].shape)
print("Первые 2 столбца: ", matrix[:,:2], matrix[:,:2].shape)
print("Фрагмент из строк с индексами 1–3 и столбцов 2–4: ", matrix[1:4, 2:5], matrix[1:4, 2:5].shape)
print("Угловой блок 2×2 в правом нижнем углу: ", matrix[3:5, 3:5], matrix[3:5, 3:5].shape)