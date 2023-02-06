__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    even_sum, odd_sum = 0, 0
    for element in arr:
        if element%2 :
            odd_sum += element
        else:
            even_sum += element

    if not odd_sum:
        return 0
    return even_sum/odd_sum
