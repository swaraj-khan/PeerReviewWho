from concurrent.futures import ThreadPoolExecutor
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from services.llm_service import LLMService
from memory.shared_state import SharedState
from agents.title_agent import TitleAgent
from agents.citation_agent import CitationAgent
from agents.abstract_agent import AbstractAgent
from agents.intro_agent import IntroAgent
from agents.literature_agent import LiteratureAgent
from agents.methodology_agent import MethodologyAgent
from agents.results_agent import ResultsAgent
from agents.references_agent import ReferencesAgent
from agents.discussion_agent import DiscussionAgent
from agents.citation_placing_agent import CitationPlacingAgent
from agents.conclusion_agent import ConclusionAgent
from agents.latex_agent import LatexAgent
from agents.base_agent import BaseAgent


class Orchestrator(BaseAgent):
    def __init__(self):
        super().__init__()
        self.console = Console()
        self.memory = SharedState()
        self.title_agent = TitleAgent()
        self.citation_agent = CitationAgent()
        self.abstract_agent = AbstractAgent()
        self.intro_agent = IntroAgent()
        self.literature_agent = LiteratureAgent()
        self.methodology_agent = MethodologyAgent()
        self.results_agent = ResultsAgent()
        self.references_agent = ReferencesAgent()
        self.discussion_agent = DiscussionAgent()
        self.citation_placing_agent = CitationPlacingAgent()
        self.conclusion_agent = ConclusionAgent()
        self.latex_agent = LatexAgent()

    def understand_idea(self, user_input: str):
        prompt = f"""
            Analyze the following research idea.
            Return ONLY valid JSON.
            Format:
            {{
            "topic": "short research topic",
            "keywords": ["k1","k2","k3","k4","k5"],
            "domain": "computer science / medicine / law / etc",
            "paper_type": "survey / experimental / theoretical / review"
            }}
            User Idea:
            {user_input}
            """
        result = self.llm.generate(prompt)
        data = self._parse_json_output(result)
        self.memory.update("user_idea", user_input)
        self.memory.update("topic", data["topic"])
        self.memory.update("keywords", data["keywords"])
        self.memory.update("domain", data["domain"])
        self.memory.update("paper_type", data["paper_type"])

    def run(self, user_input: str):
        progress_columns = [
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeElapsedColumn(),
        ]

        with Progress(*progress_columns, console=self.console) as progress:
            main_task = progress.add_task("[bold blue]Generating Research Paper...", total=7)

            progress.update(main_task, description="[bold blue]Phase 1: Understanding Idea...")
            self.understand_idea(user_input)
            self.console.print(Panel(f"Topic: {self.memory.get('topic')}\nType: {self.memory.get('paper_type')}", title="[bold green]✔ Idea Analyzed[/bold green]", border_style="green"))
            progress.update(main_task, advance=1)

            with ThreadPoolExecutor(max_workers=3) as executor:
                progress.update(main_task, description="[bold blue]Phase 2: Laying Foundations...")
                p2_task = progress.add_task("Drafting...", total=3)
                future_titles = executor.submit(
                    self.title_agent.generate_titles, self.memory.get("topic"), self.memory.get("keywords"))
                future_citations = executor.submit(
                    self.citation_agent.find_citations, self.memory.get("topic"), self.memory.get("keywords"))
                future_method = executor.submit(
                    self.methodology_agent.generate_methodology,
                    f"A paper on {self.memory.get('topic')}", self.memory.get("topic"), self.memory.get("paper_type"), self.memory.get("keywords"))
                
                titles = future_titles.result()
                progress.update(p2_task, advance=1, description="Titles generated")
                citations = future_citations.result()
                progress.update(p2_task, advance=1, description="Citations found")
                methodology = future_method.result()
                progress.update(p2_task, advance=1, description="Methodology drafted")
                
                self.memory.update("citations", citations)
                selected_title = titles[0]
                self.memory.update("title", selected_title)
                self.memory.update("methodology", methodology)
                self.console.print(Panel(f"Selected Title: {selected_title}\nCitations Found: {len(citations)}", title="[bold green]✔ Initial Content Ready[/bold green]", border_style="green"))
                progress.update(main_task, advance=1)

                progress.update(main_task, description="[bold blue]Phase 3: Drafting Core Literature...")
                p3_task = progress.add_task("Drafting...", total=2)
                future_abstract = executor.submit(
                    self.abstract_agent.generate_abstract,
                    self.memory.get("title"), self.memory.get("topic"), self.memory.get("keywords"), self.memory.get("citations"))
                future_lit = executor.submit(
                    self.literature_agent.generate_literature_review,
                    self.memory.get("title"), self.memory.get("topic"), self.memory.get("keywords"), self.memory.get("citations"))
                
                abstract = future_abstract.result()
                progress.update(p3_task, advance=1, description="Abstract written")
                lit_review = future_lit.result()
                progress.update(p3_task, advance=1, description="Literature Review written")

                self.memory.update("abstract", abstract)
                self.memory.update("literature_review", lit_review)
                progress.update(main_task, advance=1)

                progress.update(main_task, description="[bold blue]Phase 4: Writing Intro & Results...")
                p4_task = progress.add_task("Writing...", total=2)
                future_intro = executor.submit(
                    self.intro_agent.generate_introduction,
                    self.memory.get("title"), self.memory.get("abstract"), self.memory.get("topic"), self.memory.get("keywords"), self.memory.get("citations"))
                future_results = executor.submit(
                    self.results_agent.generate_results,
                    self.memory.get("title"), self.memory.get("topic"), self.memory.get("paper_type"), self.memory.get("methodology"), self.memory.get("keywords"))

                intro = future_intro.result()
                progress.update(p4_task, advance=1, description="Introduction written")
                results = future_results.result()
                progress.update(p4_task, advance=1, description="Results written")

                self.memory.update("introduction", intro)
                self.memory.update("results", results)
                progress.update(main_task, advance=1)

                progress.update(main_task, description="[bold blue]Phase 5: Discussing & Referencing...")
                p5_task = progress.add_task("Writing...", total=2)
                future_discussion = executor.submit(
                    self.discussion_agent.generate_discussion,
                    self.memory.get("title"), self.memory.get("introduction"), self.memory.get("literature_review"), self.memory.get("results"))
                future_refs = executor.submit(
                    self.references_agent.generate_references,
                    self.memory.get("citations"), self.memory.get("literature_review"))

                discussion = future_discussion.result()
                progress.update(p5_task, advance=1, description="Discussion written")
                references = future_refs.result()
                progress.update(p5_task, advance=1, description="References compiled")

                self.memory.update("references", references)
                self.memory.update("discussion", discussion)
                progress.update(main_task, advance=1)

                progress.update(main_task, description="[bold blue]Phase 6: Concluding Paper...")
                p6_task = progress.add_task("Concluding...", total=1)
                conclusion = self.conclusion_agent.generate_conclusion(
                    self.memory.get("title"), self.memory.get("abstract"), self.memory.get("discussion"))
                self.memory.update("conclusion", conclusion)
                progress.update(p6_task, advance=1)
                progress.update(main_task, advance=1)

            progress.update(main_task, description="[bold blue]Phase 7: Placing Citations...")
            p7_task = progress.add_task("Placing citations...", total=3)
            
            intro_text = self.memory.get("introduction")
            lit_review_text = self.memory.get("literature_review")
            discussion_text = self.memory.get("discussion")
            references_list = self.memory.get("references")

            intro_with_citations = self.citation_placing_agent.add_citations_to_section(intro_text, references_list)
            self.memory.update("introduction", intro_with_citations)
            progress.update(p7_task, advance=1, description="Citations placed in Introduction")

            lit_review_with_citations = self.citation_placing_agent.add_citations_to_section(lit_review_text, references_list)
            self.memory.update("literature_review", lit_review_with_citations)
            progress.update(p7_task, advance=1, description="Citations placed in Literature Review")

            discussion_with_citations = self.citation_placing_agent.add_citations_to_section(discussion_text, references_list)
            self.memory.update("discussion", discussion_with_citations)
            progress.update(p7_task, advance=1, description="Citations placed in Discussion")
            progress.update(main_task, advance=1)

            progress.update(main_task, description="[bold blue]Final Phase: Compiling PDF...")
            final_task = progress.add_task("Compiling...", total=1)
            output_file = self.latex_agent.generate_latex(self.memory.dump(), "research_paper")
            progress.update(final_task, advance=1)

        self.console.print(Panel(f"Research Paper Generation Complete!\nOutput file: [bold cyan]{output_file}[/bold cyan]", title="[bold green]✔ Success[/bold green]", border_style="green"))
        return self.memory.dump()
