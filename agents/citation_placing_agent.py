import re
from agents.base_agent import BaseAgent

class CitationPlacingAgent(BaseAgent):
    def __init__(self):
        super().__init__()

    def add_citations_to_section(self, text_section: str, references: list) -> str:
        """Injects citation placeholders into a text section based on a list of references."""
        
        if not references or not text_section.strip():
            return text_section

        reference_list_str = ""
        for ref in references:
            reference_list_str += f"- {ref['key']}: {ref['ref']}\n"

        prompt = f"""
You are an academic editor. Your task is to add in-text citation placeholders to a section of a research paper.
You will be given a text section and a list of available references with keys.
Read the text and insert a citation placeholder `[CITE:key]` where the text discusses or refers to information from a specific reference.
Place citations appropriately, usually at the end of a sentence or clause that relies on the cited work. Do not add too many citations; only cite where it is clearly necessary.

**Available References:**
{reference_list_str}

**Text to Edit:**
---
{text_section}
---

Return ONLY the edited text with the `[CITE:key]` placeholders. Do not change the original text otherwise.
"""
        result = self.llm.generate(prompt)
        cleaned = re.sub(r"```(text)?|```", "", result, flags=re.IGNORECASE).strip()
        return cleaned