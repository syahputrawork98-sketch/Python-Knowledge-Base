# Python Knowledge Base

> **"From Simple Scripts to AI Data Science."**

## 🏛️ Arsitektur 6-Rak (Universal Standard)
Repositori ini menggunakan **6-Rack Universal Architecture** dengan prinsip **Digital Mirroring** untuk memisahkan antara fondasi penggunaan dengan dekonstruksi arsitektur mesin.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#FFF'}}}%%
graph TD
    Root["Python Knowledge Base"]
    
    RAK01["RAK-01-anatomy<br/>(The Landscape)"]
    RAK02["RAK-02-foundation<br/>(The Standard Book)"]
    RAK03["RAK-03-evolution<br/>(History & Future)"]
    RAK04["RAK-04-core-mechanics<br/>(The Internal Logic)"]
    RAK05["RAK-05-standard-library<br/>(The Environment)"]
    RAK06["RAK-06-interpreters<br/>(The Machine Room)"]
    
    Root --> RAK01 & RAK02 & RAK03 & RAK04 & RAK05 & RAK06
    
    style Root fill:#3776AB,stroke:#333,stroke-width:4px,color:#FFF
    style RAK01 fill:#fff,stroke:#333
    style RAK02 fill:#fff,stroke:#333
    style RAK03 fill:#fff,stroke:#333
    style RAK04 fill:#ddd,stroke:#333
    style RAK05 fill:#fff,stroke:#333
    style RAK06 fill:#ddd,stroke:#333
```

---

## 🗄️ Struktur Perpustakaan

### 1. [RAK-01-anatomy](./RAK-01-anatomy/)
Menelusuri esensi naratif Python, Zen of Python, dan target utamanya.

### 2. [RAK-02-foundation](./RAK-02-foundation/)
Struktur dan sintaks fundamental layaknya membaca Python documentation secara presisi.

### 3. [RAK-03-evolution](./RAK-03-evolution/)
Jejak evolusi PEP (Python Enhancement Proposals) dan pergeseran versi.

### 4. [RAK-04-core-mechanics](./RAK-04-core-mechanics/)
Mekanisme Internal, membedah Python Data Model (Dunder Methods), dan Duck Typing.

### 5. [RAK-05-standard-library](./RAK-05-standard-library/)
Eksplorasi komprehensif Modul Built-in Python dan ekosistem `pip`.

### 6. [RAK-06-interpreters](./RAK-06-interpreters/)
Deep Dive ke dalam Jantung Eksekutor: CPython, Bytecode, GIL, dan PyPy.

---

## 📏 Standar Kualitas (Gold Standard)
Setiap materi mengikuti prinsip **Digital Mirroring** dan standar **PPM V4** yang mewajibkan:
1. **Source-Synced**: Akurasi 1:1 terhadap dokumentasi resmi/spesifikasi.
2. **Experimental Lab**: Kode pembuktian fungsional di folder `examples/`.
3. **Mental Model Visual**: Diagram Mermaid di folder `assets/`.
4. **Narrative Excellence**: Penjelasan mendalam dengan analogi dunia nyata.

*Dokumentasi Lengkap Standar: [docs/standards/architecture.md](./docs/standards/architecture.md)*

---
*Status Pengembangan: [status.md](./status.md)*
