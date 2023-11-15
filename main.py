import os
from concurrent.futures import ThreadPoolExecutor
from execution_time import *

folder_path = 'books'


def process_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    text = text.replace('\n', '').lower()

    letter_frequency = {}
    for letter in text:
        if letter.isalpha():
            if letter in letter_frequency:
                letter_frequency[letter] += 1
            else:
                letter_frequency[letter] = 1

    return letter_frequency


@execution_time
def process_files(folder_path):
    file_list = os.listdir(folder_path)

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(process_file, os.path.join(folder_path, file_name)) for file_name in file_list]
        letter_frequency = {}
        for future in futures:
            result = future.result()
            for letter, frequency in result.items():
                if letter in letter_frequency:
                    letter_frequency[letter] += frequency
                else:
                    letter_frequency[letter] = frequency
    
    return letter_frequency

result = process_files(folder_path)

for letter, frequency in result.items():
    print(f"Буква {letter}: {frequency} раз(а)")


