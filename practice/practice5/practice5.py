import timeit
import matplotlib.pyplot as plt

sizes = [100, 1000, 10000]
target = -1  # Элемент отсутствует в коллекции (худший случай для list)

times_list = []
times_set = []

print("Результаты бенчмарка (время проверок в микросекундах):")

for n in sizes:
    # Данные
    data_list = list(range(n))
    data_set = set(range(n))
    
    # Строки для timeit
    stmt_list = "target in data_list"
    stmt_set = "target in data_set"    
    globals= {"target": target, "data_list": data_list, "data_set": data_set}
    
    # Замеры: 5 временных, 1000 итераций
    t_list_repeated = timeit.repeat(stmt_list, globals=globals, number=1000, repeat=5)
    t_set_repeated = timeit.repeat(stmt_set, globals=globals, number=1000, repeat=5)
    
    # Выбор лучшего замера 
    best_list = (min(t_list_repeated) / 1000) * 1_000_000
    best_set = (min(t_set_repeated) / 1000) * 1_000_000
    
    times_list.append(best_list)
    times_set.append(best_set)
    
    # Во сколько раз set быстрее
    ratio = best_list / best_set if best_set > 0 else 0
    print(f"n = {n:5d} | list: {best_list:8.2f} мкс | set: {best_set:8.2f} мкс | set быстрее в {ratio:6.1f} раз")


fig, ax = plt.subplots(figsize=(9, 5))

ax.plot(sizes, times_list, marker='o', label="list — O(n)", linewidth=2, color="crimson")
ax.plot(sizes, times_set, marker='s', label="set — O(1)", linewidth=2, color="seagreen")

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("Размер коллекции (n, лог. шкала)", fontsize=12)
ax.set_ylabel("Время одной проверки (мкс, лог. шкала)", fontsize=12)
ax.set_title("Сравнение производительности: x in list vs x in set", fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, which="both", alpha=0.3)

plt.tight_layout()
plt.show()