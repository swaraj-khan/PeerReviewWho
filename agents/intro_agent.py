from agents.base_agent import BaseAgent

class IntroAgent(BaseAgent):
    def __init__(self):
        super().__init__()

    def generate_introduction(self, title: str, abstract: str, topic: str, keywords: list, citations: list) -> str:
        """
        Generate an academic introduction for the research paper.
        
        Args:
            title: The paper title
            abstract: The generated abstract
            topic: The research topic
            keywords: List of keywords
            citations: List of relevant citations
            
        Returns:
            str: Generated introduction text
        """
        
        citation_context = ""
        if citations:
            citation_context = "Key related works include: "
            for i, citation in enumerate(citations[:3]):
                citation_context += f"{citation['title']} ({citation['authors'][0] if citation['authors'] else 'Unknown'} et al.); "
        
        prompt = f"""
Generate a comprehensive academic introduction for a research paper.

The introduction should:
- Be 300-500 words
- Provide background and context for the research
- Clearly state the research problem/question
- Review relevant literature (briefly)
- State the paper's contributions
- Outline the paper structure

Paper Title: {title}
Abstract: {abstract}
Research Topic: {topic}
Keywords: {keywords}
{citation_context}

Return ONLY the introduction text, no additional formatting or explanations.
"""

        result = self.llm.generate(prompt)
        
        return self._clean_llm_output(result, "Introduction")
