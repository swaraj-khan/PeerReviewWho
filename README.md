# Research-Agent

Research-Agent is a modular Python system for generating and assembling structured research papers using specialized agents.  
Each agent is responsible for a distinct section or responsibility in the paper generation pipeline, coordinated through a central orchestrator and shared memory.

<img width="1487" height="207" alt="image" src="https://github.com/user-attachments/assets/2912f785-b0d3-44d5-92a3-45c57e9b827a" />

<img width="1486" height="266" alt="image" src="https://github.com/user-attachments/assets/f77efc92-cf99-43ed-a9c5-39a65bb7399b" />


---

## Project Structure


```
Research-Agent
├─ agents
│  ├─ abstract_agent.py
│  ├─ base_agent.py
│  ├─ citation_agent.py
│  ├─ citation_placing_agent.py
│  ├─ conclusion_agent.py
│  ├─ discussion_agent.py
│  ├─ intro_agent.py
│  ├─ latex_agent.py
│  ├─ literature_agent.py
│  ├─ methodology_agent.py
│  ├─ orchestrator.py
│  ├─ references_agent.py
│  ├─ results_agent.py
│  ├─ title_agent.py
│  └─ __init__.py
├─ config
│  └─ settings.py
├─ main.py
├─ memory
│  └─ shared_state.py
├─ README.md
├─ requirements.txt
├─ research_paper.tex
└─ services
   ├─ llm_service.py
   └─ search_service.py

```
---

## Architecture Overview

The system follows an agent-oriented architecture where each section of a research paper is generated independently and then composed into a final LaTeX document.

**Flow:**

1. User input / topic initialization
2. Orchestrator delegates tasks to section agents
3. Agents generate content using LLM and search services
4. Shared memory stores intermediate state
5. LaTeX agent compiles structured output
6. Final `.tex` paper is produced

---

## Agents

### Core
- **base_agent.py** – Shared agent utilities and interface
- **abstract_agent.py** – Generates paper abstract
- **title_agent.py** – Produces title options
- **intro_agent.py** – Introduction section
- **literature_agent.py** – Related work / literature review
- **methodology_agent.py** – Methods and approach
- **results_agent.py** – Results and findings
- **discussion_agent.py** – Interpretation and implications
- **conclusion_agent.py** – Final summary and future work
- **references_agent.py** – Reference list generation
- **citation_agent.py** – Citation extraction and formatting
- **citation_placing_agent.py** – Inserts citations into sections
- **latex_agent.py** – Converts content into LaTeX structure
- **orchestrator.py** – Coordinates execution order and data flow

---

## Services

- **llm_service.py** – Interface for language model calls
- **search_service.py** – External search/query abstraction

---

## Memory

- **shared_state.py** – Centralized in-memory store for:
  - Section drafts
  - Citations
  - Metadata
  - Execution context

---

## Configuration
- **.env**  
```python
GOOGLE_API_KEY=AIzaSxxxxxx
MODEL_NAME=gemini-2.5-flash
```
---

## Installation

```bash
git clone https://github.com/swaraj-khan/PeerReviewWho
cd Research-Agent
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux: source venv/bin/activate
# MacOS: source venv/bin/activate
pip install -r requirements.txt
```

## Run

```python
python main.py
```
## Output

<img width="1862" height="787" alt="image" src="https://github.com/user-attachments/assets/82e78994-2cab-4448-9e39-6dec7f484f29" />

- Generates a structured research paper.
- Produces a LaTeX file (`research_paper.tex`) ready for compilation.
- Copy and paste the latex text into https://www.overleaf.com/ to get the pdf. In there you can do whatever the edits you have in mind !

See ya
