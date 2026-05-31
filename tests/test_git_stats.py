import os
import tempfile
import subprocess
import sys
import pathlib
from pathlib import Path

# Add the parent directory to the path to import the module
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

from tools.repo_introspect.git_stats import commits_per_author

def test_commits_per_author():
    # Create a temporary directory for our test repo
    with tempfile.TemporaryDirectory() as tmp_dir:
        repo_root = Path(tmp_dir)
        
        # Initialize git repo
        subprocess.run(["git", "init"], cwd=repo_root, check=True, capture_output=True)
        
        # Configure git user
        subprocess.run(["git", "config", "user.name", "Test User"], cwd=repo_root, check=True, capture_output=True)
        subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo_root, check=True, capture_output=True)
        
        # Create first file and commit
        test_file1 = repo_root / "test1.txt"
        test_file1.write_text("test content 1")
        subprocess.run(["git", "add", "test1.txt"], cwd=repo_root, check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", "First commit"], cwd=repo_root, check=True, capture_output=True)
        
        # Change user to second author
        subprocess.run(["git", "config", "user.email", "second@example.com"], cwd=repo_root, check=True, capture_output=True)
        
        # Create second file and commit
        test_file2 = repo_root / "test2.txt"
        test_file2.write_text("test content 2")
        subprocess.run(["git", "add", "test2.txt"], cwd=repo_root, check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", "Second commit"], cwd=repo_root, check=True, capture_output=True)
        
        # Test the function
        result = commits_per_author(repo_root)
        
        # Verify the results
        assert "test@example.com" in result
        assert "second@example.com" in result
        assert result["test@example.com"] == 1
        assert result["second@example.com"] == 1

def test_commits_per_author_since_filter():
    # Create a temporary directory for our test repo
    with tempfile.TemporaryDirectory() as tmp_dir:
        repo_root = Path(tmp_dir)
        
        # Initialize git repo
        subprocess.run(["git", "init"], cwd=repo_root, check=True, capture_output=True)
        
        # Configure git user
        subprocess.run(["git", "config", "user.name", "Test User"], cwd=repo_root, check=True, capture_output=True)
        subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo_root, check=True, capture_output=True)
        
        # Create first file and commit
        test_file1 = repo_root / "test1.txt"
        test_file1.write_text("test content 1")
        subprocess.run(["git", "add", "test1.txt"], cwd=repo_root, check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", "First commit"], cwd=repo_root, check=True, capture_output=True)
        
        # Create second file and commit
        test_file2 = repo_root / "test2.txt"
        test_file2.write_text("test content 2")
        subprocess.run(["git", "add", "test2.txt"], cwd=repo_root, check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", "Second commit"], cwd=repo_root, check=True, capture_output=True)
        
        # Test the function with since filter
        result = commits_per_author(repo_root, since="2023-01-01")
        
        # Verify the results
        assert "test@example.com" in result
        assert result["test@example.com"] == 2
