from typing import Dict, Any

class SharedState:
    def __init__(self):
        self.state: Dict[str, Any] = {
            "user_idea": "",
            "topic": "",
            "keywords": [],
            "domain": "",
            "paper_type": "",
            "title": "",
            "citations": [],
            "abstract": "",
            "introduction": "",
            "literature_review": "",
            "methodology": "",
            "results": "",
            "references": [],
            "discussion": "",
            "conclusion": ""
        }

    def update(self, key: str, value):
        self.state[key] = value

    def get(self, key: str):
        return self.state.get(key)

    def dump(self):
        return self.state
