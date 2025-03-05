import streamlit as st
from transformers import pipeline
import time

# Load a pre-trained Hugging Face Model
chatbot = pipeline("text-generation", model="distilgpt2")

def healthcare_chatbot(user_input):
    """Handles user queries with rule-based responses and AI-generated replies."""
    user_input = user_input.lower()
    
    keyword_responses = {
        "symptom": "For proper guidance, please seek advice from a doctor.",
        "appointment": "Would you like to book an appointment with the doctor?",
        "medication": "Taking prescribed medication regularly is essential. If you have any questions, don't hesitate to consult your doctor.",
        "emergency": "If it's an emergency, please call emergency services or visit the nearest hospital.",
        "diet": "Maintaining a balanced diet is crucial for good health. Would you like some dietary recommendations?",
        "exercise": "Regular exercise helps improve overall health. Do you want some fitness tips?"
    }
    
    for keyword, response in keyword_responses.items():
        if keyword in user_input:
            return response
    
    # Generate AI-based response for other inputs
    response = chatbot(user_input, max_length=100, num_return_sequences=1)
    return response[0]['generated_text']

# Streamlit web app interface
def main():
    st.set_page_config(page_title="Healthcare Assistant", page_icon="🩺", layout="wide")
    st.title("🩺 Healthcare Assistant Chatbot")
    st.write("Hello! I'm **Ella**, your AI-powered health assistant. How can I assist you today?")
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    # Sidebar for additional options
    with st.sidebar:
        st.header("🛠️ Options")
        st.write("Customize your chatbot experience.")
        clear_chat = st.button("🗑️ Clear Chat History")
        if clear_chat:
            st.session_state.chat_history = []
            st.success("Chat history cleared!")
    
    # Main chat interface
    st.subheader("💬 Chat with Ella")
    user_input = st.text_input("Your Question:", key="user_input")
    if st.button("Ask Ella"): 
        if user_input.strip():
            with st.spinner("Thinking..."):
                time.sleep(1)
                response = healthcare_chatbot(user_input)
                
            # Save chat history
            st.session_state.chat_history.append((user_input, response))
    
    # Display chat history
    st.subheader("📜 Conversation History")
    for user_msg, bot_msg in st.session_state.chat_history:
        st.write(f"**You:** {user_msg}")
        st.write(f"**Ella:** {bot_msg}")
    
    st.markdown("---")
    st.caption("🤖 Powered - AI & Streamlit by Jayesh Sharma")
    
    # Footer with health resources
    st.subheader("📚 Health Resources")
    st.write("Here are some trusted health resources:")
    st.markdown("- [World Health Organization](https://www.who.int/)")
    st.markdown("- [Mayo Clinic](https://www.mayoclinic.org/)")
    st.markdown("- [MedlinePlus](https://medlineplus.gov/)")
    st.markdown("- [Centers for Disease Control and Prevention](https://www.cdc.gov/)")

if __name__ == "__main__":
    main()
