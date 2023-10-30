import argparse
import multiprocessing
import random
from typing import List


def estimate_pi(num_points: int) -> float:
    """Оценивает значение числа π методом Монте-Карло."""
    inside_circle = 0
    for _ in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return (inside_circle / num_points) * 4

def main() -> None:
    """ функция для распараллеливания оценки значения π методом Монте-Карло."""
    parser = argparse.ArgumentParser()
    parser.add_argument("num_points", type=int)
    args = parser.parse_args()

    num_processes = multiprocessing.cpu_count()
    num_points_per_process = args.num_points // num_processes

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(estimate_pi, [num_points_per_process] * num_processes)

    estimated_pi = sum(results) / num_processes
    print(f"Estimated value of pi using {args.num_points} points: {estimated_pi}")

if __name__ == "__main__":
    main()