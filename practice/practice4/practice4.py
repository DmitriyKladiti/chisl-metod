import time
import numpy as np
import math

rng = np.random.default_rng(42)
m = rng.normal(size=(100_000, 10))


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



# 1

r_loop,  t_loop  = measure(loop_sum_rows,  m)
r_numpy, t_numpy = measure(numpy_sum_rows, m)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")

# 2

m = rng.normal(size=(10_000, 10))

def loop_sum_rows1(mat):
    result = [0.0] * mat.shape[0]
    for i in range(mat.shape[0]):
        s = 0.0
        for j in range(mat.shape[1]):
            s += mat[i, j]
        result[i] = s / mat.size
    return result

def loop_sum_rows2(mat):
    result = [0.0] * mat.shape[0]
    for i in range(mat.shape[0]):
        s = 0.0
        for j in range(mat.shape[1]):
            s += mat[i, j]
        result[i] = s**2 / mat.size
    return result


def numpy_sum_rows1(mat):
    return mat.mean()

def numpy_sum_rows2(mat):
    return mat.std()


r_loop,  t_loop  = measure(loop_sum_rows1,  m)
r_numpy, t_numpy = measure(numpy_sum_rows1, m)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")

# 3 

m = rng.normal(size=(100_000, 10))

def loop_sum_rows3(mat):
    result = [0.0] * mat.shape[0]
    for i in range(mat.shape[0]):
        s = 0.0
        for j in range(mat.shape[1]):
            s += mat[i, j]
        result[i] = math.sin(s) + s*s
    return result

print("3")
def numpy_sum_rows3(mat):
    return (np.sin(mat) + mat**2).sum(axis=1)

r_loop,  t_loop  = measure(loop_sum_rows3,  m)
r_numpy, t_numpy = measure(numpy_sum_rows3, m)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")