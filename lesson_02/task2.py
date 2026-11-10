import math, mpmath, random

data = [random.randint(0, 9) + 0.5 for _ in range(10**6)]



def relative_error(approx, exact):
    if exact == 0:
        return float('inf')
    return abs(approx - exact) / abs(exact)

def tabl(approx: list[float], exact: list[float]):
    print(f"{"x":>14} | {"x*":>14} | {"Δx":>20} | {"δx":>20}" )
    print("-" * 80)
    for i, value in enumerate(exact):
        print(f"{approx[i]:>14.8f} | {exact[i]:>14.8f} | {abs(approx[i] - value):>14.18f} |"
              f"{(relative_error(approx[i], value) * 100):>14.18f} %")
        print("-" * 80)


print("Задача 1. Ручной счёт:\n")

exact = [math.pi, math.e, 9.81, 1 / 3] # точные значения
approx = [3.14, 2.718, 9.8, 0.333] # приблизительные значения

tabl(approx, exact)


print("\nЗадача 2. Сравнение несопоставимых величин:\n")

exact = [1250.0, 10.0] # точные значения
approx = [1247.0, 9.7] # приблизительные значения

tabl(approx, exact)


print("\nЗадача 3. Функция relative_error:\n")

exact = [math.pi, math.e, 9.81, 1 / 3, 0] # точные значения
approx = [3.14, 2.718, 9.8, 0.333, 999] # приблизительные значения

for i, value in enumerate(exact):
        print(f"{relative_error(approx[i], value)}")


print("\nЗадача 4. Обратная задача — оценка точного значения:\n")

a = 47.3 / (1 + 0.001)
b = 47.3 / (1 - 0.001)
print(f"[{a:.3f} - {b:.3f}]")


print("\nЗадача 5.  Порог по абсолютной и относительной ошибке:\n")

print(0.3 / 0.005) # = 60.0


print("\nЗадача 7. Честная запись результата.\n")

a = 4.738291
b = 0.02 # Δx

print(f"{(a - b):>.2f}") # = 4.72
print(f"{(a + b):>.2f}") # = 4.76


print("\nЗадача 8. Округление и banker's rounding.\n")

print(round(0.5), round(1.5), round(2.5), round(3.5),
    round(-0.5), round(-1.5), round(-2.5))

a = [random.randint(0,9) + 0.5 for i in range(10**2)]#range(10**7)] # убрал чтобы не тормозило при запуске
b = 0.0
c = 0.0

for i in a:
    b += round(i) # округление по правилу четности
    c += math.ceil(i) # округление строго вверх
     
print(f"\nround = {b} округление по правилу четности")
print(f"ceil = {c} округление строго вверх\n")


print("\nЗадача 9. Промежуточное округление — зло.\n")

a_sum = 0.0
b_sum_f3 = 0.0
c_sum_etl = 0.0

for k in range(1, 101):
    a_sum += 1 / k
    b_sum_f3 += round(1 / k, 3)

c_sum_etl = math.fsum(1/k for k in range(1, 101))

print(f"a = {a_sum} \nb.000 = {b_sum_f3} \nc_fsum = {c_sum_etl} \n")

tabl([a_sum], [c_sum_etl])
tabl([b_sum_f3], [c_sum_etl])


print("\nЗадача 10. Классика 0.1 + 0.2.\n")

a = 0.1 + 0.2
b = 0.3

print(f"a = {a}\nb = {b}\na == b - {a == b}\nisclose = {math.isclose(a, b)}\n")

# Не использовал функцию своей таблици для большей точности
print(f"Δx = {abs(a - b)}") # Δx 
print(f"δx = {relative_error(a, b)}\n") # δx


print("\nЗадача 11. Катастрофическая потеря точности.\n")

a = 1.0 + 1e-15
b = 1.0
print(f"a = {a}\na - b = {a - b}")
tabl([a - b], [1e-15])

b = 1e8; a = 1; c = 1
d = math.sqrt(b * b - 4 * a * c) # дискриминант
x1Small = (-b - d) / (2 * a) # больший корень
x2Small = (-b + d) / (2 * a) # меньший корень
x2Sml = (-2 * c) / (b + d) # меньший корень другая формула

print(f"\nx1 = {x1Small}")
print(f"x2 = {x2Small}")
print(f"x2 alt = {x2Sml}")
tabl([x2Small], [x2Sml])


print("\nЗадача 12. Накопление в цикле — сравнение стратегий.\n")

arr = [0.1] * 1_000_000
etl = 1e5

total= 0.0
for x in arr:
    total += x

total_sum = sum(arr)
total_fsum = math.fsum(arr)

print(f"for sum = {total:.15f}")
print(f"sum(arr) = {total_sum:.15f}")
print(f"math.fsum(arr) = {total_fsum:.15f}\n")

tabl([total, total_sum, total_fsum], [etl, etl, etl])