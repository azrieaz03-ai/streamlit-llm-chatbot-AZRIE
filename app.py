import streamlit as st
from utils import generate_response, retrieve_documents  # pastikan utils.py ada

# =========================
# Konfigurasi halaman
# =========================
st.set_page_config(
    page_title="ProdBot — Personal Productivity Assistant",
    layout="wide",
    page_icon="🤖",
)

# =========================
# Sidebar
# =========================
with st.sidebar:
    st.title("🤖 ProdBot")
    st.markdown("**Personal Productivity Assistant**")
    st.divider()
    
    # Parameter gaya
    style = st.radio("Gaya bahasa:", ["Santai", "Formal"], index=0)
    use_rag = st.checkbox("Aktifkan RAG (vector DB)", value=False)
    use_agent = st.checkbox("Aktifkan Agent (mock)", value=True)

    # Parameter model
    temp = st.slider("Temperature (kreativitas)", 0.0, 1.0, 0.3, step=0.05)
    max_tokens = st.slider("Max tokens", 50, 1024, 350, step=50)

# =========================
# Session state
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================
# UI utama
# =========================
st.title("ProdBot — Personal Productivity Assistant 💡")

# Tampilkan riwayat percakapan
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input chat
user_input = st.chat_input("Ketik pertanyaan atau tugasmu...")

if user_input:
    # Simpan pesan user
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Retrieval (kalau aktif)
    docs = retrieve_documents(user_input) if use_rag else None

    # Generate response
    try:
        response = generate_response(
            user_input,
            history=st.session_state.messages,   # ✅ tambahin riwayat chat
            docs=docs,
            style=style,
            temperature=float(temp),
            max_tokens=int(max_tokens),
            use_agent=use_agent,
        )
    except Exception as e:
        response = f"⚠️ Terjadi error: {e}"

    # Simpan & tampilkan jawaban
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
