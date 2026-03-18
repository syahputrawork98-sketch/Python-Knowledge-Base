import os
import sys

def check_standards(base_path):
    standards_path = os.path.join(base_path, 'docs', 'standards')
    required_files = [
        'architecture.md', 'conventions.md', 'workflow.md', 
        'status-protocol.md', 'contribution.md', 'core-contribution.md'
    ]
    missing = []
    if not os.path.exists(standards_path):
        return ["Docs standards directory missing"]
    
    for f in required_files:
        if not os.path.exists(os.path.join(standards_path, f)):
            missing.append(f"Missing standard file: {f}")
    return missing

def audit_structure(base_path):
    errors = []
    for root, dirs, files in os.walk(base_path):
        # Skip hidden dirs
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        folder_name = os.path.basename(root)
        
        # Check RAK/SR/BK/CH naming and README requirement
        if folder_name.startswith(('RAK-', 'SR-', 'BK-', 'CH-')):
            if 'README.md' not in files:
                errors.append(f"Missing README.md in {root}")
            
            # Specific check for Chapter (Level 5)
            
            if folder_name.startswith('CH-'):
                if 'assets' not in dirs:
                    errors.append(f"Missing 'assets/' folder in chapter {root}")
                if 'examples' not in dirs:
                    errors.append(f"Missing 'examples/' folder in chapter {root}")
                    
    return errors

def main():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"--- Sentinel Audit (Python Edition) ---")
    print(f"Auditing: {base_path}\n")
    
    standards_errors = check_standards(base_path)
    structure_errors = audit_structure(base_path)
    
    all_errors = standards_errors + structure_errors
    
    if not all_errors:
        print("[PASS] Everything is perfectly standardized! (Gold Standard)")
    else:
        print(f"[FAIL] Found {len(all_errors)} inconsistencies:")
        for err in all_errors:
            print(f" - {err}")
        sys.exit(1)

if __name__ == "__main__":
    main()
