import matplotlib.pyplot as plt
import random
import math


def generate_points(num_points):
    points = []
    for _ in range(num_points):
        points.append((random.uniform(0, 3.2), random.uniform(0, 3.2)))
    return points


def estimate_square(points):
    points_inside_circle = 0
    for i in points:
        x = i[0]
        y = i[1]
        if ((x - 1) ** 2 + (y - 1) ** 2 <= 1 and (x - 1.5) ** 2 + (y - 2) ** 2 <= 1.25 and (x - 2) ** 2 + (y - 1.5) ** 2 <= 1.25):
            points_inside_circle += 1
    square_estimate = 10.24 * points_inside_circle / len(points)
    return square_estimate


def calculate_error(estimated_square):
    sq = 0.25 * math.pi + 1.25 * math.asin(0.8) - 1
    error = abs(estimated_square - sq) / sq * 100
    return error


square_values = []
errors = []
for num_points in range(100, 100001, 500):
    points = generate_points(num_points)
    square_value = estimate_square(points)
    square_values.append(square_value)
    error = calculate_error(square_value)
    errors.append(error)

points_range = range(100, 100001, 500)

print("Исходные данные, использованные для построения графиков:")
print(f"Количество точек: {[i for i in points_range]}")
print(f"Приближенное значение площади фигуры: {square_values}")
print(f"Относительное отклонение (в %): {errors}")

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(points_range, square_values, marker='o', linestyle='-', color='b')
plt.axhline(y = 0.25 * math.pi + 1.25 * math.asin(0.8) - 1, color='r', linestyle='--', label='Точная площадь')
plt.title('Приближенное значение площади фигуры от количества точек')
plt.xlabel('Количество точек')
plt.ylabel('Приближенное значение площади фигуры')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(points_range, errors, marker='o', linestyle='-', color='g')
plt.title('Относительное отклонение (в %) от количества точек')
plt.xlabel('Количество точек')
plt.ylabel('Относительное отклонение (в %)')

plt.tight_layout()
plt.show()



