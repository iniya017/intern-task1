import streamlit as st
from utils import scrape_chapter
from agents import ai_writer, ai_reviewer
from versioning import save_version, search_version

st.set_page_config(page_title="📚 AI Book Workflow", layout="wide")

st.title("📖 Automated Book Publication Workflow")
st.markdown("Spin, Review, Edit and Version Book Chapters with AI + Human Loop")

# URL input
url = st.text_input("📎 Enter Chapter URL", 
                    "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1")

if st.button("🧲 Scrape Chapter"):
    scrape_chapter(url)
    st.success("✅ Chapter scraped and screenshot saved as 'data/chapter1.png'")

# Load scraped text
try:
    with open("data/chapter1.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()
except:
    raw_text = ""

if raw_text:
    st.subheader("📜 Original Chapter Text")
    st.text_area("Original Text", raw_text, height=250)

    if st.button("✍️ AI Rewrite"):
        prompt = f"Rewrite this chapter in poetic and simple English:\n\n{raw_text}"
        rewritten = ai_writer(prompt)
        st.session_state["ai_written"] = rewritten
        st.success("AI Writer finished!")

if "ai_written" in st.session_state:
    st.subheader("🧠 AI Reviewed Output")
    reviewed = ai_reviewer(st.session_state["ai_written"])
    st.session_state["ai_reviewed"] = reviewed
    edited_text = st.text_area("✏️ You can manually edit the final text here:", reviewed, height=300)

    if st.button("💾 Save Final Version"):
        save_version(edited_text)
        st.success("✅ Version saved!")

st.divider()

# Search
st.subheader("🔍 Search Saved Versions")
query = st.text_input("Search Query")
if st.button("Search"):
    st.info(f"Searching for: {query}")
    search_version(query)
