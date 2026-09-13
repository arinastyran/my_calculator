# Абсолютный импорт! Полный путь от корня проекта
from operations.basic import add, subtract
from operations.advanced import multiply, power_of_sum

def main():
    print("=== Умный калькулятор ===")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"(2 + 3)^3 = {power_of_sum(2, 3, 3)}")

if __name__ == "__main__":
    main()