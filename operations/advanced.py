# Относительный импорт! Берём функции из соседнего файла basic.py
from .basic import add

def multiply(a, b):
    return a * b

def power_of_sum(a, b, power):
    # Используем функцию add из basic.py через относительный импорт
    total = add(a, b)
    return total ** power