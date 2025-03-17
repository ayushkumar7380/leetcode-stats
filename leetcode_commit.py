import os
import requests
from bs4 import BeautifulSoup
import time

# Your LeetCode username
LEETCODE_USERNAME = "your_leetcode_username"

# GitHub repository details
GITHUB_REPO_PATH = "/path/to/your/local/leetcode-solutions"
GIT_COMMIT_MESSAGE = "Updated LeetCode solutions"

# LeetCode submission URL
LEETCODE_URL = f"https://leetcode.com/{LEETCODE_USERNAME}/submissions/"

def fetch_latest_submission():
    """Fetch the latest accepted LeetCode submission"""
    response = requests.get(LEETCODE_URL)
    if response.status_code != 200:
        print("Error fetching LeetCode data")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    latest_submission = soup.find("div", class_="status-wrapper")  # Locate latest problem
    if latest_submission:
        return latest_submission.text.strip()
    return None

def save_to_github():
    """Save the latest submission to GitHub"""
    os.system(f"cd {GITHUB_REPO_PATH} && git pull origin main")  # Sync with GitHub
    submission = fetch_latest_submission()
    if submission:
        with open(f"{GITHUB_REPO_PATH}/latest_submission.txt", "w") as f:
            f.write(submission)

        os.system(f"cd {GITHUB_REPO_PATH} && git add .")
        os.system(f'cd {GITHUB_REPO_PATH} && git commit -m "{GIT_COMMIT_MESSAGE}"')
        os.system(f"cd {GITHUB_REPO_PATH} && git push origin main")
        print("✅ LeetCode submission updated on GitHub!")
    else:
        print("❌ No new submissions found.")

if __name__ == "__main__":
    save_to_github()
