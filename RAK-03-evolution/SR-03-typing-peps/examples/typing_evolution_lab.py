"""
LAB PRACTICAL: Typing Evolution (PEPs 484, 526, 695)
Standard: PPM V4 - Gold Standard

Tujuan: Memahami perjalanan Python menuju Static Type Safety.
Guna: Membangun basis kode yang terdokumentasi dan aman.
"""

import sys
from typing import List, Union

def check_version(required_v):
    """Utility to guard version-specific features."""
    return sys.version_info >= required_v

# 1. PEP 484: Function Annotations (Python 3.5+)
def calculate_area(radius: float) -> float:
    """Standard function hints."""
    import math
    return math.pi * (radius ** 2)

def run_lab():
    print("=" * 60)
    print("🚀 PYTHON TYPING EVOLUTION LAB")
    print("=" * 60)

    # 1. PEP 484 demo
    print(f"\n1. PEP 484: Function Type Hints")
    radius = 5.0
    area = calculate_area(radius)
    print(f"   [RESULT] Area for radius {radius}: {area:.2f}")

    # 2. PEP 526: Variable Annotations (Python 3.6+)
    print(f"\n2. PEP 526: Variable Annotations")
    if check_version((3, 6)):
        # Local variable annotation
        user_scores: List[int] = [80, 90, 85]
        print(f"   [RESULT] User scores: {user_scores}")
    else:
        print("   [SKIP] Variable annotations require Python 3.6+")

    # 3. PEP 695: Modern Generic Syntax (Python 3.12+)
    print(f"\n3. PEP 695: Modern Type Parameter Syntax")
    if check_version((3, 12)):
        # We use eval/exec to protect compatibility
        modern_typing_code = """
# Modern Type Alias (PEP 695)
type Coordinate = tuple[float, float]

# Modern Generic Class (PEP 695)
class Box[T]:
    def __init__(self, content: T):
        self.content = content

def show_modern():
    my_box = Box[int](42)
    point: Coordinate = (10.5, 20.5)
    print(f"   [RESULT] Modern Box contains: {my_box.content}")
    print(f"   [RESULT] Modern Coordinate: {point}")

show_modern()
"""
        exec(modern_typing_code)
    else:
        print("   [SKIP] PEP 695 (bracketed generics) requires Python 3.12+")

    print("\n" + "=" * 60)
    print("✅ Lab Completed.")

if __name__ == "__main__":
    run_lab()
