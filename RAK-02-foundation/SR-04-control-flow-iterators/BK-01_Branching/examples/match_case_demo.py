"""
LAB PRACTICAL: Structural Pattern Matching (PEP 634)
Standard: PPM V4 - Gold Standard

Tujuan: Mendemonstrasikan kekuatan `match-case` (Python 3.10+) untuk destructuring data.
Guna: Menggantikan rangkaian if-elif yang kompleks dengan pola yang deklaratif.
"""

def handle_command(command):
    print(f"\nProcessing command: {command}")
    
    match command:
        # 1. Matching Exact Values
        case "QUIT":
            print("🛑 System: Quitting...")
            
        # 2. Destructuring List (2 elements)
        case ["MOVE", direction]:
            print(f"🏃 Moving toward {direction}")
            
        # 3. Destructuring List with Guard Clause
        case ["MOVE", direction, distance] if int(distance) > 100:
             print(f"🚀 Long Distance Move detected: {distance} to {direction}")
        case ["MOVE", direction, distance]:
             print(f"🚶 Normal Move: {distance} units to {direction}")
            
        # 4. Destructuring Dictionary
        case {"type": "MSG", "user": name, "content": msg}:
            print(f"💬 Message from {name}: \"{msg}\"")
            
        # 5. Wildcard (Catch-all)
        case _:
            print("❓ Unknown command format.")

def run_lab():
    print("=" * 60)
    print("🪄 STRUCTURAL PATTERN MATCHING LAB")
    print("=" * 60)
    
    # Test cases
    handle_command("QUIT")
    handle_command(["MOVE", "NORTH"])
    handle_command(["MOVE", "SOUTH", "50"])
    handle_command(["MOVE", "EAST", "500"]) # Guard clause test
    handle_command({"type": "MSG", "user": "Antigravity", "content": "Hello Pythonic World!"})
    handle_command("SAY HELLO") # Unknown command

    print("\n" + "=" * 60)
    print("✅ Lab Completed.")

if __name__ == "__main__":
    import sys
    # Cek versi Python (Minimal 3.10)
    if sys.version_info < (3, 10):
        print("❌ Error: Structural Pattern Matching membutuhkan Python 3.10 atau lebih baru.")
        print(f"Info : Versi Anda saat ini adalah {sys.version.split()[0]}")
    else:
        run_lab()
