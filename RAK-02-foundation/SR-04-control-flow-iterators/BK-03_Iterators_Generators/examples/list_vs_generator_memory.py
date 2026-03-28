"""
LAB PRACTICAL: List vs Generator Memory Consumption
Standard: PPM V4 - Gold Standard

Tujuan: Membuktikan efisiensi memori (Lazy Evaluation) pada Generator Expression.
Guna: Menghindari MemoryError saat memproses data berjumlah jutaan.
"""

import sys

def audit_memory_efficiency(n):
    print("=" * 60)
    print(f"🧬 MEMORY AUDIT: Eager (List) vs Lazy (Generator)")
    print(f"Data Volume: {n:,} elements")
    print("=" * 60)

    # 1. List Comprehension (Eager - Semua elemen di RAM)
    list_obj = [i**2 for i in range(n)]
    list_memory = sys.getsizeof(list_obj)
    print(f"🏗️ List Object Memory      : {list_memory:,} bytes")

    # 2. Generator Expression (Lazy - Hanya 1 elemen di RAM)
    gen_obj = (i**2 for i in range(n))
    gen_memory = sys.getsizeof(gen_obj)
    print(f"🪄 Generator Object Memory : {gen_memory:,} bytes")

    if list_memory > gen_memory:
        diff = list_memory - gen_memory
        improvement = list_memory / gen_memory
        print(f"\n   ⭐️ RESULT: Generator is {improvement:,.1f}x smaller.")
        print(f"   SAVED : {diff:,} bytes of RAM.")
        print("   REASON: Generator evaluates items one by one on demand.")
    
    print("-" * 60)

    # 3. Proving Yielding one-by-one
    print("CASE: Next Step Evaluation")
    print(f"   First Value  : {next(gen_obj)}")
    print(f"   Second Value : {next(gen_obj)}")
    print("   ... (Remaining values are still waiting to be produced)")

    print("=" * 60)
    print("✅ Audit Completed.")

if __name__ == "__main__":
    # Gunakan 10.000.000 (10 Juta) elemen untuk melihat perbedaan drastis
    audit_memory_efficiency(10_000_000)
