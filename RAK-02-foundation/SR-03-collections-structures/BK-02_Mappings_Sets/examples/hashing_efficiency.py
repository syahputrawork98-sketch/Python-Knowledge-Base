"""
LAB PRACTICAL: Hashing Search Efficiency (Big O)
Standard: PPM V4 - Gold Standard

Tujuan: Membuktikan perbedaan kecepatan pencarian antara List (Linear Search) 
       dan Set (Hash Search) pada volume data besar (n=100.000).
Guna: Mengetahui kapan harus mengonversi List ke Set untuk optimasi pencarian O(1).
"""

import time

def benchmark_search_speed(n):
    print("=" * 60)
    print(f"⚡ SEARCH BENCHMARK: List (O(n)) vs Set (O(1))")
    print(f"Data Volume: {n:,} elements")
    print("=" * 60)

    # Inisialisasi Data
    list_data = list(range(n))
    set_data = set(list_data)
    
    # Target pencarian (elemen terakhir untul skenario terburuk List)
    target = n - 1

    # 1. Benchmark List (Linear Search)
    start_time = time.perf_counter()
    found_list = target in list_data
    end_time = time.perf_counter()
    list_duration = (end_time - start_time) * 1000 # in ms
    print(f"🔍 List Lookup time: {list_duration:.6f} ms")

    # 2. Benchmark Set (Hash Search)
    start_time = time.perf_counter()
    found_set = target in set_data
    end_time = time.perf_counter()
    set_duration = (end_time - start_time) * 1000 # in ms
    print(f"⚡ Set Lookup time : {set_duration:.6f} ms")

    if set_duration > 0:
        improvement = list_duration / set_duration
        print(f"\n   ⭐️ RESULT: Set is approx {improvement:,.1f}x faster.")
        print(f"   REASON: Set uses Hashing (O(1)), List uses Linear Scanning (O(n)).")

    print("=" * 60)
    print("✅ Audit Completed.")

if __name__ == "__main__":
    # Gunakan 100.000 elemen
    benchmark_search_speed(100_000)
