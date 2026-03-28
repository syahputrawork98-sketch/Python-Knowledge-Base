"""
LAB PRACTICAL: PyObject & Reference Inspection
Standard: PPM V4 - Gold Standard

Tujuan: Memahami struktur fisik PyObject dan manajemen referensi.
Guna: Debugging kebocoran memori dan optimalisasi eksekusi C-API Python.
"""

import sys
import ctypes

def inspect_object(obj):
    print("=" * 60)
    print(f"🚀 INSPECTING PyObject: {obj} ({type(obj).__name__})")
    print("=" * 60)

    # 1. MEMORY ADDRESS (id())
    addr = id(obj)
    print(f"   [MEMORY] Memory Address: {hex(addr)}")

    # 2. REFERENCE COUNT (sys.getrefcount)
    # Catatan: getrefcount() selalu +1 dari aslinya karena ia meminjam referensi saat dipanggil.
    ref_count = sys.getrefcount(obj)
    print(f"   [REFC]   Reference Count: {ref_count - 1} (Effective)")

    # 3. DIRECT MEMORY ACCESS (ctypes)
    # Membaca ob_refcnt langsung dari struct C (64-bit systems)
    # struct _object { ssize_t ob_refcnt; ... }
    ref_from_mem = ctypes.c_ssize_t.from_address(addr).value
    print(f"   [C-LVL]  ob_refcnt from C-struct: {ref_from_mem}")

    # 4. TYPE OBJECT INSPECTION
    print("\n   [TYPE]   Type Object Anatomy:")
    print(f"      - tp_name: {type(obj).__name__}")
    print(f"      - tp_basicsize: {sys.getsizeof(obj)} bytes")

    print("\n" + "=" * 60)
    print("✅ Lab Completed. Use sys.getrefcount() to track object lifecycles.")

def ref_leak_simulation():
    print("\n--- Simulation: Reference Increases ---")
    a = [1, 2, 3] # Base ref: 1
    print(f"   [S1] List created. Ref: {sys.getrefcount(a)-1}")
    
    b = a # Ref: 2
    print(f"   [S2] Bound to 'b'. Ref: {sys.getrefcount(a)-1}")
    
    c = [a, a, a] # Ref: 5
    print(f"   [S3] Added to list 3 times. Ref: {sys.getrefcount(a)-1}")

if __name__ == "__main__":
    x = "Python DNA"
    inspect_object(x)
    ref_leak_simulation()
