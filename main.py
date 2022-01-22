from os import name, system

from commands import (
    build_notebook,
    display_commands,
    display_notebook,
    save_notebook
)


def main():
    """"Main Process"""
    system('cls' if name == 'nt' else 'clear')
    root = build_notebook()
    current_note = None
    
    while current_note != "quit":
        if current_note is None:
            current_note = root
        display_notebook(root)
        current_note = display_commands(current_note)
        save_notebook(root)
        
if __name__ == "__main__":
    main()
