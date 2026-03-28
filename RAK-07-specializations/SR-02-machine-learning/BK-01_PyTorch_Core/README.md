# BK-01: PyTorch Core (Tensors & Gradients) [x] Complete

> **"Tensors are the language of intelligence, and PyTorch is the voice that speaks it."**

Buku ini membedah **PyTorch**, framework deep learning paling populer di dunia riset dan industri AI. Kita akan mempelajari fondasi matematika dari kecerdasan buatan—**Tensors**—dan bagaimana mekanisme **Autograd** (Automatic Differentiation) memungkinkan komputer "belajar" dari kesalahan melalui proses backpropagation.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [PyTorch Official Documentation](https://pytorch.org/docs/stable/index.html)
- **Concept Guide**: [Deep Learning with PyTorch: A 60 Minute Blitz](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)

---

## 🧠 The Essence (Narrative)
Secara teknis, PyTorch adalah library manipulasi array (seperti NumPy) namun dengan dua kekuatan super:
1.  **Akselerasi GPU**: Operasi matematika dapat dijalankan ribuan kali lebih cepat di kartu grafis (NVIDIA CUDA).
2.  **Computational Graphs**: PyTorch mencatat setiap operasi yang Anda lakukan dalam grafik dinamis. Saat Anda memanggil `.backward()`, PyTorch menghitung turunan (gradient) untuk setiap variabel secara otomatis. Inilah jantung dari pelatihan Neural Networks.

---

## 🎨 Visual Logic (Backpropagation Flow)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#EE4C2C', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph LR
    Input[Input Data] --> Model[Neural Network]
    Model --> Prediction[Output/Prediction]
    Prediction --> Loss[Loss Function: Error Calculation]
    Loss -- BACKWARD --> Gradients[Compute Gradients]
    Gradients -- OPTIMIZE --> Weights[Update Network Weights]
    Weights --> Input
    
    style Model fill:#EE4C2C,stroke:#333,color:#fff
    style Gradients fill:#FFD43B,stroke:#333,color:#000
```

---

## 🛠️ Implementation: Tensor Mechanics
```python
import torch

# 1. Tensor creation (with gradient tracking)
x = torch.tensor([2.0, 3.0], requires_grad=True)

# 2. Forward pass (Operation)
y = x**2 + 5

# 3. Backward pass (Automatic Differentiation)
z = y.sum()
z.backward()

# 4. Resulting Gradients (dy/dx)
print(x.grad) # Result: [4.0, 6.0]
```

---

## ⚠️ Pitfalls
- **Device Mismatch Error**: Python akan melemparkan error jika Anda mencoba melakukan operasi antara dua tensor yang berada di perangkat berbeda (misal: satu di CPU dan satu di CUDA GPU). Selalu pastikan `.to(device)` konsisten.
- **Gradient Accumulation**: Secara default, PyTorch **menambahkan** gradient ke nilai sebelumnya setiap kali `.backward()` dipanggil. Jangan lupa menjalankan `optimizer.zero_grad()` sebelum setiap putaran pelatihan (epoch).
- **The .detach() Necessity**: Saat Anda ingin menggunakan hasil tensor untuk logging atau plotting tanpa ingin grafik komputasinya dicatat (menghemat memori), gunakan `.detach()` atau blok `with torch.no_grad():`.

---
*Back to [SR-02 AI & ML Engineering](../README.md)*
