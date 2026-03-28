"""
LAB PRACTICAL: Collections Performance (deque & defaultdict)
Standard: PPM V4 - Gold Standard

Tujuan: Memahami efisiensi struktur data alternatif (collections).
Guna: Optimasi antrean (queues) dan pengelompokan (grouping) data masif.
"""

import timeit
from collections import deque, defaultdict, Counter, namedtuple

def run_lab():
    print("=" * 60)
    print("🚀 PYTHON COLLECTIONS PERFORMANCE LAB")
    print("=" * 60)

    # 1. THE QUEUE BATTLE: List vs Deque
    print("\n1. Queue Performance: (Removing 1000 items from start)")
    
    def list_queue():
        l = list(range(10000))
        for _ in range(1000):
            l.pop(0) # O(n) operation per pop

    def deque_queue():
        d = deque(range(10000))
        for _ in range(1000):
            d.popleft() # O(1) operation per pop

    print(f"   [TIME] list.pop(0): {timeit.timeit(list_queue, number=100):.5f}s")
    print(f"   [TIME] deque.popleft(): {timeit.timeit(deque_queue, number=100):.5f}s")
    print("   [INFO] Deque win! Linked-list structure avoids element-shifting.")

    # 2. Grouping with defaultdict
    print("\n2. Grouping: Automating aggregation")
    raw_data = [("IT", "Alice"), ("HR", "Bob"), ("IT", "Charlie")]
    
    groups = defaultdict(list)
    for dept, name in raw_data:
        groups[dept].append(name)
        
    print(f"   [RESULT] Groups created: {dict(groups)}")

    # 3. Frequency Analysis with Counter
    print("\n3. Word Frequency: Analyzing text")
    text = "code code code python python internals"
    counts = Counter(text.split())
    print(f"   [RESULT] Most Common: {counts.most_common(2)}")

    # 4. Memory footprint: namedtuple vs Class
    print("\n4. Architecture: namedtuple for lightweight data")
    Point = namedtuple("Point", ["x", "y"])
    p = Point(10, 20)
    print(f"   [DATA] namedtuple instance: {p} (Accessed by p.x = {p.x})")

    print("\n" + "=" * 60)
    print("✅ Lab Completed. Use Deque for Queues and DefaultDict for Grouping logic.")

if __name__ == "__main__":
    run_lab()
