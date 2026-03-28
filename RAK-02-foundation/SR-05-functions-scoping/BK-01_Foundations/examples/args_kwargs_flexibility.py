"""
LAB PRACTICAL: Function Argument Flexibility (*args, **kwargs)
Standard: PPM V4 - Gold Standard

Tujuan: Memahami fleksibilitas pengiriman argumen dalam Python.
Guna: Membangun fungsi yang dapat menerima input dinamis dan bersifat modular.
"""

def print_audit_report(title, *args, company="PythonHub", **kwargs):
    """
    Fungsi demonstrasi yang menggabungkan:
    1. Positional Arg (title)
    2. Variadic Args (*args)
    3. Keyword-only Default (company)
    4. Keyword Variadic (**kwargs)
    """
    print("=" * 60)
    print(f"📊 REPORT: {title.upper()}")
    print(f"🏢 Org   : {company}")
    print("=" * 60)
    
    # Menangani Positional Variadic (*args)
    if args:
        print("📝 Positional Overflow Items:")
        for i, item in enumerate(args, 1):
            print(f"   [{i}] {item}")
    
    # Menangani Keyword Variadic (**kwargs)
    if kwargs:
        print("\n🔑 Metadata attributes:")
        for key, value in kwargs.items():
            print(f"   - {key}: {value}")

    print("=" * 60)
    print("✅ Audit Segment Completed.")

def run_lab():
    # TEST 1: Minimal entry
    print_audit_report("Basic Report")

    # TEST 2: Positional overflow (*args)
    print_audit_report("Inventory", "Item A", "Item B", "Item C")

    # TEST 3: Metadata overflow (**kwargs)
    print_audit_report("Server Status", status="ONLINE", uptime="99.9%", region="ASIA")

    # TEST 4: Full Combination
    print_audit_report(
        "Complex Audit", 
        "Task 1", "Task 2", # Positional overflow
        company="Global-JS", # Override keyword default
        author="Antigravity", version="1.0" # Metadata overflow
    )

if __name__ == "__main__":
    run_lab()
