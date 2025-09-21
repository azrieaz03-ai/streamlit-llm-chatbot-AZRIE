import streamlit as st
from utils import generate_response, retrieve_documents  # pastikan ada file utils.py

# Konfigurasi halaman
st.set_page_config(page_title="ProdBot — Personal Productivity Assistant", layout="wide")

# Sidebar
with st.sidebar:
    st.title("ProdBot")
    st.markdown("Personal Productivity Assistant")
    
    # Parameter kreatif
    style = st.radio("Gaya bahasa:", ["Santai", "Formal"])  # creative parameter
    use_rag = st.checkbox("Aktifkan RAG (vector DB)", value=False)
    use_agent = st.checkbox("Aktifkan Agent (mock)", value=True)
    temp = st.slider("Temperature (kreativitas)", 0.0, 1.0, 0.3)
    max_tokens = st.slider("Max tokens", 50, 1024, 350)

# Session state untuk menyimpan percakapan
if "messages" not in st.session_state:
    st.session_state.messages = []

# Judul utama
st.title("ProdBot — Personal Productivity Assistant")

# Tampilkan riwayat chat
for msg in st.session_state.messages:
    role = msg["role"]
    text = msg["content"]
    if role == "user":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**ProdBot:** {text}")

# Input pengguna
user_input = st.text_input("Ketik pertanyaan atau tugasmu...", key="input")

# Tombol kirim
if st.button("Kirim") and user_input:
    # Tambahkan input user ke riwayat
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Retrieval step (jika RAG aktif)
    docs = None
    if use_rag:
        docs = retrieve_documents(user_input)

    # Generate response (LLM / Agent / Mock)
    response = generate_response(
        user_input,
        docs=docs,
        style=style,
        temperature=float(temp),
        max_tokens=int(max_tokens),
        use_agent=use_agent,
    )

    # Simpan jawaban ke session_state
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Kosongkan input
    st.session_state.input = ""
 
