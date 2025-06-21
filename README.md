Automated Book Publication Workflow
This project is a complete system for transforming and managing literary content using a combination of web scraping, AI language models, and semantic version control. It is designed to showcase a real-world use case of AI-assisted writing, editing, and version tracking, all integrated into a user-friendly web interface.

Project Overview
The goal of this project is to build an automated yet editable workflow that simulates how content might be prepared for publication. It begins with scraping text from a public domain source, then refines it using AI tools, and allows for multiple iterations of human feedback before storing each version. These versions can later be retrieved based on meaning, thanks to semantic search powered by embeddings.

This project was built as part of a developer evaluation challenge and demonstrates real-world skills in AI integration, automation, and user interface development.

Key Features
Web Scraping: Extracts chapter content directly from a provided URL using Playwright.

AI Writer: Rewrites the scraped chapter in a simplified and poetic tone using a local LLM served via Ollama.

AI Reviewer: Further polishes the AI-generated content to enhance clarity and flow.

Human-in-the-Loop Editing: After the AI review, users can manually refine the content before saving.

Version Control: Each version is saved into ChromaDB with a unique identifier.

Semantic Search: Previous versions can be retrieved through search queries that match based on meaning rather than exact wording.

Streamlit Web Interface: Provides an easy-to-use UI for running the workflow, viewing/editing outputs, and searching saved content.

Project Structure
graphql
Copy
Edit
book_/
├── app.py                # Streamlit-based UI for full workflow
├── main.py               # Command-line version of the process
├── agents.py             # AI Writer and Reviewer logic using Ollama
├── utils.py              # Web scraping functions using Playwright
├── versioning.py         # ChromaDB integration for storing and retrieving versions
├── rl_search.py          # Semantic search logic based on embeddings
├── data/
│   ├── chapter1.txt      # Scraped content
│   ├── chapter1.png      # Screenshot of the source webpage
│   └── chromadb/         # Persistent ChromaDB vector storage
└── README.md             # Project documentation
Streamlit Interface
The project includes a fully interactive Streamlit app (app.py) that makes the workflow accessible to users without requiring them to run Python scripts manually.

Main capabilities in the web UI:

Input a chapter URL to scrape text and save a screenshot

Automatically rewrite the text using the AI Writer

Review and refine the rewritten text using the AI Reviewer

Edit the reviewed text manually in a rich text area

Save the final version to ChromaDB with semantic embeddings

Search previously saved versions using a natural language query

To run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Make sure Ollama is running in a separate terminal before using the AI Writer:

bash
Copy
Edit
ollama run llama3
Setup Instructions
Requirements
Python 3.8+

Ollama (local language model runner)

Playwright (for scraping)

ChromaDB (vector database)

Streamlit (for UI)

Installation
bash
Copy
Edit
# Clone the repository
git clone https://github.com/yourusername/ai-book-workflow.git
cd ai-book-workflow

# Install dependencies
pip install -r requirements.txt

# Set up Playwright (first-time only)
playwright install
Start Ollama in a separate terminal:

bash
Copy
Edit
ollama run llama3
Then launch the web app:

bash
Copy
Edit
streamlit run app.py
How It Works
The user enters a URL pointing to a book chapter.

The system fetches and stores both the text and a screenshot of the chapter.

The text is passed through an AI model (via Ollama) that rewrites it in a poetic, simplified tone.

The rewritten text is reviewed and improved further by another AI model.

The user has the opportunity to manually edit the final version.

Once confirmed, the content is saved in ChromaDB with vector embeddings.

Any past version can be retrieved later by querying the system using natural language.

