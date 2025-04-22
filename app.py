import streamlit as st
import time
from chains import get_chain
from memory import create_character_memory

# Page configuration
st.set_page_config(page_title="Espresso Yourself", page_icon="☕", layout="centered")

st.markdown("""
<style>
.stApp {
    background-image : url("app/static/bg.png"); 
    background-size: cover;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>Espresso Yourself Café</h2>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'><h6 style='font-size: 0.8rem; color: #803d3b;'>Rant to your companion of choice — a warm barista, anxious waitress, or a sassy customer.<br>Powered by Langchain.</h6></div>", unsafe_allow_html=True)
st.write("")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "character" not in st.session_state:
    st.session_state.character = "Barista"
if "memory" not in st.session_state:
    st.session_state.memory = create_character_memory(st.session_state.character)
if "show_debug" not in st.session_state:
    st.session_state.show_debug = False

# Character avatars
character_avatars = {
    "Barista": "🧑🏻‍🍳",
    "Waitress": "🧍🏻‍♀️",
    "Customer": "🧑🏻‍🦰"
}
user_avatar = "😤"

# Character selection handler
def select_character(char):
    if st.session_state.character != char:
        st.session_state.character = char
        st.session_state.messages = []
        st.session_state.memory = create_character_memory(char)
        st.rerun()

# Character selection buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🧑🏻‍🍳 Barista", use_container_width=True,
                key="barista_btn",
                type="primary" if st.session_state.character == "Barista" else "secondary"):
        select_character("Barista")

with col2:
    if st.button("🧍🏻‍♀️ Waitress", use_container_width=True,
                key="waitress_btn",
                type="primary" if st.session_state.character == "Waitress" else "secondary"):
        select_character("Waitress")

with col3:
    if st.button("🧑🏻‍🦰 Customer", use_container_width=True,
                key="customer_btn",
                type="primary" if st.session_state.character == "Customer" else "secondary"):
        select_character("Customer")

st.markdown(f"You're currently ranting to the **{st.session_state.character}**")

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message(msg["role"], avatar=user_avatar):
            st.write(msg["text"])
    else:
        avatar = character_avatars.get(msg.get("character", "Barista"))
        with st.chat_message(msg["role"], avatar=avatar):
            st.write(msg["text"])

# Handle user input
user_input = st.chat_input("Type your rant here...")

if user_input:
    # Add message to UI state
    st.session_state.messages.append({"role": "user", "text": user_input})
    
    # Display user message
    with st.chat_message("user", avatar=user_avatar):
        st.write(user_input)
    
    # Process input and generate response
    chain = get_chain(st.session_state.character, st.session_state.memory)
    
    try:
        # Generate response
        response = chain.invoke({"input": user_input})
        response_text = response["text"] if isinstance(response, dict) and "text" in response else str(response)
        
    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.error("⚠️ Uh oh! Looks like you've hit the daily free quota. Please come back tomorrow!")
        st.stop()

    # Display assistant response with typewriter effect
    with st.chat_message("assistant", avatar=character_avatars[st.session_state.character]):
        response_placeholder = st.empty()
        full_response = ""
        for chunk in response_text.split():
            full_response += chunk + " "
            response_placeholder.write(full_response)
            time.sleep(0.05)

    # Store in session state for display
    st.session_state.messages.append({
        "role": "assistant",
        "text": response_text,
        "character": st.session_state.character
    })

# Debug toggle (at the bottom of the page)
if st.sidebar.checkbox("Show debug info", value=st.session_state.show_debug):
    st.session_state.show_debug = True
    st.sidebar.subheader("Memory Contents")
    try:
        memory_vars = st.session_state.memory.load_memory_variables({})
        st.sidebar.json(memory_vars)
        
        # Add a button to clear memory
        if st.sidebar.button("Clear Memory"):
            st.session_state.memory.clear()
            st.sidebar.success("Memory cleared!")
            time.sleep(1)
            st.rerun()
    except Exception as e:
        st.sidebar.error(f"Error loading memory: {str(e)}")
else:
    st.session_state.show_debug = False
