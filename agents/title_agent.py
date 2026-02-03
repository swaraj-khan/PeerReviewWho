from agents.base_agent import BaseAgent

class TitleAgent(BaseAgent):
    def __init__(self):
        super().__init__()

    def generate_titles(self, topic, keywords):
        prompt = f"""
Generate 3 academic research paper titles.

Return ONLY valid JSON.
Format:
{{
  "titles": ["t1", "t2", "t3"]
}}

Topic: {topic}
Keywords: {keywords}
"""

        result = self.llm.generate(prompt)
        data = self._parse_json_output(result)

        return data.get("titles", [])
