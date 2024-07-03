import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Water Guardian", page_icon="🌊")

st.title("🌊 Water Guardian")

# Predefined water-related prompts and responses
prompts_responses = {
    "What are the benefits of drinking water?": "Drinking water helps maintain the balance of body fluids, aids digestion, controls calories, energizes muscles, and keeps skin looking good.",
    "How does water support life on Earth?": "Water is essential for all living organisms. It is a solvent, a temperature buffer, a metabolite, and a living environment.",
    "What are some interesting facts about oceans?": "Oceans cover more than 70% of the Earth's surface, contain 97% of the Earth's water, and produce more than half of the world's oxygen.",
    "How can we conserve water in our daily lives?": "We can conserve water by fixing leaks, taking shorter showers, turning off the tap while brushing teeth, and using water-efficient appliances.",
    "What are the effects of water pollution?": "Water pollution can lead to health issues, harm aquatic life, disrupt ecosystems, and contaminate drinking water sources.",
    "How does the water cycle work?": "The water cycle involves the continuous movement of water on, above, and below the surface of the Earth through processes like evaporation, condensation, and precipitation.",
    "What is the importance of clean water?": "Clean water is vital for drinking, sanitation, agriculture, and industrial processes. It is essential for health, development, and ecosystems."
}

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Display prompts as radio buttons
selected_prompt = st.radio("Select a prompt about water:", list(prompts_responses.keys()))

# Add a button to submit the selected prompt
if st.button("Submit Prompt"):
    st.session_state.messages.append({"role": "user", "content": selected_prompt})
    with st.chat_message("user"):
        st.markdown(selected_prompt)

    response = prompts_responses[selected_prompt]
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Handle user input through chat input
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate a placeholder response for custom inputs
    response = "This is a placeholder response. Please select a predefined prompt."
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
