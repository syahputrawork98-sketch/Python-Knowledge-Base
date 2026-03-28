"""
LAB PRACTICAL: CPython Source Anatomy (The Machine Room Map)
Standard: PPM V4 - Gold Standard

Tujuan: Memahami hirarki fisik repositori CPython.
Guna: Navigasi cepat bagi kontributor inti (Core Dev) dan pengembang ekstensi C.
"""

import sys
import os

def render_machine_map():
    print("=" * 60)
    print("🚀 CPYTHON SOURCE ANATOMY: THE MACHINE ROOM MAP")
    print("=" * 60)

    # 1. THE ARCHITECTURAL COMPONENT LIST
    COMPONENTS = {
        "Include/": "C-API Headers (.h) - The Contract",
        "Objects/": "Built-in Types (list, dict, str) - The Atoms",
        "Python/": "The Engine (compiler, ceval.c) - The Brain",
        "Modules/": "C-Extensions (math, hashlib) - The Muscles",
        "Parser/": "The PEG Grammar & Parser - The Gatekeeper",
        "Grammar/": "Formal Language Tokens - The DNA",
        "Lib/": "Python Standard Library (.py) - The Cells",
        "PCbuild/": "Windows Build Project Files - The Windows Port",
    }

    print("\n1. Key Folders & Responsibilities:")
    for path, desc in COMPONENTS.items():
        print(f"   [ ] {path:<15} | {desc}")

    # 2. FILE TYPE SEARCH (CONCEPTS)
    print("\n2. Identifying the Core 'Holy' Files:")
    CORE_FILES = {
        "Include/object.h": "The absolute base Struct: PyObject.",
        "Python/ceval.c": "The main bytecode evaluation loop.",
        "Objects/listobject.c": "The memory implementation of Python Lists.",
        "Parser/pegen.c": "The PEG parser implementation.",
    }

    for file, purpose in CORE_FILES.items():
        print(f"   [!] {file:<25} | {purpose}")

    # 3. INTERACTIVE SEARCH CONCEPT
    print("\n3. Navigating Search Tips:")
    print("   [TIP] Use 'grep -r PyObject_New' in Include/ to find allocation logic.")
    print("   [TIP] Search for 'TARGET(BINARY_ADD)' in ceval.c to see ADD internals.")

    print("\n" + "=" * 60)
    print("✅ Lab Completed. Use these maps to find where Python logic is TRULY written.")

if __name__ == "__main__":
    render_machine_map()
