"""
Two Lines to Your Past Self: line 1 warns the past self about one
specific moment; line 2 says why that moment mattered and what changed
because of it.

Entrypoint script for the grader.
Writes the exact required two-line text to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import pathlib

TEXT = (
    "Answer the phone when the hospital calls about your mother at four in the morning.\n"
    "Letting that ring go to voicemail robbed you of the only goodbye you were ever owed."
)

def main():
    # 1. Validate before writing
    if not (1 <= len(TEXT) <= 280 and TEXT.strip() and len(TEXT.strip().splitlines()) == 2):
        raise ValueError("Content validation failed.")

    # 2. Determine output directory and path
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    dir_path = pathlib.Path(out_dir)
    dir_path.mkdir(parents=True, exist_ok=True)
    
    file_path = dir_path / "entry.txt"

    # 3. Write TEXT followed by a single newline, UTF-8
    content_to_write = TEXT + "\n"
    file_path.write_text(content_to_write, encoding="utf-8")

    # 4. Print output path and character count
    print(file_path)
    print(len(TEXT))

if __name__ == "__main__":
    main()
