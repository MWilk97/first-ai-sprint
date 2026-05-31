import argparse
import os
from datetime import datetime
from .loc_counter import count_lines_by_extension, format_loc_report
from .git_stats import get_git_commits, format_git_stats_report, get_run_timestamp

def main():
    parser = argparse.ArgumentParser(description='Repo introspection tool')
    parser.add_argument('--since', help='Only count commits since this date (YYYY-MM-DD)')
    
    args = parser.parse_args()
    
    # Get current working directory
    current_dir = os.getcwd()
    
    # Count lines by extension
    extension_counts = count_lines_by_extension(current_dir)
    
    # Get git stats
    author_counts = get_git_commits(args.since)
    
    # Format reports
    loc_report = format_loc_report(extension_counts)
    git_report = format_git_stats_report(author_counts)
    
    # Print the full report
    print("# Repository Introspection Report")
    print()
    print(loc_report)
    print()
    print(git_report)
    print()
    print(f"_Report generated on: {get_run_timestamp()}_")

if __name__ == '__main__':
    main()