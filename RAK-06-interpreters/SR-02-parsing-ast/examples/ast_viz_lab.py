"""
LAB PRACTICAL: AST Visualization & Inspection
Standard: PPM V4 - Gold Standard

Tujuan: Memahami representasi internal kode Python sebagai pohon sintaks (AST).
Guna: Analisis statis kode (linting), pembuatan formatter, dan transformasi kode.
"""

import ast

def inspect_code(source_code: str):
    print("=" * 60)
    print("🚀 PYTHON AST INSPECTION LAB")
    print(f"Source Code: '{source_code}'")
    print("=" * 60)

    # 1. PARSING: String to AST Tree
    print("\n1. Parsing to AST...")
    tree = ast.parse(source_code)
    
    # 2. DUMPING: Structure Visualization
    print("\n2. Tree Structure (Detailed Dump):")
    print(ast.dump(tree, indent=4))

    # 3. SELECTIVE NODE ANALYSIS
    print("\n3. Selective Node Analysis:")
    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp):
            print(f"   [FOUND] BinOp: {node.op.__class__.__name__}")
        elif isinstance(node, ast.Constant):
            print(f"   [FOUND] Constant Value: {node.value}")
        elif isinstance(node, ast.Name):
            print(f"   [FOUND] Variable Reference: {node.id} ({node.ctx})")

    # 4. AST TO CODE: Re-generation
    print("\n4. Code Regeneration (AST -> Source):")
    try:
        regen_code = ast.unparse(tree) # Python 3.9+
        print(f"   [RESULT] {regen_code}")
    except AttributeError:
        print("   [SKIP] ast.unparse requires Python 3.9+")

    print("\n" + "=" * 60)
    print("✅ Lab Completed. Use ast.parse() to understand the code's intention.")

if __name__ == "__main__":
    # Test case: Dynamic Assignment
    sample = "res = (10 + 5) * 2"
    inspect_code(sample)
