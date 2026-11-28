import math
import numpy as np
import matplotlib.pyplot as plt


def bisection(f, a, b, eps=1e-9, max_iter=200, for_task3 = False):
    """
    Метод половинного деления с журналом итераций.
    
    Возвращает: (корень, журнал, статус)
      статус = 'ok'        — достигнута точность по длине интервала
      статус = 'f_zero'    — f(c) == 0 (точное попадание)
      статус = 'max_iter'  — исчерпан лимит итераций
    """
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError(
            f"Нет смены знака на [{a}, {b}]: f(a)={fa}, f(b)={fb}"
        )
    
    journal = []   # список словарей — каждая запись = одна итерация
    
    for k in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)
        length = b - a
        
        # записываем всё, что нужно для аудита
        journal.append({
            "iter": k,
            "a": a,
            "b": b,
            "c": c,
            "f(c)": fc,
            "length": length,
        })
        
        # условия остановки
        if fc == 0 & for_task3 == False:
            return c, journal, "f_zero"
        elif fc == 0 & for_task3 == True: return k, length, fc

        if length < eps and for_task3 == False:
            return c, journal, "ok"
        elif length < eps and for_task3 == True: return k, length, fc
        
        # обновляем интервал
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    if for_task3 == False:
        return c, journal, "max_iter", k, length, fc
    else:
        return k, length, fc


def print_journal(journal, title=""):
    if title:
        print(f"\n=== {title} ===")
    print(f"{'k':>3} | {'a':>12} | {'b':>12} | {'c':>12} | "
          f"{'f(c)':>14} | {'b-a':>10}")
    print("-" * 80)
    for row in journal:
        print(f"{row['iter']:>3} | {row['a']:>12.6f} | {row['b']:>12.6f} | "
              f"{row['c']:>12.6f} | {row['f(c)']:>14.3e} | "
              f"{row['length']:>10.2e}")


print("\nЗадача 1. Базовая бисекция с журналом\n")

def f_tack1(x):
    return x**3 - 2 * x - 5

x = np.linspace(1, 4, 100)
plt.figure(figsize=(10, 6))
plt.plot(x, f_tack1(x), 'b-', linewidth=2, label=r'$f(x) = x^3 - 2x - 5$')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.tight_layout()
plt.show()

root1, j1, s1 = bisection(f_tack1, 2.0, 3.0, eps=1e-6)
print_journal(j1, "f(x) = x^3 - 2x - 5,  [2.0, 3.0]")
print(f"корень: {root1:.12f},  f(root) = {f_tack1(root1):.3e},  статус: {s1}")


print("\nЗадача 2. Все корни на отрезке\n")

def f_tack2(x):
    return x**3 - 4 * x

x = np.linspace(-3, 3, 100)
plt.figure(figsize=(10, 6))
plt.plot(x, f_tack2(x), 'b-', linewidth=2, label=r'$f(x) = x^3 - 4x$')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.tight_layout()
plt.show()

root1, j1, s1 = bisection(f_tack2, -2.5, -1.5, eps=1e-8)
print_journal(j1, "f(x) = x^3 - 4x,  [-2.5, -1.5,]")
print(f"корень: {root1:.12f},  f(root) = {f_tack2(root1):.3e},  статус: {s1}")

root2, j2, s2 = bisection(f_tack2, -1.0, 1.0, eps=1e-8)
print_journal(j2, "f(x) = x^3 - 4x,  [-1.0, 1.0]")
print(f"корень: {root2:.12f},  f(root) = {f_tack2(root2):.3e},  статус: {s2}")

root3, j3, s3 = bisection(f_tack2, 1.5, 2.5, eps=1e-8)
print_journal(j3, "f(x) = x^3 - 4x,  [1.5, 2.5]")
print(f"корень: {root3:.12f},  f(root) = {f_tack2(root3):.3e},  статус: {s3}")

root4, j4, s4 = bisection(f_tack2, -3.0, 3.0, eps=1e-8)
print_journal(j4, "f(x) = x^3 - 4x,  [-3.0, 3.0]")
print(f"корень: {root4:.12f},  f(root) = {f_tack2(root4):.3e},  статус: {s4}")


print("\nЗадача 3. Влияние точности на число итераций\n")

def besection_top(f_bis, a_bis, b_bis, eps1, eps2, shag):
    shag_exp = shag

    print(f"{'e':>12} | {"teor_count":>12} | {"count_iter":>12} | {"b-a":>12} | {"f(c)":>12} |")
    print('-' * 74)

    while(eps1 >= eps2):        
        k, length, fc = bisection(f_bis, a_bis, b_bis, eps=eps1, for_task3 = True)
        print(f"{eps1:>12.3e} | {n_log(eps1, 1):>12.2f} | {k:>12} | {length:>12.3e} | {fc:>12.2e} |")
        shag_exp = shag_exp + shag 
        eps1 = 10 ** shag_exp

def f_tack3(x):
    return math.e**x - 3 * x

def n_log(eps, delta):
    return math.log2(delta / eps)

x = np.linspace(0, 1, 100)
plt.figure(figsize=(10, 6))
plt.plot(x, f_tack3(x), 'b-', linewidth=2, label=r'$f(x) = e^x - 3x$')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.tight_layout()
plt.show()

print(f"F(0) = {f_tack3(0)}")
print(f"F(1) = {f_tack3(1)}")

root1, j1, s1 = bisection(f_tack3, 0.0, 1.0, eps=1e-2)
print_journal(j1, "f(x) = e^x - x,  [0.0, 1.0]")
print(f"корень: {root1:.12f},  f(root) = {f_tack3(root1):.3e},  статус: {s1}")

besection_top(f_tack3, 0, 1, 1e-2, 1e-10, -2)
    