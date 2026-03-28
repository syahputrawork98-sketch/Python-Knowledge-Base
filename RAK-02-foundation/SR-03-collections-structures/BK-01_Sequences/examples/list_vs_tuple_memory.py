"""
LAB PRACTICAL: List vs Tuple Memory Optimization
Standard: PPM V4 - Gold Standard

Tujuan: Membuktikan perbedaan alokasi memori antara List dan Tuple.
Guna: Memahami kapan harus memilih Tuple untuk efisiensi RAM pada data statis.
"""

import sys

def audit_memory_allocation(n):
    print("=" * 60)
    print(f"🧬 MEMORY AUDIT: Collections (n={n:,} elements)")
    print("=" * 60)

    # 1. Objek List (Over-allocated)
    list_obj = [i for i in range(n)]
    list_size = sys.getsizeof(list_obj)
    
    # 2. Objek Tuple (Fixed size)
    tuple_obj = tuple(list_obj)
    tuple_size = sys.getsizeof(tuple_obj)

    print(f"[List Size ] : {list_size:,} bytes")
    print(f"[Tuple Size] : {tuple_size:,} bytes")

    if list_size > tuple_size:
        diff = list_size - tuple_size
        percent = (diff / list_size) * 100
        print(f"\n   ⭐️ RESULT: Tuple is {percent:.1f}% smaller ({diff:,} bytes saved).")
        print("   REASON: List needs extra capacity for future append() operations.")
    
    print("-" * 60)

    # 3. Reference Stability
    print("CASE: Hash-ability")
    try:
        hash_count = {tuple_obj: "Saved!"}
        print(" ✅ Tuple is hashable (Can be a Dict Key).")
    except TypeError:
        print(" ❌ Tuple is NOT hashable.")

    try:
        hash_count = {list_obj: "Saved!"}
        print(" ✅ List is hashable.")
    except TypeError:
        print(" ❌ List is NOT hashable (Mutable).")

    print("=" * 60)
    print("✅ Audit Completed.")

if __name__ == "__main__":
    # Gunakan angka 10.000 elemen
    audit_memory_allocation(10_000)
