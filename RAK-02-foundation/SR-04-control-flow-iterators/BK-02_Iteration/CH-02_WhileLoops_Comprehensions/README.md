# CH-02: While Loops & Comprehensions [x] Complete

> **"A while loop repeats until truth fades, but a comprehension builds with intent."**

Bab ini membedah dua cara berbeda untuk mengelola perulangan: **`while`** loop yang berbasis kondisi dan **Comprehensions** — cara Pythonic yang elegan dan deklaratif untuk menciptakan struktur data.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [Python Docs - while Statements](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)
- **Primary Source**: [List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- **Strategic Blueprint**: [RAK-02 Foundation](file:///i:/Workspace/Workspace-Syahputrawork/learning-matrix-blueprint/01-Language-Hubs/Python-Knowledge-Base.md)

---

## 🧠 The Essence (Narrative)
**`while`** loop terus berjalan selama kondisinya tetap `True`. Sama seperti `for`, ia memiliki blok `else` yang berjalan saat kondisi menjadi `False`. Di sisi lain, **Comprehensions** adalah fitur unggulan Python untuk membuat `list`, `dict`, atau `set` baru dari koleksi yang ada dalam satu baris (one-liner). Ia menggabungkan loop dan filter (`if`) secara padat, namun tetap terbaca (jika digunakan dengan benar).

---

## 🎨 Visual Logic (The Comprehension Flow)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph LR
    Input[Source Collection] -- iter --> Loop[For Item]
    Loop -- optional --> Filter{Condition?}
    Filter -- Yes --> Build[Apply Expression]
    Build --> Output[New Collection]
    style Build fill:#3776AB,stroke:#333,color:#fff
```

---

## 🛠️ Syntax Examples

### 1. While Loop
```python
x = 0
while x < 5:
    print(x)
    x += 1
```

### 2. Comprehensions (The Pythonic Way)
```python
# List Comprehension
squares = [i**2 for i in range(10) if i % 2 == 0]

# Dict Comprehension
square_map = {i: i**2 for i in range(5)}
```

---

## ⚠️ Pitfalls
- **Infinite While Loop**: Selalu pastikan variabel kondisi dalam `while` diperbarui agar loop tidak berjalan selamanya (menghabiskan CPU).
- **Over-Complicated Comprehensions**: Jangan paksa menulis logika yang sangat rumit dalam satu baris. Jika pembaca harus membacanya lebih dari dua kali, gunakan `for` loop biasa demi keterbacaan (*Readability*).

---
*Back to [BK-02 Iteration](../README.md)*
