from pydantic import BaseModel


class OptimizedPromptResult(BaseModel):
    optimized_prompt: str
    output: str
