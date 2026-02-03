from services.search_service import SearchService

class CitationAgent:
    def __init__(self):
        self.search = SearchService()

    def find_citations(self, topic, keywords):
        query = topic + " " + " ".join(keywords[:3])
        papers = self.search.search_arxiv(query, max_results=5)
        return papers
