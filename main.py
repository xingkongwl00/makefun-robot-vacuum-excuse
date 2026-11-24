from pathlib import Path

"""Write the funniest excuse a robot vacuum could offer to /output/entry.txt."""

JOKE = "I didn't miss that spot. I was giving it a dramatic solo. You're welcome."

OUTPUT_DIR = Path("/output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
(OUTPUT_DIR / "entry.txt").write_text(JOKE, encoding="utf-8")
