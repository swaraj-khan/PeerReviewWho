from agents.base_agent import BaseAgent

class ResultsAgent(BaseAgent):
    def __init__(self):
        super().__init__()

    def generate_results(self, title: str, topic: str, paper_type: str, methodology: str, keywords: list) -> str:
        """
        Generate a results section for the research paper.
        
        Args:
            title: The paper title
            topic: The research topic
            paper_type: Type of paper (survey/experimental/theoretical/review)
            methodology: The methodology section
            keywords: List of keywords
            
        Returns:
            str: Generated results text
        """
        
        results_guidance = ""
        if paper_type.lower() == "experimental":
            results_guidance = """
The results should include:
- Experimental findings and data
- Statistical analysis results
- Tables and figures (describe them)
- Key observations
- Patterns and trends
"""
        elif paper_type.lower() == "survey":
            results_guidance = """
The results should include:
- Survey response statistics
- Demographic breakdowns
- Key findings from survey data
- Response patterns
- Statistical analysis results
"""
        elif paper_type.lower() == "theoretical":
            results_guidance = """
The results should include:
- Theoretical findings
- Model outputs and predictions
- Analytical results
- Key theorems or propositions
- Validation outcomes
"""
        else: 
            results_guidance = """
The results should include:
- Synthesis of reviewed literature
- Key themes and patterns
- Comparative analysis
- Gaps and limitations identified
- Summary of findings across studies
"""
        
        prompt = f"""
Generate a results section for a research paper based on the methodology.

The results should:
- Be 400-600 words
- Present findings clearly and objectively
- Connect to the methodology
- Include appropriate data presentation
- If you include a table, use standard Markdown format.
- Highlight key discoveries

Paper Title: {title}
Research Topic: {topic}
Paper Type: {paper_type}
Methodology: {methodology}
Keywords: {keywords}

{results_guidance}

Return ONLY the results text, no additional formatting or explanations.
"""

        result = self.llm.generate(prompt)
        
        return self._clean_llm_output(result, "Results")
