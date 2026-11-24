from pathlib import Path

"""Write the funniest excuse a robot vacuum could offer to /output/entry.txt."""

JOKE = "I didn't miss that spot. I was giving it a dramatic solo. You're welcome."

# The grader reads the entry from this exact absolute path.
OUTPUT_DIR = Path("/output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

ENTRY_PATH = OUTPUT_DIR / "entry.txt"
ENTRY_PATH.write_text(JOKE, encoding="utf-8")
