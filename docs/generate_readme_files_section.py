#!/usr/bin/env python3
"""
Execute from project root directory
python docs/generate_readme.py

Update only the '## Files' section in README.md with file lists from subdirectories.
Preserves all other content in the README.
"""

import sys
from pathlib import Path
from fnmatch import fnmatch
from urllib.parse import quote

# Directories to exclude from the Files section
EXCLUDED_PATHS = [
    '.*',              # Excludes all hidden folders (.git, .github, .DS_Store, etc.)
    '__pycache__',
    '__init__.py',
    'img',
    # Add your own paths here
]


def is_excluded(path_name):
    """Check if path matches any exclusion pattern"""
    for pattern in EXCLUDED_PATHS:
        if fnmatch(path_name, pattern):
            return True
    return False

def scan_directory_recursive(directory, root_dir, level=0):
    """Recursively scan directory and return formatted file listings"""
    content = []
    
    # Get all items in current directory, sorted
    items = sorted(directory.iterdir(), key=lambda x: (not x.is_dir(), x.name))
    
    # Separate directories and files
    subdirs = [d for d in items if d.is_dir() and not is_excluded(d.name)]
    files = [f for f in items if f.is_file() and not is_excluded(f.name)]
    
    # Add files from current directory
    if files:
        # Calculate relative path from root
        rel_path = directory.relative_to(root_dir)
        section_title = str(rel_path) if str(rel_path) != '.' else 'Root'
        
        # Adjust heading level based on depth
        heading = '#' * (3 + level) + f" {section_title}\n\n"
        content.append(heading)
        
        for file in files:
            # URL-encode the full relative path
            file_rel_path = file.relative_to(root_dir)
            encoded_path = '/'.join(quote(part) for part in file_rel_path.parts)
            content.append(f"- [{file.name}]({encoded_path})\n")
        
        content.append("\n")
    
    # Recursively process subdirectories
    for subdir in subdirs:
        content.extend(scan_directory_recursive(subdir, root_dir, level + 1))
    
    return content

def scan_files():
    """Scan subdirectories recursively and return formatted file listings"""
    root_dir = Path.cwd()
    content = []
    
    # Get all top-level subdirectories, sorted alphabetically
    subdirs = sorted([
        d for d in root_dir.iterdir() 
        if d.is_dir() and not is_excluded(d.name)
    ])
    
    for subdir in subdirs:
        # Recursively scan each top-level directory
        content.extend(scan_directory_recursive(subdir, root_dir, level=0))
    
    return content

def update_readme():
    """Update only the ## Files section in README.md"""
    readme_path = Path.cwd() / "README.md"
    
    # Check if README.md exists
    if not readme_path.exists():
        print("❌ ERROR: README.md not found!")
        sys.exit(1)
    
    # Read existing README
    with open(readme_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # Find where ## Files section starts and ends
    files_section_start = None
    files_section_end = None
    
    for i, line in enumerate(lines):
        if line.strip() == "## Files":
            files_section_start = i
        # Found next ## heading = end of Files section
        elif files_section_start is not None and line.startswith("## ") and i > files_section_start:
            files_section_end = i
            break
    
    # Error if ## Files section doesn't exist
    if files_section_start is None:
        print("❌ ERROR: '## Files' section not found in README.md!")
        print("   Please add a '## Files' section to your README.md first.")
        sys.exit(1)
    
    # If no end found, section goes to end of file
    if files_section_end is None:
        files_section_end = len(lines)
    
    # Generate new file listings
    new_files_content = scan_files()
    
    # Rebuild README: keep before + new content + keep after
    new_readme = (
        lines[:files_section_start + 1] +  # Before + "## Files" line
        ["\n"] +
        new_files_content +  # New generated content
        lines[files_section_end:]  # After Files section
    )
    
    # Write updated README
    with open(readme_path, "w", encoding="utf-8") as f:
        f.writelines(new_readme)
    
    print("✅ README.md updated successfully!")
    print(f"  Updated '## Files' section (recursive)")
    if EXCLUDED_PATHS:
        print(f"  Excluded patterns: {', '.join(EXCLUDED_PATHS)}")

if __name__ == "__main__":
    update_readme()

