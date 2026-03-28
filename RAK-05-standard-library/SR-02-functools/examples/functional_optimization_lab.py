"""
LAB PRACTICAL: Functional Optimization (lru_cache & partial)
Standard: PPM V4 - Gold Standard

Tujuan: Memahami percepatan algoritma melalui memoization dan spesialisasi fungsi.
Guna: Optimasi algoritma rekursif dan penulisan kode yang lebih modular.
"""

import time
from functools import lru_cache, partial, wraps

def measure_time(func):
    """Decorator to measure execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"   [TIME] {func.__name__}({args[0]}) took {end - start:.6f}s")
        return result
    return wrapper

# 1. THE FIBONACCI BATTLE
def fib_naive(n):
    if n < 2: return n
    return fib_naive(n-1) + fib_naive(n-2)

@lru_cache(maxsize=None)
@measure_time
def fib_optimized(n):
    # This wrapper is slightly tricky for recursion, but educational
    def _fib(k):
        if k < 2: return k
        return _fib(k-1) + _fib(k-2)
    return _fib(n)

# Cleaner recursive cache
@lru_cache(maxsize=128)
def fib_recursive_cached(n):
    if n < 2: return n
    return fib_recursive_cached(n-1) + fib_recursive_cached(n-2)

def run_lab():
    print("=" * 60)
    print("🚀 PYTHON FUNCTIONAL OPTIMIZATION LAB")
    print("=" * 60)

    # 1. The Power of Memoization
    print("\n1. Memoization: Fibonacci(33)")
    
    start_naive = time.time()
    res_naive = fib_naive(33)
    end_naive = time.time()
    print(f"   [RESULT] Naive: {res_naive} (Time: {end_naive - start_naive:.4f}s)")

    start_cached = time.time()
    res_cached = fib_recursive_cached(33)
    end_cached = time.time()
    print(f"   [RESULT] Cached: {res_cached} (Time: {end_cached - start_cached:.6f}s)")
    print("   [INFO] Output: Cached version is virtually instantaneous.")

    # 2. Composition with Partial
    print("\n2. Partial: Binary/Hex Converters")
    
    # int(str, base=10)
    from_binary = partial(int, base=2)
    from_hex = partial(int, base=16)
    
    print(f"   [DATA] Binary '1010' -> {from_binary('1010')}")
    print(f"   [DATA] Hex 'FF' -> {from_hex('FF')}")

    # 3. Wraps and Metatdata
    print("\n3. Metadata: The Importance of @wraps")
    @measure_time
    def my_logic(x):
        """Important docstring."""
        return x * x
    
    print(f"   [META] Function Name: {my_logic.__name__}")
    print(f"   [META] Docstring: {my_logic.__doc__}")

    print("\n" + "=" * 60)
    print("✅ Lab Completed. Use lru_cache for repetitive recursion and partial for reusable tools.")

if __name__ == "__main__":
    run_lab()
