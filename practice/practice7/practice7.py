import math
import numpy as np
import matplotlib.pyplot as plt


def bisection(f, a, b, eps=1e-9, max_iter=200):
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
        if fc == 0:
            return c, journal, "f_zero"
        if length < eps:
            return c, journal, "ok"
        
        # обновляем интервал
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return c, journal, "max_iter"


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


def f_pract1(x):
    return x**3 - 6 * x**2 + 11 * x -6

x = np.linspace(0, 4, 100)
plt.figure(figsize=(10, 6))
plt.plot(x, f_pract1(x), 'b-', linewidth=2, label=r'$f(x) = x^3 - 6x^2 + 11x - 6$')
plt.axhline(0, color='black', linewidth=1)   # ось OX
plt.axvline(0, color='black', linewidth=1)
plt.tight_layout()
plt.show()


root1, j1, s1 = bisection(f_pract1, 0.5, 1.5, eps=1e-9)
print_journal(j1, "f(x) = x^3 - 6x^2 + 11x - 6,  [0.5, 1.5]")
print(f"корень: {root1:.12f},  f(root) = {f_pract1(root1):.3e},  статус: {s1}")

root2, j2, s2 = bisection(f_pract1, 1.6, 2.5, eps=1e-9)
print_journal(j2, "f(x) = x^3 - 6x^2 + 11x - 6,  [1.6, 2.5]")
print(f"корень: {root2:.12f},  f(root) = {f_pract1(root2):.3e},  статус: {s2}")

root3, j3, s3 = bisection(f_pract1, 2.6, 3.5, eps=1e-9)
print_journal(j3, "f(x) = x^3 - 6x^2 + 11x - 6,  [2.6, 3.5]")
print(f"корень: {root3:.12f},  f(root) = {f_pract1(root3):.3e},  статус: {s3}")