"""
LAB PRACTICAL: Integer Interning & Memory Identity
Standard: PPM V4 - Gold Standard

Tujuan: Membedah mekanisme 'Small Integer Cache' (-5 s/d 256) pada CPython.
Guna: Memahami mengapa operator `is` berbahaya jika digunakan untuk perbandingan nilai numerik.
"""

import sys

def audit_interning_cache():
    print("=" * 60)
    print("🧠 CPYTHON INTEGER INTERNING AUDIT")
    print("=" * 60)

    # 1. Kasus di dalam Catch (Small Int Cache)
    a = 256
    b = 256
    print(f"CASE 1 (Inside Cache): n = 256")
    print(f"   Value  : {a} == {b} -> {a == b}")
    print(f"   Memory : {id(a)} is {id(b)} -> {a is b}")
    print("   RESULT : CPython uses pre-allocated object for 256.")

    print("-" * 60)

    # 2. Kasus di luar Cache
    x = 257
    y = 257
    print(f"CASE 2 (Outside Cache): n = 257")
    print(f"   Value  : {x} == {y} -> {x == y}")
    print(f"   Memory : {id(x)} is {id(y)} -> {x is y}")
    print("   RESULT : CPython creates two distinct objects in memory.")

    print("-" * 60)

    # 3. Arbitrary Precision (Unlimited Memory)
    huge_n = 10**100
    print(f"CASE 3 (Large Integer Growth): 10**100")
    print(f"   Value Length: {len(str(huge_n))} digits")
    print(f"   Memory Size : {sys.getsizeof(huge_n)} bytes")
    print("   RESULT : Python manages memory dynamically for big ints.")

    print("=" * 60)
    print("✅ Audit Completed.")

if __name__ == "__main__":
    audit_interning_cache()
