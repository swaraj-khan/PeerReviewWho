import re
import json
from services.llm_service import LLMService

class BaseAgent:
    def __init__(self):
        self.llm = LLMService()

    def _clean_llm_output(self, result: str, section_name: str = "") -> str:
        """Cleans up markdown and section headers from LLM output."""
        cleaned = re.sub(r"```(json)?|```", "", result, flags=re.IGNORECASE).strip()
        
        if section_name:
            pattern = r"^\s*(#+\s*|\*\*|__)?\s*" + re.escape(section_name) + r"\s*(\*\*|__|:)?\s*\n?"
            cleaned = re.sub(pattern, "", cleaned, flags=re.IGNORECASE).strip()
            
        return cleaned

    def _parse_json_output(self, result: str) -> dict | list:
        """Cleans and parses JSON output from the LLM, returning a default on failure."""
        cleaned = self._clean_llm_output(result)
        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            print(f"Warning: Failed to parse JSON from LLM output: {cleaned}")
            if cleaned.strip().startswith('['):
                return []
            return {}