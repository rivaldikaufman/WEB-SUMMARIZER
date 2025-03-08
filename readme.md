# 📜 Telegram Article Summarizer Bot

## 🚀 Teknologi yang Digunakan

<p align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" width="60"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" alt="Telegram" width="60"/>
  <img src="https://dicksonneoh.com/portfolio/deploy_gpt_hf_models_on_telegram/botfather_img.png" alt="Gemini" height="" width="60"/>
  <img src="https://registry.npmmirror.com/@lobehub/icons-static-png/latest/files/dark/gemini-color.png" alt="Gemini" height="" width="60"/>
</p>

## 🚀 Deskripsi
Bot Telegram ini memungkinkan pengguna untuk merangkum artikel secara otomatis hanya dengan mengirimkan link artikel. Bot menggunakan model AI **Gemini** untuk menghasilkan ringkasan dengan berbagai pilihan bahasa dan gaya bahasa.

## 🎯 Fitur Utama
- 🔗 **Ekstrak teks otomatis** dari artikel yang dikirimkan.
- 🤖 **Ringkasan AI** menggunakan model **Gemini**.
- 🌍 **Dukungan multi-bahasa** (Bahasa Indonesia & English).
- ✨ **Gaya bahasa bervariasi**: Formal, Gaul, atau Jaksel.
- ⚡ **Mudah digunakan** hanya dengan mengirimkan link artikel.

## 🛠️ Teknologi yang Digunakan
- **Python** 🐍
- **Telegram Bot API**
- **Google Generative AI (Gemini API)**
- **Newspaper3k** (Untuk ekstraksi teks artikel)
- **Python-Telegram-Bot** (Untuk integrasi dengan Telegram)

## 🏗️ Instalasi & Penggunaan

### 1️⃣ **Clone Repository**
```bash
git clone https://github.com/rivaldikaufman/WEB-SUMMARIZER.git
cd WEB-SUMMARIZER
```

### 2️⃣ **Buat Virtual Environment (Opsional)**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate    # Windows
```

### 3️⃣ **Install Dependensi**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Konfigurasi API Token**
Buka file `main.py` dan ganti:
```python
BOT_TOKEN = "YOUR BOTFATHER TOKEN"
GEMINI_API_KEY = "YOUR GEMINI API"
```
Dengan token bot Telegram dan API Key Gemini milikmu.

### 5️⃣ **Jalankan Bot**
```bash
python main.py
```

## 📌 Cara Menggunakan
1. Kirim **link artikel** ke bot.
2. Pilih **bahasa ringkasan**.
3. Pilih **gaya bahasa**.
4. Bot akan mengirimkan ringkasan artikel!

## 📜 Contoh Penggunaan
**Input:**
```
https://example.com/artikel
```
**Bot Response:**
```
📰 Ringkasan dalam Bahasa Indonesia (Gaya Jaksel):
"Jadi gini, bro, intinya artikel ini tuh ngebahas tentang..."
```

## ⚠️ Catatan
- Pastikan artikel yang dikirim memiliki akses publik.
- Model AI memiliki batasan karakter untuk input teks.

## 📧 Kontak & Kontribusi
Jika ingin berkontribusi atau melaporkan masalah, silakan buat **issue** atau **pull request** di repo ini. 🚀

