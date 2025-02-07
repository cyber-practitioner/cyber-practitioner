import requests
from datetime import datetime

# Fetch recent activity (example: GitHub API)
def fetch_recent_activity(username):
    url = f"https://api.github.com/users/{username}/events/public"
    response = requests.get(url)
    if response.status_code == 200:
        events = response.json()
        activity = []
        for event in events[:5]:  # Get the last 5 events
            activity.append(f"- {event['type']} at {event['repo']['name']} on {event['created_at']}")
        return "\n".join(activity)
    return "No recent activity found."

# Update README
def update_readme():
    username = "cyber-practitioner"  # Replace with your GitHub username
    recent_activity = fetch_recent_activity(username)

    with open("README.md", "r") as file:
        content = file.read()

    # Replace the activity section
    start_marker = "<!-- ACTIVITY_START:striped -->"
    end_marker = "<!-- ACTIVITY_END -->"
    new_content = f"{start_marker}\n{recent_activity}\n{end_marker}"

    updated_content = content.split(start_marker)[0] + new_content + content.split(end_marker)[1]

    with open("README.md", "w") as file:
        file.write(updated_content)

if __name__ == "__main__":
    update_readme()