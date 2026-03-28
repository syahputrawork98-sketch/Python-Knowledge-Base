"""
LAB PRACTICAL: Standard Concurrency (asyncio & threading)
Standard: PPM V4 - Gold Standard

Tujuan: Memahami perbedaan paradigma Co-operative vs Pre-emptive multitasking.
Guna: Memilih mesin eksekusi yang tepat untuk I/O-bound atau Network-heavy apps.
"""

import asyncio
import threading
import time
from queue import Queue

# 1. THE ASYNCIO ENGINE (Co-operative)
async def async_worker(id):
    print(f"   [ASYNC] Worker {id} starting wait...")
    await asyncio.sleep(0.5) # Non-blocking wait
    return f"Async Result {id}"

async def run_async_lab():
    print("\n1. Running Asyncio Event Loop...")
    start = time.time()
    results = await asyncio.gather(*(async_worker(i) for i in range(3)))
    end = time.time()
    print(f"   [DONE] Async Results: {results} (Time: {end - start:.4f}s)")

# 2. THE THREADING ENGINE (Pre-emptive)
lock = threading.Lock()
counter = 0

def thread_worker(id):
    global counter
    print(f"   [THREAD] Worker {id} simulating I/O...")
    time.sleep(0.5) # Blocking wait (Safe in threads)
    with lock: # Protecting shared memory
        counter += 1
    print(f"   [DONE] Worker {id} finished.")

def run_thread_lab():
    print("\n2. Running Threads with Shared Lock...")
    start = time.time()
    threads = []
    for i in range(3):
        t = threading.Thread(target=thread_worker, args=(i,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    end = time.time()
    print(f"   [DONE] Shared Counter: {counter} (Time: {end - start:.4f}s)")

# 3. THE QUEUE HUB (Safe Communication)
def run_queue_lab():
    print("\n3. Thread Communication via Queue...")
    q = Queue()
    
    def producer():
        q.put("SECRET_DATA")
    
    def consumer():
        data = q.get()
        print(f"   [QUEUE] Consumer received: {data}")

    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start(); t2.start()
    t1.join(); t2.join()

def main():
    print("=" * 60)
    print("🚀 PYTHON CONCURRENCY & ASYNC LAB")
    print("=" * 60)

    # Run Async Lab
    asyncio.run(run_async_lab())
    
    # Run Thread Lab
    run_thread_lab()
    
    # Run Queue Lab
    run_queue_lab()

    print("\n" + "=" * 60)
    print("✅ Lab Completed. Use Asyncio for thousands of connections, Threads for legacy/blocking IO.")

if __name__ == "__main__":
    main()
