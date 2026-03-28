"""
LAB PRACTICAL: The Executive Timer Decorator
Standard: PPM V4 - Gold Standard

Tujuan: Membangun decorator untuk mengukur waktu eksekusi fungsi.
Guna: Benchmarking fungsi tanpa mengubah logika internalnya.
"""

import time
from functools import wraps

def execution_timer(func):
    """
    Decorator yang mencatat waktu mulai dan selesai eksekusi fungsi.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        
        # Eksekusi fungsi asli
        result = func(*args, **kwargs)
        
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        
        print(f"⏱️ [TIMER] {func.__name__} took {elapsed:.6f} seconds.")
        return result
    return wrapper

@execution_timer
def complex_computation(n):
    """
    Simulasi beban kerja berat (Mencari total kuadrat).
    """
    return sum(i**2 for i in range(n))

def run_lab():
    print("=" * 60)
    print("🚀 DECORATOR PIT-STOP LAB: Execution Timer")
    print("=" * 60)

    # 1. Panggilan fungsi dengan decorator
    print("Executing computation (n=1,000,000)...")
    res = complex_computation(1_000_000)
    print(f"Result length: {len(str(res))} digits.")

    print("-" * 60)

    # 2. Verifikasi Metadata (@wraps check)
    print("🧬 Checking Function Metadata (via @wraps):")
    print(f"   Name   : {complex_computation.__name__}")
    print(f"   Doc    : {complex_computation.__doc__}")
    
    # Tanpa @wraps, name akan menjadi 'wrapper' dan doc akan menjadi None.
    print("=" * 60)
    print("✅ Lab Completed.")

if __name__ == "__main__":
    run_lab()
