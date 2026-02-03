from agents.base_agent import BaseAgent

class AbstractAgent(BaseAgent):
    def __init__(self):
        super().__init__()

    def generate_abstract(self, title: str, topic: str, keywords: list, citations: list) -> str:
        """
        Generate an academic abstract for the research paper.
        
        Args:
            title: The selected paper title
            topic: The research topic
            keywords: List of keywords
            citations: List of relevant citations
            
        Returns:
            str: Generated abstract text
        """
        
        citation_summary = ""
        if citations:
            citation_summary = "Relevant research includes: "
            for i, citation in enumerate(citations[:3]):
                citation_summary += f"{citation['title']}; "
        
        prompt = f"""
Generate a comprehensive academic abstract for a research paper.

The abstract should:
- Be 150-250 words
- Include the research problem/context
- Describe the methodology/approach
- Summarize key findings/results
- Mention implications/contributions
- Use academic language and proper structure

Paper Title: {title}
Research Topic: {topic}
Keywords: {keywords}
{citation_summary}

Return ONLY the abstract text, no additional formatting or explanations.
"""

        result = self.llm.generate(prompt)
        
        return self._clean_llm_output(result, "Abstract")
