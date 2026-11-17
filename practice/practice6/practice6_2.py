import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
points = rng.uniform(-2, 2, size=(200, 2))

# Масштаб: sx = 1.5, sy = 0.5
T_scale = np.array([
    [1.5, 0.0],
    [0.0, 0.5]
])
# Поворот на 60 градусов против часовой стрелки
theta = np.deg2rad(60)
T_rotate = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])
# Вектор переноса
t_vector = np.array([1.0, -1.0])

scaled = points @ T_scale.T
rotated = scaled @ T_rotate.T
transformed = rotated + t_vector

# Восстановление исходных точек 
step_back_translated = transformed - t_vector
# Обратный поворот на -60 градусов
theta_inv = np.deg2rad(-60)
T_rotate_inv = np.array([
    [np.cos(theta_inv), -np.sin(theta_inv)],
    [np.sin(theta_inv),  np.cos(theta_inv)]
])
step_back_rotated = step_back_translated @ T_rotate_inv.T
# Обратный масштаб: sx = 1/1.5, sy = 1/0.5
T_scale_inv = np.array([
    [1.0 / 1.5, 0.0       ],
    [0.0,       1.0 / 0.5 ]
])
recovered = step_back_rotated @ T_scale_inv.T

# Проверка через np.allclose с точностью 1e-12
is_equal = np.allclose(recovered, points, atol=1e-12)
print("Восстановленные точки совпадают с исходными (1e-12):", is_equal)

plt.figure(figsize=(8, 8))
plt.scatter(points[:, 0], points[:, 1], color='black', alpha=0.5, label='Исходные', s=25)
plt.scatter(transformed[:, 0], transformed[:, 1], color='crimson', alpha=0.5, label='Преобразованные', s=25)
plt.scatter(recovered[:, 0], recovered[:, 1], color='dodgerblue', alpha=0.3, label='Восстановленные', s=10)

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal')
plt.grid(True, alpha=0.3)
plt.legend()
plt.title('Композиция преобразований (матрицы 2x2 + вектор переноса)')
plt.xlabel('X')
plt.ylabel('Y')
plt.tight_layout()
plt.show()