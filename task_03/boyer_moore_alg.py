
def bad_char_heuristic(pattern):
    bad_char = {}

    for i, char in enumerate(pattern):
        bad_char[char] = i

    return bad_char


def good_suffix_heuristic(pattern):
    m = len(pattern)
    good_suffix = [0] * (m + 1)
    border_pos = [-1] * (m + 1)
    i = m
    j = m + 1
    border_pos[i] = j

    while i > 0:
        while j <= m and pattern[i - 1] != pattern[j - 1]:
            if good_suffix[j] == 0:
                good_suffix[j] = j - i
            j = border_pos[j]
        i -= 1
        j -= 1
        border_pos[i] = j

    j = border_pos[0]
    for i in range(m + 1):
        if good_suffix[i] == 0:
            good_suffix[i] = j
        if i == j:
            j = border_pos[j]

    return good_suffix

def boyer_moore_search(text: str, pattern:str) -> list:
    bad_char = bad_char_heuristic(pattern)
    m = len(pattern)
    n = len(text)
    s = 0
    results = []

    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            results.append(s)
            s += (m - bad_char.get(text[s + m], -1)) if s + m < n else 1
        else:
            bad_char_shift = j - bad_char.get(text[s + j], -1)
            s += max(bad_char_shift, 1)

    return results
