"""
LAB PRACTICAL: Syntax Evolution (PEPs 498, 572, 634)
Standard: PPM V4 - Gold Standard

Tujuan: Memahami transisi dari Python klasik ke modern.
Guna: Menulis kode yang lebih ekspresif dan efisien.
"""

import sys

def check_version(required_v):
    """Utility to guard version-specific features."""
    return sys.version_info >= required_v

def run_lab():
    print("=" * 60)
    print("🚀 PYTHON SYNTAX EVOLUTION LAB")
    print("=" * 60)

    # 1. PEP 498: f-strings (Python 3.6+)
    name = "Pythonista"
    version = f"{sys.version_info.major}.{sys.version_info.minor}"
    print(f"\n1. PEP 498: Literal Interpolation")
    print(f"   [RESULT] Hello {name}, you are using Python {version}")

    # 2. PEP 572: Assignment Expressions (Python 3.8+)
    print(f"\n2. PEP 572: Walrus Operator (Assignment Expressions)")
    if check_version((3, 8)):
        # Simulate processing a line with assignment in condition
        sample_text = "Python Evolution"
        if (n := len(sample_text)) > 10:
            print(f"   [RESULT] Text '{sample_text}' is long enough ({n} chars).")
    else:
        print("   [SKIP] Walrus operator requires Python 3.8+")

    # 3. PEP 634: Structural Pattern Matching (Python 3.10+)
    print(f"\n3. PEP 634: Match-Case (Structural Pattern Matching)")
    if check_version((3, 10)):
        # We use eval to avoid SyntaxError on older Python versions
        matching_code = """
command = "move North 10"
match command.split():
    case ["move", direction, distance]:
        print(f"   [RESULT] Moving {distance} steps to {direction}")
    case ["quit"]:
        print("   [RESULT] Quitting...")
    case _:
        print("   [RESULT] Unknown command")
"""
        exec(matching_code)
    else:
        print("   [SKIP] Match-Case requires Python 3.10+")

    print("=" * 60)
    print("✅ Lab Completed.")

if __name__ == "__main__":
    run_lab()
