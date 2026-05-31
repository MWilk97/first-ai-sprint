from pathlib import Path
import subprocess
from typing import Dict, Optional

def commits_per_author(repo_root: Path, since: Optional[str] = None) -> Dict[str, int]:
    """
    Count commits per author in a git repository.

    Args:
        repo_root: Path to the git repository root
        since: Optional date string to filter commits (e.g., '2023-01-01')

    Returns:
        Dictionary mapping author emails to commit counts
    """
    # Build the git log command
    cmd = ["git", "log", "--pretty=format:%ae"]
    if since:
        cmd.extend(["--since", since])
    
    # Run the command
    try:
        result = subprocess.run(
            cmd,
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=True
        )
        
        # Count commits per author
        commit_counts = {}
        for line in result.stdout.strip().split('\n'):
            if line:
                commit_counts[line] = commit_counts.get(line, 0) + 1
        
        return commit_counts
    except subprocess.CalledProcessError:
        # Return empty dict if git command fails
        return {}
