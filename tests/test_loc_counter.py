import tempfile
import os
from pathlib import Path
from tools.repo_introspect.loc_counter import count_loc_by_ext

def test_count_loc_by_ext(tmp_path):
    # Create test files
    py_file = tmp_path / "test.py"
    py_file.write_text("# This is a Python file\nprint('Hello')\n")
    
    md_file = tmp_path / "test.md"
    md_file.write_text("# This is a Markdown file\nThis is a line\nAnother line\n")
    
    # Run the function
    result = count_loc_by_ext(tmp_path)
    
    # Check results
    assert '.py' in result
    assert '.md' in result
    assert result['.py'] == 2  # 2 lines in Python file
    assert result['.md'] == 3  # 3 lines in Markdown file
    
    # Test with nested directories
    nested_dir = tmp_path / "nested"
    nested_dir.mkdir()
    nested_py = nested_dir / "nested.py"
    nested_py.write_text("# Nested Python file\nprint('Nested')\n")
    
    result_nested = count_loc_by_ext(tmp_path)
    assert result_nested['.py'] == 4  # 2 + 2 lines
    
    # Test with files in skip directories
    git_dir = tmp_path / ".git"
    git_dir.mkdir()
    git_file = git_dir / "file.txt"
    git_file.write_text("This should be ignored\n")
    
    result_skip = count_loc_by_ext(tmp_path)
    assert result_skip['.py'] == 4  # Should be same as before
    assert '.git' not in result_skip
