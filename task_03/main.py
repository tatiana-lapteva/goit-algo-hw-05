"""
Порівняти ефективність алгоритмів пошуку підрядка: Боєра-Мура, 
Кнута-Морріса-Пратта та Рабіна-Карпа на основі двох текстових 
файлів (стаття 1, стаття 2). Використовуючи timeit, треба виміряти 
час виконання кожного алгоритму для двох видів підрядків: одного, 
що дійсно існує в тексті, та іншого — вигаданого (вибір підрядків 
за вашим бажанням). На основі отриманих даних визначити найшвидший 
алгоритм для кожного тексту окремо та в цілому.
"""

import timeit
from read_article import read_article
from rabin_karp_alg import rabin_karp_search
from boyer_moore_alg import boyer_moore_search
from kmp_alg import kmp_search
import matplotlib.pyplot as plt


def measure_time(search_function, text, pattern):
    start = timeit.default_timer()
    result = search_function(text, pattern)
    
    return timeit.default_timer() - start, result

if __name__ == "__main__":
    article1_text = read_article("article_1.txt")
    article2_text = read_article("article_2.txt")

    algorithms = [boyer_moore_search, kmp_search, rabin_karp_search]
    results = {alg.__name__: [] for alg in algorithms}

    # CASE 1 - pattern matched
    articles = [(article1_text, "найпростіший алгоритм пошуку"), (article2_text, "Графові моделі"), (article1_text, "нвоаипоек"), (article2_text, "нвоаипоек")]

    for article_text, pattern in articles:
          
         for alg in algorithms:
            time, position = measure_time(alg, article_text, pattern)
            results[alg.__name__].append(time)
            print(f"{alg.__name__} time: {time:.8f}")
            print(f"{alg.__name__} pattern matched at position: {position}")

    # Visualization
    num_articles = len(articles)
    fig, axes = plt.subplots(1, num_articles, figsize=(16, 10))

    for i, (article_text, pattern) in enumerate(articles):
        times = [results[alg.__name__][i] for alg in algorithms]
        algorithm_names = [alg.__name__ for alg in algorithms]

        ax = axes[i] if num_articles > 1 else axes
        ax.bar(algorithm_names, times, color='skyblue')
        ax.set_xlabel('Algorithm')
        ax.set_ylabel('Time (seconds)')
        ax.set_title(f'Pattern "{pattern}" in Article {i+1}')

    plt.tight_layout()
    plt.show()
