import streamlit as st
import openai
from openai import OpenAI
from prompts import basic_prompt, few_shot_shakespeare_prompt, lewis_carrol_prompt, few_shot_lewis_carrol_prompt

# Get your API key from Streamlit secrets
api_key = st.secrets["openai"]["api_key"]

if not api_key:
    st.error("API key not found. Please check your Streamlit secrets.")
else:
    # Set the API key
    openai.api_key = api_key

    # Initialize the OpenAI client
    client = OpenAI(api_key=api_key)

    st.title("📝 Style Transformer")

    user_input = st.text_input("Enter a modern English sentence:")

    style_mode = st.selectbox("Choose style mode:", ["Shakespeare", "Lewis Carroll"])

    prompt_type = st.selectbox("Choose prompt type:", ["Regular", "Few-Shot"])

    if st.button("Translate!"):
        if user_input.strip() == "":
            st.error("Please enter a sentence to translate.")
        else:
            try:
                # Prepare the prompt based on the selected style mode and prompt type
                if style_mode == "Shakespeare":
                    if prompt_type == "Regular":
                        prompt = basic_prompt(user_input)  # Regular Shakespeare style
                    else:
                        prompt = few_shot_shakespeare_prompt(user_input)  # Few-shot Shakespeare style
                elif style_mode == "Lewis Carroll":
                    if prompt_type == "Regular":
                        prompt = lewis_carrol_prompt(user_input)  # Regular Lewis Carroll style
                    else:
                        prompt = few_shot_lewis_carrol_prompt(user_input)  # Few-shot Lewis Carroll style

                # Ensure the prompt is correctly generated
                if not prompt:
                    st.error("Generated prompt is empty. Please check the prompt generation logic.")
                else:
                    # Create the message structure as required by OpenAI API
                    messages = [{"role": "user", "content": prompt}]

                    # Make OpenAI API request
                    response = client.chat.completions.create(
                        model="gpt-4",  # Specify the model to use
                        messages=messages  # Pass the list of messages
                    )

                    # Extract the styled text from the response using the correct attributes
                    styled_text = response.choices[0].message.content

                    st.subheader(f"🎭 {style_mode} Version ({prompt_type}):")
                    st.write(styled_text)

            except openai.APIError as e:
                # Handle API error here
                st.error(f"OpenAI API returned an API Error: {e}")
            except openai.APIConnectionError as e:
                # Handle connection error here
                st.error(f"Failed to connect to OpenAI API: {e}")
            except openai.RateLimitError as e:
                # Handle rate limit error
                st.error(f"OpenAI API request exceeded rate limit: {e}")
            except Exception as e:
                # Handle any other unexpected errors
                st.error(f"An unexpected error occurred: {e}")
