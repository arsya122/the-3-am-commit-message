"""Write the fixed commit message deterministically, without network access or randomness."""

import os
from pathlib import Path


message = "fix: 3am deploy deleted prod; I have now added a test that checks whether I am awake before I push"
output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "entry.txt"
output_file.write_text(message, encoding="utf-8")

# Ignore chmod failures because the grader runs as an unprivileged user on a read-only filesystem.
try:
    output_file.chmod(0o644)
except OSError:
    pass
