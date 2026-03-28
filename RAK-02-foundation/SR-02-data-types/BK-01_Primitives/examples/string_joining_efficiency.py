"""
LAB PRACTICAL: String Concatenation Efficiency
Standard: PPM V4 - Gold Standard

Tujuan: Membuktikan perbedaan performa antara operator `+` dan `.join()` pada loop besar.
Guna: Menghindari degenerasi performa O(n^2) pada pemrosesan teks.
"""

import time

def benchmark_concatenation(n):
    print(f"--- Benchmarking {n:,} concatenations ---")
    
    # 1. Menggunakan operator + (Kurang Efisien)
    start_time = time.time()
    s = ""
    for i in range(n):
        s += "a"
    end_time = time.time()
    plus_duration = end_time - start_time
    print(f"   Operator '+': {plus_duration:.4f} seconds")

    # 2. Menggunakan method .join() (Efisien)
    start_time = time.time()
    list_of_chars = []
    for i in range(n):
        list_of_chars.append("a")
    s = "".join(list_of_chars)
    end_time = time.time()
    join_duration = end_time - start_time
    print(f"   Method '.join()': {join_duration:.4f} seconds")

    if join_duration > 0:
        improvement = plus_duration / join_duration
        print(f"\n   ⭐️ RESULT: '.join()' is approx {improvement:.1f}x faster.")
    print("-" * 60)

if __name__ == "__main__":
    # Gunakan angka 100.000 untuk melihat perbedaan nyata
    benchmark_concatenation(100_000)
