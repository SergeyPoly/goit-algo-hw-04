import random
import timeit
from sort_alhorithms import insertion_sort, merge_sort

# Підготовка даних для тестування
def generate_data(size, kind="random"):
    return [random.randint(1, 10000) for _ in range(size)]

# Функція для заміру часу виконання операції сортування
def benchmark_sorting_algorithms(size):
    data = generate_data(size)

    algorithms = {
        "Merge Sort": lambda: merge_sort(data.copy()),
        "Insertion Sort": lambda: insertion_sort(data.copy()),
        "Timsort (sort)": lambda: data.copy().sort(),
        "Timsort (sorted)": lambda: sorted(data.copy()),
    }

    results = {}

    for name, func in algorithms.items():
        time = timeit.timeit(func, number=1)
        results[name] = time

    print(f"Results for data size {size}:")

    for name, duration in results.items():
        print(f"{name}: {duration:.6f} seconds")

    print("-" * 50)

# Розміри масивів для тестування
data_sizes = [100, 1000, 10000]  

print("\nTesting sorting algorithms...\n")
for size in data_sizes:
    benchmark_sorting_algorithms(size)