from typing import Optional
import re
__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    p     = re.compile(r'\w+')
    words = p.findall(text)

    if not len(words):
        return None, None

    min_word, max_word = words[0], words[0]
    for word in words:
        if len(word)  < len(min_word):
            min_word = word
        elif len(word) > len(max_word):
            max_word = word
    return min_word, max_word
