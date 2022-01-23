from pathlib import Path

from commands import (
    build_notebook,
    create_notebook,
    display_commands,
    display_notebook,
    save_notebook,
    create_notebook
)


def main():
    """"Main Process"""
    # If notebook does not exist, create it
    if not Path.exists(Path(__file__).parent / "notebook.json"):
        print("Notebook does not exist, creating new from template")
        create_notebook()
    # Rebuilding notebook
    root = build_notebook()
    current_note = None
    
    # Application Loop
    while current_note != "quit":
        # When currrent note is reset, reset to root
        if current_note is None:
            current_note = root
        # Displaying tree structure
        display_notebook(root)
        # Displaying commands
        current_note = display_commands(current_note)
        # Save changes to notebook
        save_notebook(root)
        
if __name__ == "__main__":
    main()
