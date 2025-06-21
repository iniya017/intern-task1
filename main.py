from utils import scrape_chapter
from agents import ai_writer, ai_reviewer
from versioning import save_version, search_version


url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
scrape_chapter(url)


with open("data/chapter1.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

prompt = f"Rewrite this chapter in poetic and simple English:\n\n{raw_text}"
ai_written = ai_writer(prompt)


ai_reviewed = ai_reviewer(ai_written)


edit = input("Do you want to edit the result manually? (yes/no): ")
if edit.lower() == "yes":
    print("Paste your edited text (or skip to save AI output):")
    human_text = input()
    final_version = human_text if human_text.strip() else ai_reviewed
else:
    final_version = ai_reviewed

save_version(final_version)


if input("🔎 Do you want to search saved versions? (yes/no): ").lower() == "yes":
    user_query = input("Enter your search query: ")
    search_version(user_query)
