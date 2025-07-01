from optimizer.schemas import OptimizedPromptResult
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(model="gpt-4o", temperature=0.3)


def optimize_prompt_and_run(raw_prompt: str) -> OptimizedPromptResult:
    meta_prompt = ChatPromptTemplate.from_template(
        """
        You are a world-class prompt engineer. Improve the following prompt by:
        - Adding a system role definition
        - Breaking it into clear task sections
        - Using === delimiters for any user inputs
        - Specifying output format
        - Making it deterministic and easy to parse

        Rewrite the prompt only — do not execute it.

        Original Prompt:
        ===
        {raw_prompt}
        ===

        Optimized Prompt:
        """
    )

    formatted = meta_prompt.format_messages(raw_prompt=raw_prompt)
    optimized_prompt = llm.invoke(formatted).content.strip()

    # Now use the optimized prompt to run a second GPT call
    final_output = llm.invoke([{"role": "user", "content": optimized_prompt}]).content.strip()

    return OptimizedPromptResult(optimized_prompt=optimized_prompt, output=final_output)
