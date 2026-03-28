"""
LAB PRACTICAL: Boolean Singleton & Integer Heritage
Standard: PPM V4 - Gold Standard

Tujuan: Membedah identitas memori (Singleton) dan sifat turunan integer pada True/False.
Guna: Memahami mengapa perbandingan identitas `is` bekerja pada Boolean.
"""

def audit_boolean_internals():
    print("=" * 60)
    print("🧪 CPYTHON BOOLEAN INTERNAL AUDIT")
    print("=" * 60)

    # 1. Singleton Check
    # Semua variabel yang berisi True merujuk ke alamat memori yang sama.
    a = True
    b = (10 > 5)
    print("CASE 1: Singleton Identity Check")
    print(f"   Value a (True)   : ID = {id(a)}")
    print(f"   Value b (10 > 5) : ID = {id(b)}")
    print(f"   Are they identical? (a is b) -> {a is b}")
    print("   RESULT : True and False are fixed Singleton objects.")

    print("-" * 60)

    # 2. Integer Heritage Check
    # Boolean adalah subclass dari int.
    print("CASE 2: Integer Subclass Check")
    print(f"   isinstance(True, int)  -> {isinstance(True, int)}")
    print(f"   True + True            -> {True + True} (1 + 1)")
    print(f"   False * 10             -> {False * 10} (0 * 10)")
    print("   RESULT : Booleans can be treated as 1 and 0 in math.")

    print("-" * 60)

    # 3. Identity vs Value
    # Mengapa 'is' berbahaya walau bekerja untuk Singleton.
    x = 1
    print("CASE 3: Identity Confusion (int vs bool)")
    print(f"   Equality (1 == True) -> {x == True}")
    print(f"   Identity (1 is True) -> {x is True}")
    print("   RESULT : Always use implicit 'if x:' or explicit '==' for values.")

    print("=" * 60)
    print("✅ Audit Completed.")

if __name__ == "__main__":
    audit_boolean_internals()
