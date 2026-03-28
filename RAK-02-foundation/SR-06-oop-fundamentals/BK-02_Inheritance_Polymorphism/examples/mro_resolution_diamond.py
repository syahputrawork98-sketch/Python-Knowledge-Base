"""
LAB PRACTICAL: The Diamond Problem & MRO Solver
Standard: PPM V4 - Gold Standard

Tujuan: Memahami bagaimana Python menyelesaikan konflik pewarisan ganda.
Guna: Menghindari ambiguitas saat menggunakan Multiple Inheritance.
"""

class Base:
    def execute(self):
        print("🏠 Base: Entry Point")

class SubA(Base):
    def execute(self):
        print("🅰️ SubA: Pre-execute")
        super().execute() # Go to next in MRO
        print("🅰️ SubA: Post-execute")

class SubB(Base):
    def execute(self):
        print("🅱️ SubB: Pre-execute")
        super().execute() # Go to next in MRO
        print("🅱️ SubB: Post-execute")

class Diamond(SubA, SubB):
    """
    Kelas yang menyebabkan Diamond Problem.
    SubA dan SubB sama-sama mewarisi dari Base.
    """
    def execute(self):
        print("💎 Diamond: Starting Chain")
        super().execute()
        print("💎 Diamond: Chain Ended")

def run_lab():
    print("=" * 60)
    print("🪄 MRO RESOLUTION LAB (The Diamond)")
    print("=" * 60)

    # 1. Audit MRO
    print("Audit 1: Checking Method Resolution Order")
    mro_list = Diamond.__mro__
    for i, cls in enumerate(mro_list):
        print(f"   [{i}] {cls.__name__}")

    print("\nAudit 2: Executing Diamond.execute()")
    print("-" * 30)
    d = Diamond()
    d.execute()
    print("-" * 30)

    print("\n⭐️ INSIGHT:")
    print("   Meskipun SubA dan SubB sama-sama memanggil super(),")
    print("   Base.execute() hanya dijalankan SATU KALI.")
    print("   Ini membuktikan C3 Linearization menjaga integritas silsilah.")

    print("=" * 60)
    print("✅ Lab Completed.")

if __name__ == "__main__":
    run_lab()
