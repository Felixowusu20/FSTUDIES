 # FChatbot

from openai import OpenAI
import streamlit as st

# Set up the Streamlit app title and sidebar
st.set_page_config(
    page_title="Ella",
    page_icon=":robot_face:",
    layout="wide",

 
)

st.title("🤖 Ella")
st.sidebar.title("About 🤖 Ella")
st.sidebar.info(
    """
    Ella is an AI-powered chatbot built using OpenAI's model. 
    You can ask it anything, and it will provide you with relevant answers.
    make sure you use Ella to guide answer all the problems that youc couldn't solve.
    """
)

# Initialize the OpenAI client
client = OpenAI(api_key= "sk-proj-TwRmFL05p6hOHS51SSSyT3BlbkFJdO9MqczzeXKPXchVZaBb")

# Main chat interface
st.subheader("Hi ,I'm Ella Your Daily Companion.")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Questions for Ella?" ):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("🤖 Ella is Thinking..."):
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            for response in client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            ):
                if response.choices:
                    if response.choices[0].delta:
                        if response.choices[0].delta.content:
                            full_response += response.choices[0].delta.content
                            message_placeholder.markdown(full_response + " ")
            message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    
    
# # Feedback mechanism
#     feedback = st.selectbox("How helpful was the response?", ["😊😊", "😐😊😊", "😞😊😊😊"])
#     if feedback:
#         if st.session_state.messages:
#             st.session_state.messages[-1]["feedback"] = feedback
#         else:
#             st.session_state.messages = [{"feedback": feedback}]  
#         st.info("Thank you for your feedback!")
    st.balloons()


