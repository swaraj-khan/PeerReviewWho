from agents.base_agent import BaseAgent

class DiscussionAgent(BaseAgent):
    def __init__(self):
        super().__init__()

    def generate_discussion(self, title: str, introduction: str, literature_review: str, results: str) -> str:
        """Generates the discussion section of the research paper."""
        prompt = f"""
Generate a discussion section for a research paper.

The discussion should:
- Be 400-600 words.
- Interpret the findings presented in the results section.
- Compare and contrast the findings with existing work from the literature review.
- Discuss the broader implications and significance of the findings.
- Honestly acknowledge the limitations of the study.

Paper Title: {title}
Introduction Summary: {introduction[:500]}
Literature Review Summary: {literature_review[:500]}
Results Section: {results}

Return ONLY the discussion text.
"""
        result = self.llm.generate(prompt)
        return self._clean_llm_output(result, "Discussion")