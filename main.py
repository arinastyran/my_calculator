from rich.console import Console
from rich.panel import Panel

from operations.basic import add, subtract, divide
from operations.advanced import multiply, power_of_sum

console = Console()

def main():
    results = [
        f"5 + 3 = {add(5, 3)}",
        f"10 - 4 = {subtract(10, 4)}",
        f"6 * 7 = {multiply(6, 7)}",
        f"(2 + 3)^3 = {power_of_sum(2, 3, 3)}",
        f"10 / 2 = {divide(10, 2)}",
    ]
    text = "\n".join(results)
    console.print(Panel(text, title="🧮 Умный калькулятор", border_style="green"))

if __name__ == "__main__":
    main()