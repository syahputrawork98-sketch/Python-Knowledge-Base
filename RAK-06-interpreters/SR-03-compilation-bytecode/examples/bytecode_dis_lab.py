"""
LAB PRACTICAL: Bytecode Disassembly & Scoping
Standard: PPM V4 - Gold Standard

Tujuan: Memahami bagaimana source code berubah menjadi instruksi stack machine.
Guna: Optimasi performa dan pemahaman mendalam tentang eksekusi PVM.
"""

import dis
import symtable

def analyze_logic(source_code: str):
    print("=" * 60)
    print("🚀 PYTHON COMPILATION & BYTECODE LAB")
    print(f"Source Code:\n{source_code}")
    print("=" * 60)

    # 1. SYMBOL TABLE ANALYSIS
    print("\n1. Symbol Table Analysis (Static Scoping):")
    table = symtable.symtable(source_code, "lab_03.py", "exec")
    for sym in table.get_symbols():
        scope = "Local" if sym.is_local() else "Global"
        print(f"   [SYMBOL] {sym.get_name():<10} | Scope: {scope}")

    # 2. BYTECODE EMISSION
    print("\n2. Bytecode Emitter (The Opcodes):")
    # Compiling to a code object
    code_obj = compile(source_code, "lab_03.py", "exec")
    
    # Dissassembling the main block
    print("   [BLOCK] Main Execution Flow:")
    dis.dis(code_obj)

    # 3. CODE OBJECT INSPECTION
    print("\n3. Code Object Deep-Dive (Metadata):")
    # Finding the function code object in constants
    for const in code_obj.co_consts:
        if hasattr(const, "co_code"):
            print(f"   [FUNC] Inspecting Function Code Object:")
            print(f"      - co_varnames: {const.co_varnames}") # Local variables
            print(f"      - co_names   : {const.co_names}")    # Global/Attribute names
            print(f"      - co_consts  : {const.co_consts}")   # Literals
            break

    print("\n" + "=" * 60)
    print("✅ Lab Completed. Code is a tree of symbols flattened into opcodes.")

if __name__ == "__main__":
    test_code = """
global_val = 100
def calc(x):
    res = x + global_val
    return res
"""
    analyze_logic(test_code)
