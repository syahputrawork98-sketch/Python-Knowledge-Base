"""
Lab 01: Python int Internals
Topik: Small Integer Cache, is vs ==, sys.getsizeof(), arbitrary precision
Source: https://docs.python.org/3/library/stdtypes.html#int
"""
import sys

# ============================================================
# 1. Small Integer Cache (-5 to 256)
# ============================================================
print("=== Small Integer Cache ===")
a = 256; b = 256
print(f"a = 256, b = 256: a is b → {a is b}")        # True (cached)

a = 257; b = 257
print(f"a = 257, b = 257: a is b → {a is b}")        # False (new object)
print(f"a = 257, b = 257: a == b → {a == b}")        # True (same value)

# Takeaway: NEVER use 'is' to compare integers. Always use '=='.

# ============================================================
# 2. Arbitrary Precision — no overflow
# ============================================================
print("\n=== Arbitrary Precision ===")
googol = 10 ** 100
print(f"10^100 = {googol}")
print(f"Size of 10^100 in memory: {sys.getsizeof(googol)} bytes")
print(f"Size of 10^1000: {sys.getsizeof(10 ** 1000)} bytes")
print(f"Size of plain int 0: {sys.getsizeof(0)} bytes")

# ============================================================
# 3. Memory grows with magnitude
# ============================================================
print("\n=== sys.getsizeof() — int grows in memory ===")
for exp in [0, 10, 100, 1000]:
    n = 10 ** exp
    print(f"  10^{exp:4d}: {sys.getsizeof(n):4d} bytes")

# ============================================================
# 4. int vs float identity — common gotcha
# ============================================================
print("\n=== int vs float identity ===")
x = 1000
y = 1000.0
print(f"1000 == 1000.0  → {x == y}")        # True (value equality)
print(f"1000 is 1000.0  → {x is y}")        # False (different types!)
print(f"type(x): {type(x)}, type(y): {type(y)}")
