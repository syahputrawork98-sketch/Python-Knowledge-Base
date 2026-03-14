# Sub-Rak 04: Concurrency (Melakukan Banyak Hal Sekaligus)

Saat aplikasi bertambah besar, Anda akan menemui masalah performa yang disebabkan oleh latensi (*I/O Bound*) atau komputasi (*CPU Bound*). Fase ini membahas strategi utama Python untuk menyelesaikan masalah tersebut.

## Daftar Buku

1. [**01_concurrency**](01_concurrency/)
   Memahami struktur dasar *Threading* (untuk *I/O bound*) dan *Multiprocessing* (untuk *CPU bound*), beserta kerumitan yang menyertainya seperti `Locks` dan `Queues`.

2. [**02_async_programming**](02_async_programming/)
   Paradigma yang lebih modern dalam Python; `asyncio`, *event loops*, *coroutines*, tugas *non-blocking*. Cocok untuk API dan layanan web berkinerja tinggi.
