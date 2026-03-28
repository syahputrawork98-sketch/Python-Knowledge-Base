"""
LAB PRACTICAL: Function Factory & Closures
Standard: PPM V4 - Gold Standard

Tujuan: Memahami mekanisme Closure (Enclosing Scope).
Guna: Menciptakan fungsi yang memiliki "memori" internal tanpa menggunakan Class.
"""

def multiplier_factory(n):
    """
    Fungsi luar (Enclosing) yang bertindak sebagai pabrik.
    n disimpan di dalam closure dari fungsi yang dihasilkan.
    """
    def multiply(x):
        # x diambil dari argumen lokal
        # n diambil dari enclosing scope (Closure)
        return x * n
    
    return multiply

def run_lab():
    print("=" * 60)
    print("🏭 FUNCTION FACTORY LAB: Closures")
    print("=" * 60)

    # 1. Menciptakan fungsi pelipat ganda 2
    times_two = multiplier_factory(2)
    # 2. Menciptakan fungsi pelipat ganda 10
    times_ten = multiplier_factory(10)

    # 3. Eksekusi
    print(f"CASE 1 (times_two): 5 * 2 = {times_two(5)}")
    print(f"CASE 2 (times_ten): 5 * 10 = {times_ten(5)}")

    print("-" * 60)

    # 4. Membedah Internal Closure
    print("🧬 Closure Internal Audit:")
    # __closure__ berisi sel yang menyimpan nilai 'n'
    closure_val = times_two.__closure__[0].cell_contents
    print(f"   Stored value in times_two closure: {closure_val}")
    
    print("=" * 60)
    print("✅ Lab Completed.")

if __name__ == "__main__":
    run_lab()
