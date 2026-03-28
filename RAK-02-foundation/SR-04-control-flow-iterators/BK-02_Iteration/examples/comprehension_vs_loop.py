"""
LAB PRACTICAL: For Loop vs List Comprehension
Standard: PPM V4 - Gold Standard

Tujuan: Membuktikan efisiensi sintaks dan performa List Comprehension.
Guna: Memilih cara paling Pythonic untuk membuat koleksi data baru.
"""

import time

def benchmark_construction(n):
    print("=" * 60)
    print(f"⚡ CONSTRUCTION BENCHMARK: For Loop vs Comprehension")
    print(f"Data Volume: {n:,} elements")
    print("=" * 60)

    # 1. Standard For Loop
    start_time = time.perf_counter()
    list_for = []
    for i in range(n):
        list_for.append(i**2)
    end_time = time.perf_counter()
    for_duration = (end_time - start_time) * 1000 # in ms
    print(f"🏗️ Standard For Loop: {for_duration:.4f} ms")

    # 2. List Comprehension
    start_time = time.perf_counter()
    list_comp = [i**2 for i in range(n)]
    end_time = time.perf_counter()
    comp_duration = (end_time - start_time) * 1000 # in ms
    print(f"🪄 List Comprehension: {comp_duration:.4f} ms")

    if comp_duration > 0:
        improvement = for_duration / comp_duration
        print(f"\n   ⭐️ RESULT: Comprehension is approx {improvement:.1f}x faster.")
        print(f"   REASON: Comprehension is optimized at the C level within CPython.")

    print("=" * 60)
    print("✅ Audit Completed.")

if __name__ == "__main__":
    # Gunakan 100.000 elemen
    benchmark_construction(100_000)
