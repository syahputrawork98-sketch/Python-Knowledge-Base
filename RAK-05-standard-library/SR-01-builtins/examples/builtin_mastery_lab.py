"""
LAB PRACTICAL: Builtins Mastery (Performance & Transformation)
Standard: PPM V4 - Gold Standard

Tujuan: Memahami efisiensi fungsi bawaan (map, filter, zip).
Guna: Memilih teknik transformasi data yang paling optimal.
"""

import timeit

def run_lab():
    print("=" * 60)
    print("🚀 PYTHON BUILTINS PERFORMANCE LAB")
    print("=" * 60)

    # Setup data
    data = list(range(1000))

    # 1. Transformation: Loop vs Comprehension vs Map
    print("\n1. Transformation: (x * 2)")
    
    def loop_math():
        res = []
        for x in data:
            res.append(x * 2)
        return res

    def comp_math():
        return [x * 2 for x in data]

    def map_math():
        return list(map(lambda x: x * 2, data))

    print(f"   [TIME] Loop: {timeit.timeit(loop_math, number=1000):.5f}s")
    print(f"   [TIME] Comprehension: {timeit.timeit(comp_math, number=1000):.5f}s")
    print(f"   [TIME] Map: {timeit.timeit(map_math, number=1000):.5f}s")

    # 2. Filtering: Filter vs Comprehension
    print("\n2. Filtering: (x % 2 == 0)")
    
    def comp_filter():
        return [x for x in data if x % 2 == 0]

    def builtin_filter():
        return list(filter(lambda x: x % 2 == 0, data))

    print(f"   [TIME] Comprehension: {timeit.timeit(comp_filter, number=1000):.5f}s")
    print(f"   [TIME] Filter: {timeit.timeit(builtin_filter, number=1000):.5f}s")

    # 3. Aggregation Magic: zip & enumerate
    print("\n3. Aggregation: zip & enumerate")
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 92, 78]
    
    print("   [RESULT] Enumerated Zip:")
    for i, (name, score) in enumerate(zip(names, scores)):
        print(f"      {i+1}. {name} scored {score}")

    # 4. Sorting with Keys
    print("\n4. Sorting: key manipulation")
    students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
    # Sort by score (index 1)
    sorted_students = sorted(students, key=lambda x: x[1])
    print(f"   [RESULT] Sorted by score: {sorted_students}")

    print("\n" + "=" * 60)
    print("✅ Lab Completed. Use Map/Filter for large C-level speeds, or Comprehensions for readability.")

if __name__ == "__main__":
    run_lab()
