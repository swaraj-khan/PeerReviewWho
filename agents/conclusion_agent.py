from agents.base_agent import BaseAgent

class ConclusionAgent(BaseAgent):
    def __init__(self):
        super().__init__()

    def generate_conclusion(self, title: str, abstract: str, discussion: str) -> str:
        """Generates the conclusion section of the research paper."""
        prompt = f"""
Generate a conclusion section for a research paper.

The conclusion should:
- Be 200-300 words.
- Summarize the key findings from the discussion.
- Reiterate the paper's main contributions and significance.
- Suggest clear directions for future research.
- Provide a final, impactful closing statement.

Paper Title: {title}
Abstract: {abstract}
Discussion: {discussion}

Return ONLY the conclusion text.
"""
        result = self.llm.generate(prompt)
        return self._clean_llm_output(result, "Conclusion")