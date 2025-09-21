# 🤖 Chatbot Gemini + Streamlit

Chatbot sederhana berbasis **Google Gemini API** dengan antarmuka **Streamlit**.  
Mendukung **percakapan multi-turn** (ingat riwayat chat) dan integrasi dokumen (RAG mock).

---

## 🚀 Fitur
- 🔑 Integrasi dengan *Google Gemini API* (`gemini-1.5-flash`)
- 💬 Mendukung percakapan multi-turn (riwayat percakapan disimpan di `session_state`)
- 📄 Retrieval Augmented Generation (RAG) **mock** – contoh integrasi dengan database dokumen
- 🎭 Pilihan gaya bahasa: *Santai* atau *Formal*
- 🔧 Konfigurasi parameter (`temperature`, `max_tokens`)
- 🌐 Dibangun dengan **Python + Streamlit**

---

## 📂 Struktur Project
├── app.py # Main Streamlit app
├── utils.py # Fungsi helper (generate_response, retrieve_documents)
├── example.env # Contoh environment variables (tidak berisi API asli)
├── .gitignore # Supaya file .env tidak ikut ter-push
└── README.md # Dokumentasi project

# Install dependencies
pip install -r requirements.txt

#Setup API Key
Copy file example.env ke api.env

#Isi dengan API key milikmu
GEMINI_API_KEY=YOUR_API_KEY_HERE

#Jalankan aplikasi
streamlit run app.py
