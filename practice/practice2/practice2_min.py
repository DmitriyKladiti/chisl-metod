import math, mpmath

def experiment(f_bad, f_good, xs, f_exact):
    print(f"{'x':>10} | {'bad':>14} | {'good':>14} | "
          f"{'err_bad':>10} | {'err_good':>10}")
    print("-" * 78)
    for x in xs:
        b  = f_bad(x)
        g  = f_good(x)
        ex = f_exact(x)                    # независимый эталон
        eb = abs(b - ex) / abs(ex) if ex else float('inf')
        eg = abs(g - ex) / abs(ex) if ex else float('inf')
        print(f"{x:>10.0e} | {b:>14.8e} | {g:>14.8e} | "
              f"{eb:>10.2e} | {eg:>10.2e}")

# Пример: f(x) = (1 - cos x) / x^2
xs = [10**-10, 10**-12, 10**-14]
experiment(
    f_bad  = lambda x: (math.sqrt(1+x) - math.sqrt(x)) ,
    f_good = lambda x: (1 / (math.sqrt(1+x) + math.sqrt(x))),
    xs     = xs,
    f_exact= lambda x: float(math.sqrt(1+x) - math.sqrt(x))
)