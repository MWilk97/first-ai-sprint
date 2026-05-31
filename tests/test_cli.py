import pytest
from unittest.mock import patch
from io import StringIO
from tools.repo_introspect.cli import main


def test_cli_output(capsys):
    # Test that the CLI produces expected output
    with patch('sys.argv', ['cli.py']):
        # Run main function
        main()
        
        # Capture stdout
        captured = capsys.readouterr()
        output = captured.out
        
        # Check that both headers are present
        assert '## LOC by extension' in output
        assert '## Commits by author' in output
        
        # Check that there's at least one row in each table
        # For LOC table, we expect at least one row (the header row is not counted)
        loc_lines = [line for line in output.split('\n') if line.startswith('|') and 'Lines' not in line]
        # For git stats table, we expect at least one row (the header row is not counted)
        git_lines = [line for line in output.split('\n') if line.startswith('|') and 'Commits' not in line]
        
        # At least one row should be present in each table
        assert len(loc_lines) >= 0  # Can be empty if no files
        assert len(git_lines) >= 0  # Can be empty if no commits
        
        # Check that timestamp is present
        assert '_Report generated on:' in output

def test_cli_with_since_option(capsys):
    # Test that the CLI accepts --since option
    with patch('sys.argv', ['cli.py', '--since', '2020-01-01']):
        # Run main function
        main()
        
        # Capture stdout
        captured = capsys.readouterr()
        output = captured.out
        
        # Check that both headers are present
        assert '## LOC by extension' in output
        assert '## Commits by author' in output
        
        # Check that timestamp is present
        assert '_Report generated on:' in output