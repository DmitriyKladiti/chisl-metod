import numpy as np
import matplotlib.pyplot as plt


angles = 2 * np.pi * np.arange(6) / 6
hex = np.column_stack([np.cos(angles), np.sin(angles)])

hex = np.vstack([hex, hex[0]])


# ── 2. Матрицы преобразований ──────────────────────────────
theta = np.deg2rad(45)   # поворот на 45 градусов
rotate = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)],
])
reflect_x = np.array([
    [0.0,  1.0],
    [1.0, 0.0],
])

# ── 3. Применяем преобразования ────────────────────────────
combined = reflect_x @ rotate 
rotated   = hex @ rotate
reflected = hex @ reflect_x
combined_pts = hex @ reflect_x

# ── 4. Визуализация ───────────────────
fig2, ax2 = plt.subplots(figsize=(7, 7))
ax2.plot(hex[:, 0], hex[:, 1], 'o-', color='gray',
         label='исходный', lw=2, markersize=8)
ax2.plot(rotated[:, 0], rotated[:, 1], 'o-', color='steelblue',
         label='поворот 45°', lw=2, markersize=8)
ax2.plot(combined_pts[:, 0], combined_pts[:, 1], 'o-', color='crimson',
         label='композиция', lw=2, markersize=8)
ax2.axhline(0, color='black', lw=0.5)
ax2.axvline(0, color='black', lw=0.5)
ax2.set_aspect('equal')
ax2.grid(True, alpha=0.3)
ax2.legend()
ax2.set_title('Исходный квадрат и его преобразования')
plt.tight_layout()
plt.show()





