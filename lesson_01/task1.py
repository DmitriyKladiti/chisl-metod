import math, mpmath, random, sys
from mpmath import mp
import numpy as np

def cond(x, ffx, fx):
    return (x * ffx) / fx 

def relative_error(approx, exact):
    if exact == 0:
        return float('inf')
    return abs(approx - exact) / abs(exact)


print("Задача 1. Число обусловленности вручную.\n")

#1. f(x) = √x при x = 10−8
#2. f(x) = ln x при x = 1.001
#3. f(x) = x − 1 при x = 1.000001
#4. f(x) = sin x при x = π/2

print(f"1 = {cond(10e-8, (1 / 2 * math.sqrt(10e-8)), math.sqrt(10e-8))}")
print(f"2 = {cond(1.001, (1 / 1.001), math.log10(1.001))}")
print(f"3 = {cond(1.000001, 1, 1.000001 - 1)}")
print(f"4 = {cond(math.pi / 2, math.cos(math.pi / 2), math.sin(math.pi / 2))}")


print("Задача 2. Вычитание близких чисел как плохая обусловленность.\n")

# f(a, b) = a − b при a ≈ b. Ожидаемый результат 1e-8

a = 1 + 1e-8
b = 1.0
delta_a = 1e-9

result = ((a - b + delta_a) - (a - b)) / delta_a

print(result)
print((a - b))
print((a - b + delta_a) - (a - b))


print("\nЗадача 3. Кратные корни — плохая обусловленность.\n")

e = 1
x1 = (2 + math.sqrt(2 ** 2 - 4 * e)) / 2
x2 = (2 - math.sqrt(2 ** 2 - 4 * e)) / 2

print(f"x1 = {x1} x2 = {x2}")

x1 = (2 + math.sqrt(2 ** 2 - 4 * (e - 10**-2))) / 2
x2 = (2 - math.sqrt(2 ** 2 - 4 * (e - 10**-2))) / 2
print(f"\n10^-2:\nx1 = {x1} x2 = {x2}")

x1 = (2 + math.sqrt(2 ** 2 - 4 * (e - 10**-4))) / 2
x2 = (2 - math.sqrt(2 ** 2 - 4 * (e - 10**-4))) / 2
print(f"\n10^-4:\nx1 = {x1} x2 = {x2}")

x1 = (2 + math.sqrt(2 ** 2 - 4 * (e - 10**-6))) / 2
x2 = (2 - math.sqrt(2 ** 2 - 4 * (e - 10**-6))) / 2
print(f"\n10^-6:\nx1 = {x1} x2 = {x2}")


print("\nЗадача 4. Обусловленность vs устойчивость — различие.\n")

x = 1.e-2

alg = math.sin(x)
alg1 = math.sqrt(1 - pow(math.cos(x), 2))

print(alg)
print(alg1)
print(relative_error(alg1, alg) * 100)


print("\nЗадача 5. Квадратное уравнение — классика.\n")

mp.dps = 50

b = 1.e12
b_mp = mp.mpf(b)
x_bad = (-b + math.sqrt((b ** 2) - 4)) / 2
x_good = 2 / (-b - math.sqrt((b ** 2) - 4))
e = (-b_mp + mp.sqrt(b_mp**2 - 4)) / 2

print(f"e ={e}\n")
print(f"x_bad = {x_bad}")
print(relative_error(x_bad, e) * 100)
print(f"x_good = {x_good}")
print(relative_error(x_good, e) * 100)


print("\nЗадача 6. (1 − cos x) при малых x.\n")

x = 1.e-2
e = mp.mpf(x)

ee = (1 - mpmath.cos(e)) / e ** 2
bad = (1.0 - math.cos(x)) / (x ** 2)
good = 2.0 * (math.sin(x / 2.0) ** 2) / (x ** 2)

print(f"etl = {ee}\n")
print(f"bad = {bad}")
print(relative_error(bad, ee) * 100)
print(f"good = {good}")
print(relative_error(good, ee) * 100)


print("\nЗадача 7. √(x+1) − √x при больших x.\n")

x = 1.e16
e = mp.mpf(x)

ee = 1 / (mpmath.sqrt(e + 1) + mpmath.sqrt(e))
good = 1 / (math.sqrt(x + 1) + math.sqrt(x))
bad = (math.sqrt(x + 1) - math.sqrt(x))

print(f"etl = {ee}\n")
print(f"bad = {bad}")
print(relative_error(bad, ee) * 100)
print(f"good = {good}")
print(relative_error(good, ee) * 100)


print("\nЗадача 8. Экспонента и логарифм.\n")

mpmath.mp.dps = 50

x = 1.e-14

ee = mpmath.log(1 + mpmath.mpf(x)) 
good = math.log1p(x)
bad = math.log(1 + x)

print(f"etl = {ee}\n")
print(f"bad = {bad}")
print(relative_error(bad, ee) * 100)
print(f"good = {good}")
print(relative_error(good, ee) * 100)


print("\nЗадача 9. Неустойчивость накопления в сумме.\n")

k = 1.e5

a_sum = 0.0
for k in range(1, int(k + 1)):
    a_sum += 1 / k

b_sum_arr = sum([1 / i for i in range(1, int(k + 1))])
c_sum_f = math.fsum(1 / i for i in range(1, int(k + 1)))
e_sel_elit = mp.fsum(mp.mpf(1) / k for k in range(1, int(k + 1)))

print(f"etl = {e_sel_elit}\n")
print(f"for sum = {a_sum}")
print(relative_error(a_sum, e_sel_elit) * 100)
print(f"arr sum = {b_sum_arr}")
print(relative_error(b_sum_arr, e_sel_elit) * 100)
print(f"f sum = {c_sum_f}")
print(relative_error(c_sum_f, e_sel_elit) * 100)


print("\nЗадача 10. Разделение источников ошибки.\n")

x = 1.e-10
x32 = np.float32(x)
x64 = np.float64(x)
e = mpmath.mpf(x)

ee = (1 - mpmath.cos(e)) / e ** 2
bad_32 = (1.0 - math.cos(x32)) / (x32 ** 2)
bad_64 = (1.0 - math.cos(x64)) / (x64 ** 2)
good_64 = 2.0 * (math.sin(x64 / 2.0) ** 2) / (x64 ** 2)

print(f"etl = {ee}\n")
print(f"bad_32 = {bad_32}")
print(relative_error(bad_32, ee) * 100)
print(f"bad_64 = {bad_64}")
print(relative_error(bad_64, ee) * 100)
print(f"good_64 = {good_64}")
print(relative_error(good_64, ee) * 100)


print("\nЗадача 11. Эталон — обязателен.\n")

k = 1.e5

e_sel_elit = mp.fsum(mp.mpf(1) / k for k in range(1, int(k + 1)))

b_sum_arr = sum([1 / i for i in range(1, int(k + 1))])
c_sum_f = math.fsum(1 / i for i in range(1, int(k + 1)))

b_sum_arr_mp = sum([mpmath.mpf(1 / i) for i in range(1, int(k + 1))])
c_sum_f_mp = math.fsum(mpmath.mpf(1 / i) for i in range(1, int(k + 1)))

print(f"etl = {e_sel_elit}\n")
print(f"arr sum = {b_sum_arr}")
print(f"f sum = {c_sum_f}")
print(f"arr sum mp = {b_sum_arr_mp}")
print(f"f sum mp = {c_sum_f_mp}")

print(f"arr sum == f sum - {b_sum_arr == c_sum_f}")
print(f"arr sum mp == f sum mp - {b_sum_arr_mp == c_sum_f_mp}")


print("\nЗадача 13. Воспроизводимость эксперимента.\n")

N = 10 ** 5
seEed = 43

random.seed(seEed)
numbers = [random.random() for _ in range(N)]

rng = np.random.default_rng(seEed)
np_numbers = rng.random(N)

print("Seed =", seEed)
print("Python =", sys.version)
print("NumPy =", np.__version__)

print(f"\nrand sum = {sum(numbers)}")
print(f"rand f_sum = {math.fsum(numbers)}")
print(f"rand np_sum = {np.sum(numbers)}")

print(f"np rand sum = {sum(np_numbers)}")
print(f"np rand f_sum = {math.fsum(np_numbers)}")
print(f"np rand np_sum = {np.sum(np_numbers)}")

