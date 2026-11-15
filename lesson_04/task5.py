import time
import numpy as np
import math

rng = np.random.default_rng(42)
#m = rng.normal(size=(100_000, 10))
m = rng.normal(size=(1_000, 10))

def loop_sum_rows(mat):
    result = [0.0] * mat.shape[0]
    for i in range(mat.shape[0]):
        s = 0.0
        for j in range(mat.shape[1]):
            s += mat[i, j]
        result[i] = s
    return result

def numpy_sum_rows(mat):
    return mat.sum(axis=1)

def measure(fn, x, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(x)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best


print("\nЗадача 1. Сумма массива.\n")

#m = rng.normal(size=(10_000_000, 10))
m = rng.normal(size=(1_000, 10))

r_loop,  t_loop  = measure(loop_sum_rows,  m)
r_numpy, t_numpy = measure(numpy_sum_rows, m)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")


print("\nЗадача 2. Среднее и стандартное отклонение.\n")

#m = rng.normal(size=(1_000_000, 10))
m = rng.normal(size=(1_000, 10))

def loop_sum_rows1(mat):
    s = 0.0
    result = 0.0
    for i in range(mat.shape[0]):        
        for j in range(mat.shape[1]):            
            result += mat[i, j]/ mat.size
    return result

def loop_sum_rows2(mat):
    s = 0.0
    result = 0.0
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            result += (mat[i, j] ** 2) / mat.size        
    return result


def numpy_sum_rows1(mat):
    return mat.mean()

def numpy_sum_rows2(mat):
    return mat.std()


# r_loop,  t_loop  = measure(loop_sum_rows1,  m)
# r_numpy, t_numpy = measure(numpy_sum_rows1, m)

# print(f"цикл среднее:   {t_loop*1000:10.2f} мс")
# print(f"NumPy среднее:  {t_numpy*1000:10.2f} мс")
# print(f"ускорение: {t_loop / t_numpy:.1f}×")
# print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")

# r_loop_Sq,  t_loop_Sq  = measure(loop_sum_rows2,  m)
# r_numpy_Sq, t_numpy_Sq = measure(numpy_sum_rows2, m)

# print(f"цикл квадратное:   {t_loop_Sq*1000:10.2f} мс")
# print(f"NumPy квадратное:  {t_numpy_Sq*1000:10.2f} мс")
# print(f"ускорение: {t_loop_Sq / t_numpy_Sq:.1f}×")
# print(f"результаты совпадают: {np.allclose(r_loop_Sq, r_numpy_Sq)}")

print(f"цикл среднее = {loop_sum_rows1(m):>.12f}")
print(f"NumPy среднее = {numpy_sum_rows1(m):>.12f}")

print(f"цикл квадратное = {loop_sum_rows2(m):>.12f}")
print(f"NumPy квадратное = {numpy_sum_rows2(m):>.12f}")


print("\nЗадача 3. Поэлементное преобразование.\n")

#m = rng.normal(size=(1_000_000, 10))
m = rng.normal(size=(1_000, 10))

def loop_sum_rows3(mat):
    result = [0.0] * mat.shape[0]
    for i in range(mat.shape[0]):
        s = 0.0
        for j in range(mat.shape[1]):
            s += mat[i, j]
        result[i] = math.sin(s) + s*s
    return result

def numpy_sum_rows3(mat):
    return (np.sin(mat) + mat**2).sum(axis=1)

r_loop,  t_loop  = measure(loop_sum_rows3,  m)
r_numpy, t_numpy = measure(numpy_sum_rows3, m)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")


print("\nЗадача 4. Условная замена (clipping).\n")

# m = rng.normal(size=(100_000, 10))
m = rng.normal(size=(1_000, 10))

def loop_to_zero(mat):
    result = [0.0] * mat.shape[0]
    for i in range(mat.shape[0]):
        s = 0.0
        for j in range(mat.shape[1]):
            s = mat[i, j]
            if(s <= 0):
                s = 0.0
            else: s = 1.0
        result[i] = s
    return result

def numpy_to_zero(mat):
    return np.clip(mat, 0, 1)

r_loop,  t_loop  = measure(loop_to_zero,  m)
r_numpy, t_numpy = measure(numpy_to_zero, m)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")


print("\nЗадача 5. Сумма по строкам матрицы.\n")

# m = rng.normal(size=(100_000, 10))
m = rng.normal(size=(1_000, 10))

def loop_sum(mat):
    result = [0.0] * mat.shape[0]
    for i in range(mat.shape[0]):
        s = 0
        for j in range(10): 
            s += m[i, j]
            result[i] = s
    return result

def numpy_sum(mat):
    return mat.sum(axis=1)

r_loop,  t_loop  = measure(loop_sum,  m)
r_numpy, t_numpy = measure(numpy_sum, m)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")


print("\nЗадача 6. Среднее по столбцам и нормировка.\n")

# m = rng.normal(size=(100_000, 10))
m = rng.normal(size=(1_000, 10))

def loop_mean(mat):
    rows = mat.tolist()
    n, k = len(rows), len(rows[0])

    result = [[0.0] * k for _ in range(n)]

    for j in range(k):
        mean_j = sum(rows[i][j] for i in range(n)) / n
        for i in range(n):
            result[i][j] = rows[i][j] - mean_j

    return result

def numpy_mean(mat):
    return mat - mat.mean(axis=0)

r_loop,  t_loop  = measure(loop_mean,  m)
r_numpy, t_numpy = measure(numpy_mean, m)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")


print("\nЗадача 7. Поиск максимума и его индекса.\n")

a = rng.normal(size=(1_000_000))

def loop_max(mat):
    max_val = mat[0]
    max_ind = 0
    for i in range(mat.shape[0]):
        if (max_val < mat[i]):
            max_val = mat[i]
            max_ind = i
    return max_val, max_ind

def numpy_max(mat):
    return mat.max(), mat.argmax()

r_loop,  t_loop  = measure(loop_max,  a)
r_numpy, t_numpy = measure(numpy_max, a)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")