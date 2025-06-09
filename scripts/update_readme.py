# scripts/update_readme.py
import feedparser
import os
import re

# Fetches the latest blog post from the Android Developers Blog RSS feed.
def fetch_latest_android_blog():
    url = "https://android-developers.googleblog.com/atom.xml"
    feed = feedparser.parse(url)
    if not feed.entries:
        return "Could not fetch new posts at the moment."

    latest_post = feed.entries[0]
    post_title = latest_post.title
    post_link = latest_post.link

    # Create the markdown link for the README.
    return f"#### 📖 [{post_title}]({post_link})"

# Replaces the content between the start and end markers in the README.
def update_readme(content_to_insert):
    readme_path = "README.md"
    start_marker = "<!--START_SECTION:learn-->"
    end_marker = "<!--END_SECTION:learn-->"

    with open(readme_path, "r", encoding="utf-8") as f:
        readme_content = f.read()

    # Use regex to find and replace the content.
    pattern = f"{re.escape(start_marker)}(.*?)({re.escape(end_marker)})"

    new_readme = re.sub(
        pattern,
        f"{start_marker}\n{content_to_insert}\n{end_marker}",
        readme_content,
        flags=re.DOTALL
    )

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_readme)

if __name__ == "__main__":
    latest_post_md = fetch_latest_android_blog()
    update_readme(latest_post_md)
    print(f"✅ README updated with: {latest_post_md}")