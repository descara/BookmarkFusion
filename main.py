#!/usr/bin/env python3

# TODO
# Check if safari, firefox and chrome exist on the computer
# If yes find and open the bookmarks databases

import argparse
import sys
import platform
import os

# Firefox profiles locations
FF_PROFILE_LOC = ""
MAC_PROFILE_LOC = "~/Library/Application Support/Firefox/Profiles/"

def fetch_bookmarks():
    # Check and return OS name
    os_name = platform.system()
    
    if os_name == 'Darwin':
        print("MacOS detected")
    elif os_name == 'Windows':
        print("Windows Detected")
    elif os_name == 'Linux':
        print("Linux detected")
    
    # For linux/mac expand user home director
    expanded_path = os.path.expanduser(MAC_PROFILE_LOC)

    if os.path.exists(expanded_path):
        print("Path exists")
    else:
        print("Path does not exist")

def main():
    # Create the parser
    parser = argparse.ArgumentParser(
        description="Keep your browser bookmarks in sync"
    )

    # Add arguments (example: --name and --verbose)
    parser.add_argument(
        '-s', '--sync',
        type=str,
        help='Synchronize bookmarks from all browsers',
        required=False  # Making this argument required
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose mode'
    )

    # Parse the arguments
    args = parser.parse_args()

    # Use the parsed arguments
    if args.verbose:
        print(f"Verbose mode enabled")

    print(f"Hello, {args.name}!")

if __name__ == '__main__':
    # Call the main function
    main()
    fetch_bookmarks()