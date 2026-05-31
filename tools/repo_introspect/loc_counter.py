import os
from collections import defaultdict

def count_lines_by_extension(directory):
    """Count lines of code by file extension in the given directory."""
    extension_counts = defaultdict(int)
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext:
                # Count lines in the file
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        extension_counts[ext] += len(lines)
                except (UnicodeDecodeError, PermissionError):
                    # Skip files that can't be read
                    continue
    
    return dict(extension_counts)


def format_loc_report(extension_counts):
    """Format the LOC counts into a Markdown table."""
    if not extension_counts:
        return ""
    
    # Create header
    report = "## LOC by extension\n\n| Extension | Lines |\n|-----------|-------|\n"
    
    # Add rows
    for ext, lines in sorted(extension_counts.items()):
        report += f"| {ext} | {lines} |\n"
    
    return report