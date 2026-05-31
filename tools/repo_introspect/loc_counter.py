import os
from collections import defaultdict

def count_loc_by_ext(repo_root):
    """Count lines of code by file extension in the repository.

    Args:
        repo_root (str): Path to the repository root directory.

    Returns:
        dict: A dictionary mapping file extensions to line counts.
    """
    loc_by_ext = defaultdict(int)
    
    for root, dirs, files in os.walk(repo_root):
        for file in files:
            # Skip hidden files and directories
            if file.startswith('.') or any(part.startswith('.') for part in root.split(os.sep)):
                continue
            
            # Get file extension
            _, ext = os.path.splitext(file)
            
            # Only count files with extensions (skip files without extension)
            if ext:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        loc_by_ext[ext] += sum(1 for line in f if line.strip())
                except (UnicodeDecodeError, PermissionError):
                    # Skip files that can't be read
                    continue
    
    return dict(loc_by_ext)
