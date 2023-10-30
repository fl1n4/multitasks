import argparse
import concurrent.futures
import requests
import os
from typing import List


def download_image(url: str) -> None:
    """Загружает изображение по заданному URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        filename = os.path.basename(url)
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {url}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download: {url}, Error: {e}")

def main() -> None:
    """функция для загрузки изображений из списка URL-адресов"""
    parser = argparse.ArgumentParser(description="Parallel Image Downloader")
    parser.add_argument("urls", nargs='+', type=str)
    args = parser.parse_args()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(download_image, args.urls)

if __name__ == "__main__":
    main()