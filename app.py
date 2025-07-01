import streamlit as st
from optimizer.agent import optimize_prompt_and_run

st.set_page_config(page_title="Prompt Optimizer GPT", layout="wide")
st.title("🧠 Prompt Optimizer GPT")
st.markdown("""
This assistant takes your raw GPT prompt and rewrites it using best practices —
like system-role clarification, output structuring, delimiters, and more.
""")

raw_prompt = st.text_area("✍️ Your Raw Prompt", height=200, placeholder="e.g., Summarize this meeting transcript…")

if st.button("🚀 Optimize and Run") and raw_prompt:
    with st.spinner("Optimizing and running prompt..."):
        result = optimize_prompt_and_run(raw_prompt)

        st.subheader("🧩 Optimized Prompt")
        st.code(result.optimized_prompt, language="markdown")

        st.subheader("📥 GPT Output")
        st.write(result.output)
