from pathlib import Path
from typing import Dict

def count_loc_by_ext(repo_root: Path) -> Dict[str, int]:
    """Walk the repo (skipping .git/, .venv/, infra/repos/, __pycache__) and return {ext: total_lines}."""
    result = {}
    
    # Define directories to skip
    skip_dirs = {'.git', '.venv', 'infra', '__pycache__'}
    
    for file_path in repo_root.rglob('*'):
        if file_path.is_file():
            # Check if any part of the path contains a skip directory
            path_parts = file_path.relative_to(repo_root).parts
            should_skip = False
            for part in path_parts:
                if part in skip_dirs:
                    should_skip = True
                    break
            
            if should_skip:
                continue
            
            # Get file extension
            ext = file_path.suffix
            if not ext:
                ext = 'no_extension'
            
            # Count lines
            try:
                with file_path.open('r', encoding='utf-8') as f:
                    lines = sum(1 for _ in f)
                result[ext] = result.get(ext, 0) + lines
            except (UnicodeDecodeError, PermissionError):
                # Skip files that can't be read
                continue
    
    return result
