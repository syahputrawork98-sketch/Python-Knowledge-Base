"""
Lab 03: Numeric Operations & Numeric Tower
Topik: divmod, bitwise ops, type promotion, fractions
Source: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
"""
import fractions

# ============================================================
# 1. Integer Division — // vs / vs divmod()
# ============================================================
print("=== Division Operators ===")
print(f"17 / 5  = {17 / 5}")      # 3.4  — true division (always float)
print(f"17 // 5 = {17 // 5}")     # 3    — floor division
print(f"17 % 5  = {17 % 5}")      # 2    — modulo (remainder)
print(f"divmod(17, 5) = {divmod(17, 5)}")  # (3, 2) — both at once

# Gotcha with negative numbers (floor, not truncate)
print(f"-7 // 2 = {-7 // 2}")     # -4 (floor toward -inf), NOT -3!
print(f"-7 % 2  = {-7 % 2}")      # 1 (always same sign as divisor)

# ============================================================
# 2. Bitwise Operators on int
# ============================================================
print("\n=== Bitwise Operations ===")
a, b = 0b1010, 0b1100   # 10, 12 in binary
print(f"a & b (AND)  = {a & b:04b} = {a & b}")
print(f"a | b (OR)   = {a | b:04b} = {a | b}")
print(f"a ^ b (XOR)  = {a ^ b:04b} = {a ^ b}")
print(f"~a    (NOT)  = {~a}")              # -11 (two's complement)
print(f"a << 1 (left shift)  = {a << 1}") # 20 (multiply by 2)
print(f"a >> 1 (right shift) = {a >> 1}") # 5  (divide by 2)

# ============================================================
# 3. Numeric Tower Promotion
# ============================================================
print("\n=== Numeric Tower (int → float → complex) ===")
print(f"type(1 + 2)    = {type(1 + 2)}")       # int
print(f"type(1 + 2.0)  = {type(1 + 2.0)}")     # float
print(f"type(1 + 2j)   = {type(1 + 2j)}")      # complex

# ============================================================
# 4. fractions.Fraction — Exact Rational Arithmetic
# ============================================================
print("\n=== fractions.Fraction (exact rational) ===")
f = fractions.Fraction(1, 3) + fractions.Fraction(2, 3)
print(f"1/3 + 2/3 = {f}")   # 1 — exact!
print(f"Type: {type(f)}")
