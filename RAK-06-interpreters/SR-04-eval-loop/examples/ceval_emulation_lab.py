"""
LAB PRACTICAL: Pure Python Stack Machine Emulation
Standard: PPM V4 - Gold Standard

Tujuan: Memahami bagaimana ceval.c mengoperasikan instruksi bytecode.
Guna: Mendekonstruksi mekanisme PVM tanpa harus membaca kode C yang rumit.
"""

import sys

class TinyPVM:
    """Emulasi sederhana dari Python Virtual Machine (PVM)."""
    def __init__(self):
        self.stack = []    # Value Stack
        self.variables = {} # Locals/Globals

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def run(self, bytecode):
        print("=" * 60)
        print("🚀 TINY PVM EMULATION START")
        print("=" * 60)
        
        for instruction, arg in bytecode:
            print(f"   [EXEC] {instruction:<12} | Arg: {arg:<5} | Stack: {self.stack}")
            
            if instruction == "LOAD_CONST":
                self.push(arg)
            elif instruction == "LOAD_NAME":
                self.push(self.variables.get(arg, 0))
            elif instruction == "STORE_NAME":
                self.variables[arg] = self.pop()
            elif instruction == "BINARY_ADD":
                b = self.pop()
                a = self.pop()
                self.push(a + b)
            elif instruction == "PRINT_EXPR":
                print(f"\n   [RESULT] >> {self.pop()}\n")
            else:
                print(f"   [ERROR] Unknown Opcode: {instruction}")

        print("✅ PVM Halt. Final State:", self.variables)
        print("=" * 60)

def main():
    # Simulasi perhitungan: res = (10 + 5) * 2 (Sederhanakan ke ADD saja)
    # Bytecode:
    # 1. LOAD_CONST 10
    # 2. LOAD_CONST 5
    # 3. BINARY_ADD
    # 4. STORE_NAME res
    # 5. LOAD_NAME res
    # 6. PRINT_EXPR
    
    opcodes = [
        ("LOAD_CONST", 10),
        ("LOAD_CONST", 5),
        ("BINARY_ADD", None),
        ("STORE_NAME", "res"),
        ("LOAD_NAME", "res"),
        ("PRINT_EXPR", None)
    ]

    pvm = TinyPVM()
    pvm.run(opcodes)

if __name__ == "__main__":
    main()
