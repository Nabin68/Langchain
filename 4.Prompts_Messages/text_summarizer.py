from langchain_cohere import ChatCohere
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import streamlit as st

load_dotenv()

model = ChatCohere(model="command-a-03-2025")

st.set_page_config(page_title="Text Summarizer", page_icon="🧠", layout="centered")
st.header("🧠 Text Summarizer Tool")

text_input = st.text_area("📝 Enter your text here...", height=200)

style_input = st.selectbox(
    "🎨 Select Summarization Style",
    ["Select..", "Factual", "Dramatic", "Balanced"]
)

length_input = st.selectbox(
    "📏 Select the Length",
    ["Select..", "Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (Detailed Explanation)"]
)

template = PromptTemplate(
    input_variables=["text_input", "style_input", "length_input"],
    template="""
        Please summarize the following text:

        "{text_input}"

        Follow these specifications:

        Explanation Style: {style_input}
        Explanation Length: {length_input}

        1. Key Points:
        - Capture the most important ideas and arguments.
        - Avoid unnecessary details or repetition.

        2. Clarity:
        - Use simple, easy-to-understand language.
        - Maintain coherence and logical flow.

        3. Tone:
        - Follow the tone specified in {style_input} (e.g., formal, academic, conversational).

        If certain details are unclear or missing, respond with: "Insufficient information available."

        Ensure the summary is concise, accurate, and aligned with the provided style and length.
    """
)

if st.button("✨ Summarize"):
    if not text_input or style_input == "Select.." or length_input == "Select..":
        st.warning("⚠️ Please provide all inputs (text, style, and length) before summarizing.")
    else:
        # Build the prompt
        prompt = template.invoke({
            "text_input": text_input,
            "style_input": style_input,
            "length_input": length_input
        })

        with st.spinner("⏳ Summarizing..."):
            try:
                result = model.invoke(prompt)
                st.subheader("🧾 Summary:")
                st.write(result.content)
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")























# from langchain_cohere import ChatCohere
# from dotenv import load_dotenv
# import streamlit as st
# from langchain_core.prompts import PromptTemplate

# load_dotenv()

# model=ChatCohere(
#     model="command-a-03-2025"
# )
# st.header("Text_Summarizer Tool")

# text_input=st.text_input("Enter your text here..")
# style_input=st.selectbox("Select Summarization style",["Select..","Factual","Dramatic","Balanced"])
# length_input=st.selectbox("Select the length",["Select..","Short(1-2 paragraphs)","Medium(3-5 paragraphs)","Long(Detailed Explanation)"])

# template=PromptTemplate(
#     template = """
#     Please summarize the given text {text_input} with the following specifications:

#     Explanation Style: {style_input}
#     Explanation Length: {length_input}

#     1. Key Points:
#     - Capture the most important ideas and arguments.
#     - Avoid unnecessary details or repetition.

#     2. Clarity:
#     - Use simple, easy-to-understand language.
#     - Maintain coherence and logical flow.

#     3. Tone:
#     - Follow the tone specified in {style_input} (e.g., formal, academic, conversational).

#     If certain details are unclear or missing in the text, respond with: "Insufficient information available" instead of making assumptions.

#     Ensure the summary is concise, accurate, and aligned with the provided style and length.
#     """,
#     input_variables=["text_input","style_input","length_input"]
# )

# prompt=template.invoke({
#     "text_input":text_input,
#     "style_input":style_input,
#     "length_input":length_input
# })

# if st.button("Summarize"):
#     result=model.invoke(prompt)
#     st.text(result.content)
    
     