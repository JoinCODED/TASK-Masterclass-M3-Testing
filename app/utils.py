import operator
from typing import Callable, Optional


def get_operator(op: str) -> Optional[Callable[[float, float], float]]:
    pass


def get_arithmetic_result(num1: float, num2: float, op: str) -> Optional[float]:
    func = get_operator(op)
    return func and func(num1, num2)
