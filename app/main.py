import sys

from app.utils import get_arithmetic_result


def main() -> int:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    operation = input("Choose the operation (+, -, /, *): ")

    if num1.isdigit() and num2.isdigit():
        answer = get_arithmetic_result(int(num1), int(num2), operation)
        if answer is None:
            print("Invalid operation. Please try again.")
            return 1

        print(f"The answer is {answer}")
        return 0

    print("Invalid numbers. Please try again.")
    return 1


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
