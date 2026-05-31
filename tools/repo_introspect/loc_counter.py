import os

def count_loc_by_ext(repo_root):
    """Count lines of code by file extension in a given repository root.

    Args:
        repo_root (str): The root directory of the repository.

    Returns:
        dict: A dictionary with file extensions as keys and line counts as values.
    """
    # Initialize a dictionary to store the counts
    counts = {}
    
    # Walk through all files in the repository
    for root, dirs, files in os.walk(repo_root):
        # Skip __pycache__ directories
        dirs[:] = [d for d in dirs if d != '__pycache__']
        
        for file in files:
            # Get the file extension
            _, ext = os.path.splitext(file)
            
            # Skip files without extensions
            if not ext:
                continue
            
            # Get the full file path
            file_path = os.path.join(root, file)
            
            # Count lines in the file
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    line_count = sum(1 for line in f)
            except (UnicodeDecodeError, PermissionError):
                # Skip files that can't be read
                continue
            
            # Add to the counts dictionary
            if ext in counts:
                counts[ext] += line_count
            else:
                counts[ext] = line_count
    
    return counts
