# Multi Agent

High-level research-assistant project using LangChain-style agents and the Mistral LLM.

This repository demonstrates a two-agent pipeline (searcher + reader) plus writer/critic chains for turning web search results into a structured research report.

Contents
- `app.py` — model and chain/agent definitions (search agent, reader agent, writer & critic chains)
- `agents.py` — same agent/chain definitions (duplicate entrypoint for reuse)
- `tools.py` — tool implementations: `web_search` (Tavily) and `scrape_url` (requests + BeautifulSoup)
- `pipeline.py` — (optional) orchestration code (if present)
- `requirements.txt` — Python dependencies

Quick status
- Runtime: Python 3.11+ recommended
- Entry points: This repo provides agent and chain objects; there is no bundled HTTP server. You can import `agents` or `app` from your own script or a small FastAPI app and run it with `uvicorn`.

High-level architecture

Architecture summary
- Client (CLI / notebook / HTTP frontend) triggers a research job.
- Search Agent (uses `web_search` tool) finds relevant URLs and summaries via the Tavily API.
- Reader Agent (uses `scrape_url` tool) fetches and extracts text from selected URLs.
- Writer Chain composes the gathered research into a structured report via the Mistral LLM.
- Critic Chain evaluates the report and returns a score + improvement suggestions.

How to set up and run

Note: this project uses the directory name `uv` as the virtual environment folder in these examples (the project owner uses `uv` to mean "virtual env"). If you already use a different venv name (for example `.venv`), adapt the commands accordingly.

1) Ensure you're in the repo root:

```bash
cd ~/Downloads/Multi\ Agent
```

2) Create a virtual environment named `uv` and install dependencies:

```bash
python -m venv uv
# macOS zsh: activate the 'uv' virtual environment
source uv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

3) Add credentials (the repository uses `python-dotenv` to load keys). Create a `.env` file in the project root with the following variables:

```
OPENAI_API_KEY=...
MISTRAL_API_KEY=...
TAVILY_API_KEY=...
```

Note: A sample `.env` may already exist in the repo root. Keep secrets out of version control.

Streamlit UI

A Streamlit-based UI is included for a compact, single-file interface: `streamlit_app.py`.

- Purpose: Provide a simple form to submit a research topic and render the pipeline outputs:
  - Search Results -> `search_results`
  - Scraped Content -> `scraped_content`
  - Writer Report -> `report`
  - Critic Feedback -> `feedback`

How to run the Streamlit UI (local)

1) Activate the `uv` virtual environment and install dependencies:

```bash
source uv/bin/activate
pip install -r requirements.txt
```

2) Start the Streamlit app:

```bash
streamlit run streamlit_app.py
```