"""
LAB PRACTICAL: Async Evolution (PEPs 492, 654)
Standard: PPM V4 - Gold Standard

Tujuan: Memahami transisi ke paradigma non-blocking modern.
Guna: Membangun sistem asinkron yang tangguh dan informatif.
"""

import sys
import asyncio

def check_version(required_v):
    """Utility to guard version-specific features."""
    return sys.version_info >= required_v

async def sample_task(name, delay, fail=False):
    """A simple async task that simulates I/O."""
    await asyncio.sleep(delay)
    if fail:
        raise ValueError(f"Error in task {name}")
    return f"Task {name} completed."

async def run_lab():
    print("=" * 60)
    print("🚀 PYTHON ASYNC EVOLUTION LAB")
    print("=" * 60)

    # 1. PEP 492: Native async/await (Python 3.5+)
    print(f"\n1. PEP 492: Native Coroutines (async/await)")
    if check_version((3, 5)):
        result = await sample_task("Core Worker", 0.5)
        print(f"   [RESULT] {result}")
    else:
        print("   [SKIP] async/await requires Python 3.5+")

    # 2. PEP 654: Exception Groups (Python 3.11+)
    print(f"\n2. PEP 654: Exception Groups & except*")
    if check_version((3, 11)):
        # We use eval/exec to protect compatibility with older Python
        aggregator_code = """
import asyncio

async def handle_aggregate_errors():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(sample_task("T1", 0.1, fail=True))
            tg.create_task(sample_task("T2", 0.1, fail=True))
    except* ValueError as eg:
        print(f"   [RESULT] Handled {len(eg.exceptions)} ValueErrors from group")

asyncio.run(handle_aggregate_errors())
"""
        # Execute in a new event loop or using current loop
        # Note: TaskGroup needs its own run
        exec(aggregator_code)
    else:
        print("   [SKIP] Exception Groups & except* requires Python 3.11+")

    print("\n" + "=" * 60)
    print("✅ Lab Completed.")

if __name__ == "__main__":
    # In a real script, we would use asyncio.run(run_lab())
    # But for a simple lab script to show logic:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_lab())
