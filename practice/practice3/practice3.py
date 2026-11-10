import numpy as np

# 1 Создайте массив формы (6, 4) из np.arange(24). Выведите .shape, .ndim, .size, .dtype.
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16],
              [17, 18, 19, 20],
              [21, 22, 23, 24]])
print(a)
print(a.shape)   
print(a.ndim)    
print(a.size)    
print(a.dtype)   
# 2 Перестройте его в (4, 6), затем в (2, 3, 4), затем обратно в (24,).
# Убедитесь через np.array_equal, что значения не изменились.
A = a.copy()
b = a.reshape(4,6)
print(b)
c = a.reshape(2,3,4)
print(c)
e = a.reshape(24)
print(e)
print(np.array_equal(a, A))
# 3 Возьмите столбец [:, 2] — это view или копия? Проверьте: измените элемент среза и 
# посмотрите на оригинал.
A = a[:,2]
A[2] = 80
print(A[2])
# 4 Отфильтруйте элементы > 10 булевой маской. Посчитайте их среднее.
print(A[A>10].mean())
# 5 Вычтите из каждой строки её среднее (axis=1, keepdims=True) — убедитесь, что результат имеет 
# ту же форму и сумма по строкам ≈ 0. 
means = a - a.mean(axis=1, keepdims=True)
print(means.shape, means.sum(axis=1))