QR Code Manager
A Python-based utility designed to generate, manage, and track QR codes locally. This tool automates the process of creating QR images while maintaining a structured Excel database for all generated links.

Features
QR Generation: Converts any URL into a PNG image.
Database Tracking: Automatically logs the ID, Name, URL, and timestamp into an Excel file.
Record Management: Built-in functions to list all active records or delete specific entries (removes both the database record and the associated image file).
Local Storage: Operates entirely offline with no external API dependencies.
Requirements
The following libraries are required for the script to function:
qrcode
pandas
openpyxl
Install them using pip:

Bash
pip install qrcode[pil] pandas openpyxl
How to Use
Run the script:
Bash
python main.py
Use the interactive menu to:
Generate: Provide a URL and a label for the file.
List: View all saved entries in the terminal.
Delete: Remove a specific record and its PNG file by name.
File Structure
main.py: The core script and logic.
qr_database.xlsx: The auto-generated database file.
[Name].png: Generated QR code images saved in the root directory.
Technical Notes
The script uses the QRManager class to handle file I/O operations. Ensure the execution directory has write permissions to allow for the creation of the Excel database and image exports.