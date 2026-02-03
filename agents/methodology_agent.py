from agents.base_agent import BaseAgent

class MethodologyAgent(BaseAgent):
    def __init__(self):
        super().__init__()

    def generate_methodology(self, title: str, topic: str, paper_type: str, keywords: list) -> str:
        """
        Generate a methodology section for the research paper.
        
        Args:
            title: The paper title
            topic: The research topic
            paper_type: Type of paper (survey/experimental/theoretical/review)
            keywords: List of keywords
            
        Returns:
            str: Generated methodology text
        """
        
        methodology_guidance = ""
        if paper_type.lower() == "experimental":
            methodology_guidance = """
The methodology should include:
- Experimental design and setup
- Data collection procedures
- Variables and measurements
- Statistical methods
- Experimental protocols
"""
        elif paper_type.lower() == "survey":
            methodology_guidance = """
The methodology should include:
- Survey design and development
- Sampling strategy and population
- Data collection methods
- Survey validation procedures
- Analysis techniques
"""
        elif paper_type.lower() == "theoretical":
            methodology_guidance = """
The methodology should include:
- Theoretical framework
- Model development process
- Assumptions and constraints
- Analytical methods
- Validation approach
"""
        else:  
            methodology_guidance = """
The methodology should include:
- Literature search strategy
- Inclusion/exclusion criteria
- Quality assessment methods
- Synthesis approach
- Analysis framework
"""
        
        prompt = f"""
Generate a detailed methodology section for a research paper.

The methodology should:
- Be 400-600 words
- Clearly describe the research approach
- Explain the methods and procedures used
- Justify methodological choices
- Be appropriate for the paper type

Paper Title: {title}
Research Topic: {topic}
Paper Type: {paper_type}
Keywords: {keywords}

{methodology_guidance}

Return ONLY the methodology text, no additional formatting or explanations.
"""

        result = self.llm.generate(prompt)
        
        return self._clean_llm_output(result, "Methodology")
