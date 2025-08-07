# 🔁 Palingram Finder in Python

This project is a Python program that reads a list of English words from a text file and identifies **palingram pairs** — word pairs that form a **palindrome** when combined. It gives users flexible options to view and save results.

> ✅ DSA (Data Structures & Algorithms) concepts like `set` lookup (O(1)), two-pointer palindrome checking, and nested iteration are applied for performance and clarity.

---

## 📌 What is a Palingram?

A **palingram** is a pair of real words (like `gateman` and `nametag`) that form a **palindrome** when joined together:
gateman + nametag → gatemannametag ← same forward & backward


---

## 🚀 Features

- Reads words from any `.txt` file
- Efficiently checks for palingrams using **DSA principles**
- Offers 3 display formats:
  - Just the words
  - Just the full palindromes
  - Both
- Optionally save results to a file

---

## 🛠️ Technologies Used

- Python 3
- Standard Library only
- `set` for fast word lookups
- Two-pointer technique for palindrome validation

---

## 🧠 DSA Concepts Used

| Concept               | Purpose                                        |
|------------------------|-----------------------------------------------|
| `set` data structure   | Fast O(1) word lookup                         |
| Nested loops           | Iterate over unique word pairs               |
| Two-pointer algorithm  | Efficient palindrome checking without reversal |
| Exception handling     | File not found or I/O error handling          |

---

## ✅ How to Use

```bash
# Clone or download the repo

# Prepare a word list file (e.g., words.txt)

# Run the script
python palingram_finder.py


📄 Sample Dictionary (for testing)

You can create a small test dictionary named small_dictionary.txt:
evil
live
devil
lived
gateman
nametag
race
car
kayak
madam
level
noon
💡 Example Output
Combined palingram: evil + live → evillive
Combined palingram: gateman + nametag → gatemannametag
