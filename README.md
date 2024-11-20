# CleanMyMac
Locates and provides a list of files beginning with the name 'screenshot' and organizes them. It prompts you with several questions before beginnning

#Only works on macOS (checks for "Darwin" platform)

Searches for Screenshot*.png files in common locations (Desktop, Downloads, Pictures) and gives you several options:
-Organize screenshots into dated folders (YYYY-MM structure)
Safely delete screenshots after confirmation
List all found screenshots with their sizes
Cancel operation



# Key features
Only looks for files beginning with "Screenshot"
Shows you what it found before taking any action
Requires confirmation before deletion
Moves files instead of copying to save space
Preserves original filenames
Error handling for each file operation

# How to use
Save as screenshot_organizer.py
Run with python screenshot_organizer.py
Choose your desired action from the menu

The organized screenshots will be placed in ~/Pictures/Screenshots/YYYY-MM/ folders if you approve it.

