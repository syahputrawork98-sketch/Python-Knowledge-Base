"""
Lab 02: Python float Precision
Topik: IEEE 754, floating-point errors, decimal module, math.isclose()
Source: https://docs.python.org/3/library/floating-point.html
"""
import math
import decimal

# ============================================================
# 1. The Famous Floating-Point Bug
# ============================================================
print("=== IEEE 754 Precision Issue ===")
print(f"0.1 + 0.2 = {0.1 + 0.2}")           # 0.30000000000000004
print(f"0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}")  # False!
print(f"repr(0.1) = {repr(0.1)}")           # '0.1' (Python hides the full repr)
print(f"format(0.1, '.55f') = {format(0.1, '.55f')}")  # 0.1000000000000000055511151231257827021181583404541015625

# ============================================================
# 2. The Correct Way: math.isclose()
# ============================================================
print("\n=== Correct Comparison: math.isclose() ===")
result = 0.1 + 0.2
print(f"math.isclose(0.1+0.2, 0.3) = {math.isclose(result, 0.3)}")  # True
print(f"math.isclose(1.0, 1.0000001) = {math.isclose(1.0, 1.0000001)}")  # True (rel_tol=1e-9)
print(f"math.isclose(1.0, 1.001) = {math.isclose(1.0, 1.001)}")          # False

# ============================================================
# 3. decimal Module — Exact Decimal Arithmetic
# ============================================================
print("\n=== decimal.Decimal for financial calculations ===")
from decimal import Decimal, getcontext
getcontext().prec = 50  # 50 significant digits

a = Decimal("0.1")
b = Decimal("0.2")
print(f"Decimal('0.1') + Decimal('0.2') = {a + b}")  # 0.3 exactly
print(f"Equals 0.3? {a + b == Decimal('0.3')}")       # True

# ============================================================
# 4. float special values (IEEE 754)
# ============================================================
print("\n=== float Special Values ===")
inf = float("inf")
nan = float("nan")
print(f"inf > 10**1000: {inf > 10**1000}")
print(f"nan == nan: {nan == nan}")   # False! NaN is never equal to itself
print(f"math.isnan(nan): {math.isnan(nan)}")   # Use this instead
