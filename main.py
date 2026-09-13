from operations.basic import add, subtract, divide  # <-- добавили divide
from operations.advanced import multiply, power_of_sum

def main():
    print("=== Умный калькулятор ===")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"(2 + 3)^3 = {power_of_sum(2, 3, 3)}")
    # === ДОБАВЬ ЭТИ СТРОКИ ===
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"5 / 0 = {divide(5, 0)}")

if __name__ == "__main__":
    main()