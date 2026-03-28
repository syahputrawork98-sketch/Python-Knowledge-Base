"""
LAB PRACTICAL: Modern File System (pathlib & io)
Standard: PPM V4 - Gold Standard

Tujuan: Memahami otomasi file sistem dengan paradigma Object-Oriented.
Guna: Skrip administrasi sistem (SysAdmin) dan pengelolaan dataset lokal.
"""

from pathlib import Path
import io
import shutil

def run_lab():
    print("=" * 60)
    print("🚀 PYTHON PATHLIB & I/O AUTOMATION LAB")
    print("=" * 60)

    # 1. PATHLIB: The Object Power
    print("\n1. Pathlib: Automated Directory Structure")
    root = Path.cwd() / "lab_workspace"
    # Create multi-level folder instantly
    root.mkdir(parents=True, exist_ok=True)
    
    # Define file path
    log_file = root / "system" / "access.log"
    log_file.parent.mkdir(exist_ok=True) # Create 'system' folder
    
    # 2. Writing & Reading with one-liners
    print(f"   [ACTION] Writing to: {log_file.relative_to(Path.cwd())}")
    log_file.write_text("LOG_START: 2026-03-29\nEVENT: System Initialized", encoding="utf-8")
    
    content = log_file.read_text()
    print(f"   [DATA] File Content:\n{content}")

    # 3. Recursive Search (The Power of rglob)
    print("\n2. Search: Recursive file discovery")
    # Finding all .md and .py files in current workspace (limited to 5)
    files = list(Path.cwd().rglob("*.[mp][dy]"))
    print(f"   [RESULT] Found {len(files)} source files. Top 3:")
    for f in files[:3]:
        print(f"      - {f.name} ({f.suffix})")

    # 4. IO: String Streams (File in RAM)
    print("\n3. RAM-Files: Building virtual logs")
    virtual_log = io.StringIO()
    virtual_log.write("Virtual Event: Cache Clear\n")
    virtual_log.write("Virtual Event: Buffer Flush")
    
    virtual_log.seek(0) # Reset kursor
    print(f"   [DATA] Virtual Stream Content:\n{virtual_log.read()}")

    # 5. SHUTIL: Clean up
    print("\n4. Maintenance: Safe Cleanup")
    if root.exists():
        # shutil.rmtree(root) # Uncomment to actually delete
        print(f"   [INFO] Workspace ready for deletion at: {root}")

    print("\n" + "=" * 60)
    print("✅ Lab Completed. Use Pathlib / for joins and read_text() for simple I/O.")

if __name__ == "__main__":
    run_lab()
