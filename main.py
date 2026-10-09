import argparse
import json
import re
from pathlib import Path

def create_video_package(topic: str) -> dict:
"""Create a basic YouTube planning package without external APIs."""

topic = topic.strip()
if not topic:
    raise ValueError("Topic cannot be empty.")

safe_topic = re.sub(r"\s+", " ", topic)

return {
    "topic": safe_topic,
    "title_ideas": [
        f"{safe_topic}: Complete Guide",
        f"5 Things to Know About {safe_topic}",
        f"{safe_topic} Explained Simply",
    ],
    "description_draft": (
        f"In this video, we explore {safe_topic}. "
        "Review all facts and add reliable sources before publishing."
    ),
    "script_draft": [
        {
            "section": "Hook",
            "text": (
                f"Want to learn about {safe_topic}? "
                "Let's explore the key points."
            ),
        },
        {
            "section": "Main Content",
            "text": (
                "Explain three useful points, verify factual claims, "
                "and add trustworthy sources."
            ),
        },
        {
            "section": "Conclusion",
            "text": (
                "Summarize the main lesson and invite viewers "
                "to share their thoughts."
            ),
        },
    ],
    "scene_plan": [
        {"scene": 1, "purpose": "Opening hook", "duration_seconds": 5},
        {"scene": 2, "purpose": "Main point one", "duration_seconds": 8},
        {"scene": 3, "purpose": "Main point two", "duration_seconds": 8},
        {"scene": 4, "purpose": "Conclusion", "duration_seconds": 9},
    ],
    "publishing_status": "NOT_PUBLISHED",
    "review_required": True,
}

def main():
parser = argparse.ArgumentParser(
description="Create a basic YouTube video planning package."
)
parser.add_argument("--topic", required=True, help="Your video topic")
parser.add_argument(
"--output",
default="output/video_package.json",
help="Path for the generated JSON file",
)
args = parser.parse_args()

package = create_video_package(args.topic)
output_path = Path(args.output)
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(
    json.dumps(package, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
)

print("Video planning package created.")
print(f"Output: {output_path}")
print("Publishing: disabled; human review required.")

if name == "main":
main()
