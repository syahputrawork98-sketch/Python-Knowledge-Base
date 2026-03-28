"""
LAB PRACTICAL: Magic Methods & Operator Overloading
Standard: PPM V4 - Gold Standard

Tujuan: Memahami bagaimana Dunder Methods menghidupkan objek kustom.
Guna: Membuat objek yang bisa berinteraksi menggunakan operator standar (+, -, ==).
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 1. Representation for Developers
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    # 2. String representation for Users
    def __str__(self):
        return f"Vector(x={self.x}, y={self.y})"

    # 3. Addition Overloading (+)
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Can only add Vector to Vector")
        return Vector(self.x + other.x, self.y + other.y)

    # 4. Equality Overloading (==)
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y

    # 5. Length Overloading (len())
    def __len__(self):
        # Simplistic length demo (max of coordinates)
        return max(abs(self.x), abs(self.y))

def run_lab():
    print("=" * 60)
    print("🪄 MAGIC METHODS LAB: Vector Arithmetic")
    print("=" * 60)

    # Instantiation
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    # Audit 1: Representation
    print("Audit 1: Checking STR vs REPR")
    print(f"   __str__  : {v1}")
    print(f"   __repr__ : {v1!r}")

    # Audit 2: Operator Overloading (+)
    print("\nAudit 2: Checking Operator Overloading (+)")
    v3 = v1 + v2
    print(f"   {v1} + {v2} = {v3}")

    # Audit 3: Equality (==)
    print("\nAudit 3: Checking Equality (==)")
    v_copy = Vector(3, 4)
    print(f"   Is v1 == v2?     : {v1 == v2}")
    print(f"   Is v1 == v_copy? : {v1 == v_copy}")

    # Audit 4: Length (len())
    print("\nAudit 4: Checking Length (len())")
    print(f"   len({v1}) = {len(v1)} (max of x,y)")

    print("=" * 60)
    print("✅ Lab Completed.")

if __name__ == "__main__":
    run_lab()
