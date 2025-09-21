# app.py
st.set_page_config(page_title="ProdBot — Personal Productivity Assistant", layout="wide")


with st.sidebar:
st.title("ProdBot")
st.markdown("Personal Productivity Assistant")
style = st.radio("Gaya bahasa:", ["Santai", "Formal"]) # creative parameter
use_rag = st.checkbox("Aktifkan RAG (vector DB)", value=False)
use_agent = st.checkbox("Aktifkan Agent (mock)", value=True)
temp = st.slider("Temperature (kreativitas)", 0.0, 1.0, 0.3)
max_tokens = st.slider("Max tokens", 50, 1024, 350)


# session state for chat
if "messages" not in st.session_state:
st.session_state.messages = []


st.title("ProdBot — Personal Productivity Assistant")


# display chat history
for i, msg in enumerate(st.session_state.messages):
role = msg["role"]
text = msg["content"]
if role == "user":
st.markdown(f"**You:** {text}")
else:
st.markdown(f"**ProdBot:** {text}")


# input
user_input = st.text_input("Ketik pertanyaan atau tugasmu...", key="input")


if st.button("Kirim") and user_input:
# append user
st.session_state.messages.append({"role": "user", "content": user_input})


# retrieval step (if enabled)
docs = None
if use_rag:
docs = retrieve_documents(user_input)


# generate response via LLM or Agent
response = generate_response(
user_input,
docs=docs,
style=style,
temperature=float(temp),
max_tokens=int(max_tokens),
use_agent=use_agent,
)


st.session_state.messages.append({"role": "assistant", "content": response})
# clear input
st.session_state.input = ""
