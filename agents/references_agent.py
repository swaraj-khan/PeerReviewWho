from agents.base_agent import BaseAgent

class ReferencesAgent(BaseAgent):
    def __init__(self):
        super().__init__()

    def generate_references(self, citations: list, literature_review: str) -> list:
        """
        Generate a formatted references list for the research paper.
        
        Args:
            citations: List of citation objects from arXiv
            literature_review: The literature review text
            
        Returns:
            list: List of formatted references
        """
        
        formatted_references = []
        
        for i, citation in enumerate(citations):
            authors = ", ".join(citation['authors'][:3])
            if len(citation['authors']) > 3:
                authors += " et al."
            
            year = citation['published'][:4] if citation['published'] else "n.d."
            
            key = f"b{i + 1}"
            reference_text = f"{authors}. ({year}). {citation['title']}. arXiv preprint arXiv:{citation['link'].split('/')[-1] if citation['link'] else 'unknown'}."
            formatted_references.append({'key': key, 'ref': reference_text})
        
        if literature_review:
            prompt = f"""
Based on the following literature review, generate 3-5 additional relevant academic references in APA format.
The references should be realistic and appropriate for the research topic.

Literature Review:
{literature_review}

Return ONLY a JSON array of reference strings in APA format:
[
  "Author1, A., & Author2, B. (Year). Title. Journal, Volume(Issue), Pages.",
  "Author3, C. (Year). Book Title. Publisher.",
  ...
]
"""

            result = self.llm.generate(prompt)
            
            additional_references = self._parse_json_output(result)
            if isinstance(additional_references, list):
                for ref_text in additional_references:
                    key = f"b{len(formatted_references) + 1}"
                    formatted_references.append({'key': key, 'ref': ref_text})
        
        return formatted_references
