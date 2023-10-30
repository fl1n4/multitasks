import argparse
import multiprocessing
import os
from typing import List


def search_keyword_in_file(keyword: str, filename: str) -> None:
    """Поиск ключевого слова в указанном текстовом файле."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line_number, line in enumerate(lines, start=1):
                if keyword in line:
                    print(f"Found '{keyword}' in '{filename}'")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred while searching in '{filename}': {e}")

def main() -> None:
    """Главная функция для распараллеливания поиска ключевого слова в нескольких текстовых файлах. """
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", type=str)
    parser.add_argument("files", nargs='+', type=str)
    args = parser.parse_args()

    with multiprocessing.Pool() as pool:
        pool.starmap(search_keyword_in_file, [(args.keyword, file) for file in args.files])

if __name__ == "__main__":
    main()