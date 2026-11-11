# SHA256-File-Integrity-Checker

## Overview
A Python-based file integrity checker that calculates and compares SHA-256 hashes of two files to determine whether their contents match. This project was created to practice Python scripting, cryptographic hashing, and basic file integrity verification.

## Technologies Used
- Python 3
- Visual Studio Code
- hashlib (Python standard library)

## Features
- Calculates SHA-256 hashes for two files.
- Uses functions to generate and compare hash values.
- Identifies whether file contents match or differ.
- Displays the calculated hashes and comparison results.

## Example of input
- Two text files:
- text.txt
- text_copy.txt
  
## Example Output
Original value: [SHA-256 hash]<br>
New value: [SHA-256 hash]<br>
Match: file unchanged<br><br>

If the hashes differ:<br>

Mismatch: file changed<br>

## How to Run
1. Install Python 3.
2. Clone or download this repository.
3. Ensure files are in the same directory as the Python script.
4. Run the script:

## Future Improvements
- Save original file hashes as a baseline for future integrity checks.
- Monitor multiple files for changes.
- Detect modified, added, or deleted files.
- Generate file integrity reports.
- 
## Skills Demonstrated
- Python scripting and functions
- Cryptographic hashing (SHA-256)
- File handling
- Conditional statements
