import platform
import sys
from pathlib import Path
from shutil import rmtree, move
from datetime import datetime

if (system := platform.system()) != "Darwin":  # Darwin is macOS
    raise SystemExit(f"{system} is not supported - this tool is for macOS only")

def find_screenshots():
    """Find screenshot files in common macOS screenshot locations"""
    # Default macOS screenshot locations
    locations = [
        Path.home() / "Desktop",
        Path.home() / "Downloads",
        Path.home() / "Pictures"
    ]
    
    screenshot_files = []
    for location in locations:
        if location.exists():
            screenshot_files.extend([
                f for f in location.glob("Screenshot*.png")  # macOS default format
            ])
    
    return screenshot_files

def human_size(size: int) -> str:
    """Convert bytes to human readable format"""
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024:
            break
        size /= 1024
    return f"{size:.2f} {unit}"

def get_size_ext(files: list[Path]) -> tuple[int, set[str]]:
    """Calculate total size and get unique extensions"""
    return (
        sum(f.stat().st_size for f in files),
        {f.suffix for f in files}
    )

def organize_screenshots(files: list[Path]):
    """Organize screenshots into dated folders"""
    if not files:
        print("No screenshot files found")
        return

    # Calculate total size and show summary
    size, extensions = get_size_ext(files)
    
    print(f"\nFound {len(files)} screenshots")
    print(f"Total size: {human_size(size)}")
    print(f"File types: {', '.join(sorted(extensions))}")
    
    # Group by creation date
    screenshots_dir = Path.home() / "Pictures" / "Screenshots"
    
    action = input("\nChoose action:\n"
                  "1. Move to organized folders by date\n"
                  "2. Delete all found screenshots\n"
                  "3. List all screenshots\n"
                  "4. Cancel\n"
                  "Enter choice (1-4): ")
    
    if action == "1":
        screenshots_dir.mkdir(parents=True, exist_ok=True)
        
        for file in files:
            # Get creation time and format into folder name
            ctime = datetime.fromtimestamp(file.stat().st_ctime)
            month_dir = screenshots_dir / ctime.strftime("%Y-%m")
            month_dir.mkdir(exist_ok=True)
            
            # Move file to new location
            try:
                move(file, month_dir / file.name)
                print(f"Moved: {file.name} → {month_dir}")
            except Exception as e:
                print(f"Error moving {file.name}: {e}")
    
    elif action == "2":
        confirm = input(f"\nAre you sure you want to delete {len(files)} screenshots? (yes/no): ")
        if confirm.lower() == "yes":
            for file in files:
                try:
                    file.unlink()
                    print(f"Deleted: {file.name}")
                except Exception as e:
                    print(f"Error deleting {file.name}: {e}")
        else:
            print("Operation cancelled")
    
    elif action == "3":
        print("\nFound screenshots:")
        for file in files:
            print(f"{file.name} ({human_size(file.stat().st_size)})")
    
    else:
        print("Operation cancelled")

def main():
    try:
        organize_screenshots(find_screenshots())
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
