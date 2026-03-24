# Python Knowledge Base

> **"From Simple Scripts to AI Data Science."**

## 🏛️ Arsitektur 7-Rak (Universal Standard + Applied)

Repositori ini menggunakan **7-Rack Architecture** dengan prinsip **Digital Mirroring**. Enam Rak pertama membedah bahasa Python itu sendiri (dari jiwa hingga mesin), satu Rak terakhir mengaplikasikannya ke industri nyata.

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
    RAK07["RAK-07-specializations<br/>(The Workshop)"]

    Root --> RAK01 & RAK02 & RAK03 & RAK04 & RAK05 & RAK06
    Root --> RAK07

    style Root fill:#3776AB,stroke:#333,stroke-width:4px,color:#FFF
    style RAK01 fill:#4CAF50,stroke:#333,color:#FFF
    style RAK02 fill:#fff,stroke:#333
    style RAK03 fill:#fff,stroke:#333
    style RAK04 fill:#ddd,stroke:#333
    style RAK05 fill:#fff,stroke:#333
    style RAK06 fill:#ddd,stroke:#333
    style RAK07 fill:#FF9800,stroke:#333,color:#FFF
```

---

## 🗄️ Struktur Perpustakaan

### Core Language (RAK-01 — RAK-06)

| # | Rak | Fokus | Status |
|---|---|---|---|
| 1 | [RAK-01-anatomy](./RAK-01-anatomy/) | Jiwa, Sejarah & Trade-offs | ✅ 100% |
| 2 | [RAK-02-foundation](./RAK-02-foundation/) | Sintaksis & Dasar Bahasa | ⚪ Planned |
| 3 | [RAK-03-evolution](./RAK-03-evolution/) | PEPs & Evolusi Versi | ⚪ Planned |
| 4 | [RAK-04-core-mechanics](./RAK-04-core-mechanics/) | Data Model & Internals | ⚪ Planned |
| 5 | [RAK-05-standard-library](./RAK-05-standard-library/) | Built-ins & Ecosystem | ⚪ Planned |
| 6 | [RAK-06-interpreters](./RAK-06-interpreters/) | CPython, Bytecode, GIL | ⚪ Planned |

### Applied Python (RAK-07)

| # | Rak | Fokus | Status |
|---|---|---|---|
| 7 | [RAK-07-specializations](./RAK-07-specializations/) | AI, ML, Web, Automation | ⚪ Planned |

---

## 📏 Standar Kualitas (Gold Standard)
Setiap materi mengikuti prinsip **Digital Mirroring** dan standar **PPM V4** yang mewajibkan:
1. **Source-Synced**: Akurasi 1:1 terhadap dokumentasi resmi/spesifikasi (docs.python.org / PEPs).
2. **Experimental Lab**: Kode pembuktian fungsional di folder `examples/` (.py).
3. **Mental Model Visual**: Diagram Mermaid inline.
4. **Narrative Excellence**: Penjelasan mendalam dengan analogi dunia nyata (The Serpent's Core).

*Dokumentasi Lengkap Standar: [docs/standards/architecture.md](./docs/standards/architecture.md)*

---
*Status Pengembangan: [status.md](./status.md)*
