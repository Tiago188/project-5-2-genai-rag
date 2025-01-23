import streamlit as st
import openai
import os

# %pip install streamlit


# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit app
st.title("Question Answering App")

# Input for user question
user_question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if user_question:
        # Prepare the messages for the OpenAI API
        messages = [
            {"role": "system", "content": "You are a knowledgeable and factual chatbot."},
            {"role": "user", "content": user_question}
        ]

        # Model parameters
        model_params = {
            "model": "gpt-4o",
            "temperature": 0.7,
            "max_tokens": 4000,
            "top_p": 0.9,
            "frequency_penalty": 0.5,
            "presence_penalty": 0.6
        }

        # Get the completion from OpenAI API
        completion = openai.ChatCompletion.create(messages=messages, **model_params, timeout=120)
        answer = completion.choices[0].message.content

        # Display the answer
        st.write("### Answer:")
        st.write(answer)
    else:
        st.write("Please enter a question.")