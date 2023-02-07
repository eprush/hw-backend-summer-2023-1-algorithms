__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    if (not number) or (number == 1):
        return False

    for i in range(2, int(number**0.5)+1):
        if not number%i:
            return False
    return True
