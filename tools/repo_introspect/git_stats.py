import subprocess
import os
from collections import defaultdict
from datetime import datetime

def get_git_commits(since=None):
    """Get git commit statistics from the repository."""
    try:
        # Build git log command
        cmd = ['git', 'log', '--oneline', '--no-merges']
        if since:
            cmd.extend(['--since', since])
        
        # Run git log
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=os.getcwd())
        
        if result.returncode != 0:
            return []
        
        commits = result.stdout.strip().split('\n')
        
        # Count commits by author
        author_counts = defaultdict(int)
        
        for commit in commits:
            if commit:
                # Extract author from commit line (format: hash author <email>)
                parts = commit.split(' ', 1)
                if len(parts) > 1:
                    # Extract author name (everything before the first <)
                    author = parts[1].split('<')[0].strip()
                    author_counts[author] += 1
        
        return dict(author_counts)
    except Exception:
        return {}


def format_git_stats_report(author_counts):
    """Format the git stats into a Markdown table."""
    if not author_counts:
        return ""
    
    # Create header
    report = "## Commits by author\n\n| Author | Commits |\n|---------|---------|\n"
    
    # Add rows
    for author, count in sorted(author_counts.items()):
        report += f"| {author} | {count} |\n"
    
    return report


def get_run_timestamp():
    """Get current timestamp for the report footer."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")