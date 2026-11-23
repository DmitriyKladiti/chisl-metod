import math
import numpy as np
import matplotlib.pyplot as plt


def newton(f, df, x0, eps=1e-12, max_iter=100):
    """
    Метод Ньютона (касательных).
    Возвращает: (корень, журнал, статус)
    """
    journal = []
    x = x0
    for k in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            return x, journal, "zero_derivative"
        x_new = x - fx / dfx
        journal.append({
            "iter": k,
            "x": x,
            "f(x)": fx,
            "f'(x)": dfx,
            "x_new": x_new,
            "step": abs(x_new - x),
        })
        if abs(x_new - x) < eps or abs(fx) < eps:
            return x_new, journal, "ok"
        x = x_new
    return x, journal, "max_iter"

def secant(f, x0, x1, eps=1e-12, max_iter=100):
    """
    Метод секущих.
    Возвращает: (корень, журнал, статус)
    """
    journal = []
    x_prev, x_curr = x0, x1
    f_prev, f_curr = f(x_prev), f(x_curr)
    
    for k in range(1, max_iter + 1):
        if f_curr - f_prev == 0:
            return x_curr, journal, "zero_denominator"
        x_new = x_curr - f_curr * (x_curr - x_prev) / (f_curr - f_prev)
        journal.append({
            "iter": k,
            "x_prev": x_prev,
             "x_curr": x_curr,
            "f_curr": f_curr,
            "x_new": x_new,
            "step": abs(x_new - x_curr),
        })
        if abs(x_new - x_curr) < eps or abs(f_curr) < eps:
            return x_new, journal, "ok"
        x_prev, f_prev = x_curr, f_curr
        x_curr = x_new
        f_curr = f(x_curr)
    return x_curr, journal, "max_iter"

def print_journal_newton(journal, title=""):
    if title:
        print(f"\n=== {title} ===")
    print(f"{'k':>3} | {'x':>14} | {'f(x)':>14} | {'f\'(x)':>14} | {'шаг':>10}")
    print("-" * 70)
    for row in journal:
        print(f"{row['iter']:>3} | {row['x']:>14.10f} | {row['f(x)']:>14.3e} | "
              f"{row['f\'(x)']:>14.3e} | {row['step']:>10.2e}")
        
def print_journal_secant(journal, title=""):
    if title:
        print(f"\n=== {title} ===")
    print(f"{'k':>3} | {'x_prev':>14} | {'x_curr':>14} | {'f_curr':>14} | {'шаг':>10}")
    print("-" * 70)
    for row in journal:
        print(f"{row['iter']:>3} | {row['x_prev']:>14.10f} | {row['x_curr']:>14.10f} |"
              f"{row['f_curr']:>14.3e} | {row['step']:>10.2e}")


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
    return x**3 - 2 * x + 2



x = np.linspace(-3, 3, 100)
plt.figure(figsize=(10, 6))
plt.plot(x, f_pract1(x), 'b-', linewidth=2, label=r'$f(x) = x^3 - 2x + 2$')
plt.axhline(0, color='black', linewidth=1)   # ось OX
plt.axvline(0, color='black', linewidth=1)
plt.tight_layout()
plt.show()

f1  = lambda x: x**3 - 2 * x + 2
df1 = lambda x: 3*x**2 - 2
root_n, jn, _ = newton(f1, df1, x0=-2, eps=1e-12)
root_s, js, _ = secant(f1, x0=-2.0, x1=-1.0, eps=1e-12)
print_journal_newton(jn, "Ньютон: f(x) = x³ − x − 1,  x₀ = 1,5")
print(f"корень = {root_n:.12f},  итераций: {len(jn)}")
print_journal_secant(js, "Секущие: f(x) = x³ − x − 1,  x₀ = -2.0, x₁ = -1.0")
print(f"корень = {root_s:.12f},  итераций: {len(js)}")

root1, j1, s1 = bisection(f_pract1, -2.0, -1.0, eps=1e-9)
print_journal(j1, "f(x) = x^3 - 6x^2 + 11x - 6,  [-2.0, -1.0]")
print(f"корень: {root1:.12f},  f(root) = {f_pract1(root1):.3e},  статус: {s1}")