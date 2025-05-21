import streamlit as st
import secrets  # Added missing import
import string

st.set_page_config(page_title="Password Generator", layout="centered")

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []

# Title
st.title("🔐 My Password & Username Generator")

# Inputs
nickname = st.text_input("Enter your nickname:")
real_name = st.text_input("Enter your real name:")

# Generate credentials
if st.button("Generate Username & Password"):
    if nickname and real_name:
        username = f"{nickname}_{real_name}"
        characters = string.ascii_letters + string.digits + string.punctuation
        
        while True:
            password = ''.join(secrets.choice(characters) for _ in range(10))  # 10-character password
            if (any(c.islower() for c in password) and 
                any(c.isupper() for c in password) and 
                any(c in string.punctuation for c in password)):
                break

        # Save to history
        st.session_state.history.append({"username": username, "password": password})

        st.success("✅ Your credentials are ready!")

        # Show copyable fields
        st.text_input("Suggested Username", value=username, key="generated_username", disabled=True)
        st.text_input("Generated Password", value=password, key="generated_password", disabled=True)
    else:
        st.warning("Please enter both nickname and real name.")

# Sidebar: History
st.sidebar.header("🕘 History")
if st.session_state.history:
    for idx, item in enumerate(reversed(st.session_state.history), 1):
        st.sidebar.markdown(f"**{idx}.** `{item['username']}` | `{item['password']}`")
else:
    st.sidebar.info("No history yet.")
