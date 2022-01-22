from os import name, system

from commands import Note, build_notebook, display_commands, display_notebook

def main():
    system('cls' if name == 'nt' else 'clear')
    root = build_notebook()
    current_note = None
    
    while current_note != "quit":
        if current_note is None:
            current_note = root
        display_notebook(root)
        current_note = display_commands(current_note)
        
if __name__ == "__main__":
    main()