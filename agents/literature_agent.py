from agents.base_agent import BaseAgent

class LiteratureAgent(BaseAgent):
    def __init__(self):
        super().__init__()

    def generate_literature_review(self, title: str, topic: str, keywords: list, citations: list) -> str:
        """
        Generate a comprehensive literature review for the research paper.
        
        Args:
            title: The paper title
            topic: The research topic
            keywords: List of keywords
            citations: List of relevant citations
            
        Returns:
            str: Generated literature review text
        """
        
        citation_details = ""
        if citations:
            citation_details = "Key papers to include in the literature review:\n"
            for i, citation in enumerate(citations):
                citation_details += f"- {citation['title']} by {', '.join(citation['authors'][:3]) if citation['authors'] else 'Unknown authors'} ({citation['published'][:4] if citation['published'] else 'Unknown year'})\n"
                citation_details += f"  Summary: {citation['summary'][:200]}...\n\n"
        
        prompt = f"""
Generate a comprehensive literature review for a research paper.

The literature review should:
- Be 500-800 words
- Survey the relevant research field
- Critically analyze existing work
- Identify gaps in current research
- Connect previous work to the current study
- Organize papers thematically or chronologically

Paper Title: {title}
Research Topic: {topic}
Keywords: {keywords}

{citation_details}

Return ONLY the literature review text, no additional formatting or explanations.
"""

        result = self.llm.generate(prompt)
        
        return self._clean_llm_output(result, "Literature Review")
