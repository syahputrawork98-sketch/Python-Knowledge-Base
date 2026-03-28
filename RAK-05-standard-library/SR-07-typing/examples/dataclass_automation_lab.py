"""
LAB PRACTICAL: Structured Data Models (dataclass & typing)
Standard: PPM V4 - Gold Standard

Tujuan: Memahami eliminasi boilerplate dan penegakan tipe (Type Safety).
Guna: Membangun model data yang bersih, aman, dan efisien.
"""

from dataclasses import dataclass, field
from typing import Protocol, runtime_checkable

# 1. THE ARCHITECTURE: Protocol (Structural Typing)
@runtime_checkable
class Entity(Protocol):
    """Membuktikan kontrak: Objek apa pun yang punya 'id' adalah Entity."""
    id: int
    def display(self) -> str: ...

# 2. THE DATA MODEL: Standard Class vs Dataclass
class ManualUser:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __repr__(self):
        return f"ManualUser(id={self.id}, name='{self.name}')"

@dataclass(frozen=True)
class SmartUser:
    id: int
    name: str
    points: int = 0
    tags: list = field(default_factory=list) # Memory safe default
    
    def display(self) -> str:
        return f"ID: {self.id} | User: {self.name}"

    def __post_init__(self):
        # Validasi bisnis setelah pembuatan
        if self.id <= 0:
            raise ValueError("ID must be positive.")

def run_lab():
    print("=" * 60)
    print("🚀 PYTHON DATA MODELS & TYPING LAB")
    print("=" * 60)

    # 1. Boilerplate Comparison
    print("\n1. Comparison: Manual vs Dataclass")
    m = ManualUser(1, "Alice")
    s = SmartUser(2, "Bob", points=100)
    
    print(f"   [MANUAL] {m}")
    print(f"   [SMART]  {s} (Auto-repr!)")

    # 2. Immutability (frozen=True)
    print("\n2. Safety: Immutability check")
    try:
        # s.name = "Charlie" # Uncommenting will raise FrozenInstanceError
        print("   [SAFE] SmartUser is frozen. No mutation allowed.")
    except Exception as e:
        print(f"   [ERROR] Mutation failed: {e}")

    # 3. Structural Typing (Protocol)
    print("\n3. Protocols: Duck Typing Formalized")
    def process_entity(obj: Entity):
        if isinstance(obj, Entity):
            print(f"   [PASS] {obj.display()} satisfies 'Entity' protocol.")
        else:
            print(f"   [FAIL] Object does not satisfy 'Entity' protocol.")

    process_entity(s) # SmartUser satisfies protocol by having id and display()

    print("\n" + "=" * 60)
    print("✅ Lab Completed. Use Dataclasses for models and Protocols for interfaces.")

if __name__ == "__main__":
    run_lab()
