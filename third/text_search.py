import timeit

from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rk_search import rabin_karp_search


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def test_search_algorithm(algorithm, text, pattern):
    start_time = timeit.default_timer()
    algorithm(text, pattern)
    return timeit.default_timer() - start_time


text1 = read_file('resources/file1.txt')
text2 = read_file('resources/file2.txt')

existing_substring = 'Література'
imaginary_substring = 'Гарі Поттер'

for text, text_name in [(text1, 'Text 1'), (text2, 'Text 2')]:
    for pattern, pattern_name in [(existing_substring, 'Existing substring'),
                                  (imaginary_substring, 'Imaginary substring')]:
        print(f"Testing on {text_name}, Substring: {pattern_name}")
        for algorithm in [boyer_moore_search, kmp_search, rabin_karp_search]:
            time = test_search_algorithm(algorithm, text, pattern)
            print(f"{algorithm.__name__}: {time} seconds")
        print()
