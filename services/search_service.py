import feedparser
import urllib.parse

class SearchService:

    ARXIV_URL = "http://export.arxiv.org/api/query?"

    def search_arxiv(self, query: str, max_results: int = 5):
        encoded_query = urllib.parse.quote(query)
        url = f"{self.ARXIV_URL}search_query=all:{encoded_query}&start=0&max_results={max_results}"

        feed = feedparser.parse(url)

        papers = []

        for entry in feed.entries:
            paper = {
                "title": entry.title,
                "authors": [a.name for a in entry.authors],
                "summary": entry.summary,
                "link": entry.link,
                "published": entry.published
            }
            papers.append(paper)

        return papers
