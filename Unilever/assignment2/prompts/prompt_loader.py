from pathlib import Path

def load_prompt(file_path: str) -> str:
    return Path(file_path).read_text()