"""
LAB PRACTICAL: Lazy Data Pipelines (itertools)
Standard: PPM V4 - Gold Standard

Tujuan: Memahami efisiensi pemrosesan data 'malas' (Lazy Evaluation).
Guna: Menangani dataset masif tanpa meledakkan RAM.
"""

import itertools
import sys

def run_lab():
    print("=" * 60)
    print("🚀 PYTHON ITERTOOLS PIPELINE LAB")
    print("=" * 60)

    # 1. INFINITE STREAMS (Generating data on-the-fly)
    print("\n1. Infinite: ID Generation & Cycling")
    ids = itertools.count(1001)
    print(f"   [DATA] Generated IDs: {next(ids)}, {next(ids)}, {next(ids)}")
    
    colors = itertools.cycle(["RED", "GREEN", "BLUE"])
    print(f"   [DATA] Round-robin: {[next(colors) for _ in range(5)]}")

    # 2. COMBINATORICS (The end of nested loops)
    print("\n2. Combinatorics: Size X Color Grid")
    sizes = ["S", "M"]
    palette = ["Black", "White"]
    
    # Replacement for: for s in sizes: for c in palette: ...
    grid = list(itertools.product(sizes, palette))
    print(f"   [RESULT] Cartesian Grid: {grid}")

    # 3. PIPELINE MEMORY EFFICIENCY (chain vs addition)
    print("\n3. Performance: Memory-safe Chaining")
    large_a = range(1_000_000)
    large_b = range(1_000_000)
    
    # Chain doesn't copy data
    pipe = itertools.chain(large_a, large_b)
    print(f"   [INFO] Chain created instanty for 2 million items.")
    print(f"   [DATA] Memory of Chain Object: {sys.getsizeof(pipe)} bytes")
    
    # 4. DATA GROUPING (Requires sorting)
    print("\n4. Grouping: Sorting & Aggregating")
    logs = [
        {"level": "INFO", "msg": "Start"},
        {"level": "ERROR", "msg": "Fail"},
        {"level": "INFO", "msg": "Process"},
    ]
    # Sort by 'level' first!
    sorted_logs = sorted(logs, key=lambda x: x["level"])
    
    print("   [RESULT] Log Grouping:")
    for level, group in itertools.groupby(sorted_logs, key=lambda x: x["level"]):
        print(f"      - {level}: {len(list(group))} entries")

    print("\n" + "=" * 60)
    print("✅ Lab Completed. Use Itertools for any dataset larger than your RAM.")

if __name__ == "__main__":
    run_lab()
