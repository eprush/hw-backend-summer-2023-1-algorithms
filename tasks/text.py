from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    if text == "":
        return None, None

    arr = text.split()
    min_word, max_word = arr[0], arr[0]
    for word in arr:
        if len(word) > len(max_word):
            max_word = word
        elif len(word) < len(min_word):
            min_word = word
    if min_word == max_word:
        return None, None
    return min_word, max_word
