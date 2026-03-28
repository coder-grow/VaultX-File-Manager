# 🛡️ VaultX - Secure File Manager (v3.0)
**Developed by: Alkama Anish**

VaultX ek advanced Python-based Command Line Interface (CLI) tool hai jo normal file management ko high-level encryption ke saath jodta hai. Ye tool developers aur security enthusiasts ke liye banaya gaya hai jo apni files ko securely handle karna chahte hain.

---

## 🔥 Key Features

* **🔐 Password-less Encryption:** AES-256 bit encryption (via Fernet) ka upyog karke files ko lock aur unlock karein.
* **📁 Full Navigation:** Bina terminal chhode folder badlein (`cd`) aur files ki list (`ls`) dekhein.
* **🛠️ File Management:** Naye folders banayein (`mkdir`), files rename karein, ya purani files delete karein.
* **💻 Interactive Shell:** Ek professional OS-style prompt jahan saari commands smoothly chalti hain.

---

## 🛠️ Tech Stack & Tools

* **Language:** Python 3.x
* **Library:** `cryptography` (For Secure Encryption)
* **Interface:** `cmd` module (For Professional CLI experience)
* **Version Control:** Git & GitHub

---

## 🚀 How to Run?

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/coder-grow/VaultX-File-Manager.git](https://github.com/coder-grow/VaultX-File-Manager.git)
    cd VaultX-File-Manager
    ```

2.  **Install Dependencies:**
    ```bash
    pip install cryptography
    ```

3.  **Start VaultX:**
    ```bash
    python vaultx.py
    ```

---

## 💡 Commands Table

| Command | Usage | Description |
| :--- | :--- | :--- |
| `ls` | `ls` | Files aur folders ki list dekhein |
| `lock` | `lock <filename>` | File ko encrypt karein |
| `unlock` | `unlock <filename>` | File ko decrypt karein |
| `mkdir` | `mkdir <name>` | Naya folder banayein |
| `rename` | `rename <old> <new>` | File ka naam badlein |
| `delete` | `delete <filename>` | File permanent delete karein |
| `exit` | `exit` | VaultX se bahar nikalne ke liye |

---

> **⚠️ Security Note:** Aapki `secret.key` file hi aapki "Master Key" hai. Agar ye kho gayi, toh encrypted files kabhi unlock nahi hongi. Ise hamesha backup karke rakhein!

---
Developed with ❤️ by **Alkama Anish**