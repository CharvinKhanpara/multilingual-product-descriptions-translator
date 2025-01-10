from transformers import pipeline
from googletrans import Translator
import streamlit as st

# Load a pre-trained text generation model
generator = pipeline('text-generation', model='openai-community/gpt2')

def generate_description(product_details):
    prompt = f"Write a concise product description for: {product_details}"
    result = generator(prompt, max_length=100, num_return_sequences=1)
    return result[0]['generated_text']


translator = Translator()

def translate_text(text, target_language):
    translation = translator.translate(text, dest=target_language)
    return translation.text


def generate_multilingual_description(product_details, languages):
    description = generate_description(product_details)
    translations = {lang: translate_text(description, lang) for lang in languages}
    return description, translations





st.title("Multilingual Product Descriptions")

product_details = st.text_input("Enter product details:")
# languages = st.multiselect("Select target languages:", ['(es)spanish', '(fr)french', '(de)German', '(hi)hindi', 'zh(Chinese)'])
languages = st.multiselect(
    "Select target languages:", 
    ['es', 'fr', 'de', 'hi', 'zh-cn', 'ja', 'ru', 'it', 'pt']
)


if st.button("Generate"):
    if product_details and languages:
        original, translations = generate_multilingual_description(product_details, languages)
        st.subheader("Original Description:")
        st.write(original)
        
        st.subheader("Translations:")
        for lang, translation in translations.items():
            st.write(f"{lang.upper()}: {translation}")
    else:
        st.error("Please enter product details and select languages.")



# import streamlit as st
# from transformers import pipeline
# from googletrans import Translator

# # Load the text generation model
# generator = pipeline('text-generation', model='openai-community/gpt2')

# # Initialize the translator
# translator = Translator()

# # Function to generate product description
# def generate_description(product_details):
#     prompt = f"Generate a product description for: {product_details}"
#     result = generator(prompt, max_length=100, num_return_sequences=1)
#     return result[0]['generated_text']

# # Function to translate text into multiple languages
# def translate_text(text, target_language):
#     translation = translator.translate(text, dest=target_language)
#     return translation.text

# # Main function for Streamlit
# def main():
#     st.title("Generative AI: Multilingual Product Descriptions")
#     st.markdown("**Create product descriptions and translate them into multiple languages.**")
    
#     # Input for product details
#     product_details = st.text_input("Enter product details (e.g., Stainless steel water bottle):")
    
#     # Language selection
#     languages = st.multiselect("Select target languages:", 
#                                 {'es': 'Spanish', 'fr': 'French', 'de': 'German', 'hi': 'Hindi', 'zh-cn': 'Chinese'})
    
#     # Generate button
#     if st.button("Generate"):
#         if product_details and languages:
#             # Generate description
#             original_description = generate_description(product_details)
            
#             # Translate to selected languages
#             translations = {lang: translate_text(original_description, lang) for lang in languages}
            
#             # Display results
#             st.subheader("Original Product Description:")
#             st.write(original_description)
            
#             st.subheader("Translated Descriptions:")
#             for lang, translation in translations.items():
#                 st.write(f"**{lang.upper()}**: {translation}")
#         else:
#             st.error("Please provide product details and select at least one language.")

# if __name__ == "__main__":
#     main()