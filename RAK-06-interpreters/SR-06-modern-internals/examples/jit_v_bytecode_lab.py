"""
LAB PRACTICAL: Modern Internals (JIT & No-GIL)
Standard: PPM V4 - Gold Standard

Tujuan: Verifikasi status JIT dan No-GIL pada environment Python terbaru.
Guna: Memahami kesiapan aplikasi untuk eksekusi paralel sejati (True Parallelism).
"""

import sys
import time
import threading

def check_modern_features():
    print("=" * 60)
    print("🚀 PYTHON MODERN INTERNALS CHECK (3.13+)")
    print("=" * 60)

    # 1. CHECKING JIT STATUS
    print("\n1. JIT Compiler Status:")
    # sys.flags.jit is only available in builds with JIT enabled
    if hasattr(sys.flags, "jit"):
        print(f"   [STATUS] JIT is ACTIVE: {sys.flags.jit}")
    else:
        print("   [STATUS] JIT is NOT enabled in this build/version.")

    # 2. CHECKING NO-GIL STATUS (PEP 703)
    print("\n2. Free-threading (No-GIL) Status:")
    if hasattr(sys.flags, "nogil"):
        print(f"   [STATUS] Free-threading is ACTIVE: {sys.flags.nogil}")
    else:
        print("   [STATUS] Free-threading (No-GIL) is NOT available in this build.")

    # 3. PERFORMANCE SIMULATION (PARALLELISM)
    print("\n3. Parallelism Simulation (CPUs):")
    def cpu_bound_task(n):
        res = 0
        for i in range(n):
            res += i
        return res

    threads = []
    start = time.time()
    for i in range(2):
        t = threading.Thread(target=cpu_bound_task, args=(10**7,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    end = time.time()
    print(f"   [EXEC] Time taken for 2 threads: {end - start:.4f}s")
    
    if hasattr(sys.flags, "nogil") and sys.flags.nogil:
        print("   [NOTE] You are seeing TRUE parallelism (Multi-core)!")
    else:
        print("   [NOTE] You are still limited by the GIL (Single-core).")

    print("\n" + "=" * 60)
    print("✅ Lab Completed. Use sys.flags to inspect modern environment features.")

if __name__ == "__main__":
    check_modern_features()
