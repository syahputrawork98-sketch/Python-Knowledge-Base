"""
LAB PRACTICAL: Attribute & Method Scoping Audit
Standard: PPM V4 - Gold Standard

Tujuan: Memahami perbedaan penanganan data pada level Class vs Instance.
Guna: Menghindari state leakage antar objek dan memilih jenis metode yang tepat.
"""

class SmartDevice:
    # 1. CLASS ATTRIBUTES (Shared by ALL instances)
    brand = "Pythonic-Core"
    _device_count = 0

    def __init__(self, name):
        # 2. INSTANCE ATTRIBUTES (Unique per instance)
        self.name = name
        SmartDevice._increment_count() # Update class state

    # 3. INSTANCE METHOD: Accesses instance data via 'self'
    def show_info(self):
        print(f"📡 Device: {self.name} | Brand: {self.brand}")

    # 4. CLASS METHOD: Accesses class data via 'cls'
    @classmethod
    def get_total_devices(cls):
        return f"Total devices in network: {cls._device_count}"

    @classmethod
    def _increment_count(cls):
        cls._device_count += 1

    # 5. STATIC METHOD: No access to instance or class state
    @staticmethod
    def validate_id(device_id):
        # Pure utility logic
        return len(device_id) > 5

def run_lab():
    print("=" * 60)
    print("🛠️ OOP SCOPING AUDIT LAB")
    print("=" * 60)

    # Instantiation
    d1 = SmartDevice("Node-01")
    d2 = SmartDevice("Node-02")

    # Audit 1: Instance Data
    print("Audit 1: Checking Instance Uniqueness")
    print(f"   Device 1 Name: {d1.name}")
    print(f"   Device 2 Name: {d2.name}")

    print("\nAudit 2: Checking Class Data Sharing")
    print(f"   d1 sees brand: {d1.brand}")
    print(f"   d2 sees brand: {d2.brand}")
    
    # Audit 3: Modifying Class Attribute via Class
    SmartDevice.brand = "Generic-Link"
    print("   [UPDATE] Class Brand updated to Generic-Link")
    print(f"   d1 sees updated brand: {d1.brand}")
    
    print("\nAudit 4: Checking Factory/Class Methods")
    print(f"   {SmartDevice.get_total_devices()}")

    print("\nAudit 5: Static Utility")
    print(f"   ID 'XYZ' is valid?   : {SmartDevice.validate_id('XYZ')}")
    print(f"   ID 'XYZ-999' is valid? : {SmartDevice.validate_id('XYZ-999')}")

    print("=" * 60)
    print("✅ Lab Completed.")

if __name__ == "__main__":
    run_lab()
