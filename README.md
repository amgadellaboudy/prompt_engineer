# 🧠 Prompt Optimizer GPT

**A GPT-powered assistant that takes your raw, vague prompt and transforms it into a clean, structured, high-performance instruction.**

Built with OpenAI + LangChain + Streamlit, this tool acts as your personal prompt engineer — rewriting low-quality prompts into ones that actually get the results you want from GPT.

---

## ✨ What It Does

* 🪄 Rewrites weak prompts using best practices
* 📐 Adds structure, delimiters, role definitions, and output formatting
* 🤖 Automatically runs the optimized prompt via GPT-4o
* 🧪 Returns both the optimized prompt and the GPT output
* 💡 Built as a developer tool, demo app, or micro-API

---

## 🔧 Use Cases

* ✅ Devs building LLM apps who need consistent behavior
* ✅ Founders/PMs who want GPT to “just work”
* ✅ Prompt engineers looking to stress-test ideas
* ✅ Teams working with AI assistants and agents

---

## 📦 Quickstart

```bash
# Clone the repo
git clone https://github.com/amgadellaboudy/prompt-optimizer-gpt.git
cd prompt-optimizer-gpt

# Set up a virtual environment (optional)
python -m venv venv

# Activate the environment
# Mac/Linux:
source venv/bin/activate
# Windows:
.\venv\Scripts\Activate.ps1

# Install requirements
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## ⚙️ How It Works

1. User enters a raw prompt (e.g., “Summarize this email”)
2. A GPT-4o call rewrites the prompt using:

   * System role definition
   * Clear format instructions
   * \=== input delimiters
   * Output schema tips
3. A second GPT-4o call executes the optimized version
4. You get both the optimized prompt and output

---

## 👋 Work With Me

I'm an AI engineer focused on building production-ready GPT copilots and internal LLM tools. If you're:

* A team building an AI product but getting inconsistent GPT output
* A founder looking to add a reliable assistant to your stack
* A recruiter, legal team, or SaaS company using GPT but struggling with prompt design

📩 I can help:

* Design better GPT workflows
* Build structured, auditable LLM agents
* Tune or re-architect prompt pipelines for consistency

Feel free to reach out.

📧 Email: [amgad.ellaboudy@gmail.com](mailto:amgad.ellaboudy@gmail.com)
🔗 LinkedIn: [linkedin.com/in/amgadellaboudy](https://www.linkedin.com/in/amgad-ellaboudy-aa596726/)

---
