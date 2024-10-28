import streamlit as st
import openai

# Set up OpenAI secret key
openai.api_key = "YOUR_OPENAI_SECRET_KEY"

def generate_json(text):
    # Call OpenAI API to generate JSON
    response = openai.Completion.create(
        engine="davinci",
        prompt=text,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
        temperature=0.7
    )
    
    # Extract the generated JSON from the response
    generated_json = response.choices[0].text.strip()
    
    return generated_json

# Streamlit app
def main():
    st.title("JSON Generator")
    
    # Input text
    input_text = st.text_area("Enter plain text", "")
    
    if st.button("Generate JSON"):
        # Generate JSON from input text
        generated_json = generate_json(input_text)
        
        # Display the generated JSON
        st.text_area("Generated JSON", generated_json)

if __name__ == "__main__":
    main()