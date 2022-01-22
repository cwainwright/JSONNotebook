from logging import root
from formatters import node_display
from objects import Note
from toolset import options_menu
from json import load, dump

def build_notebook(note: Note = None, data: list = None):
    # If no data is provided, load from file
    if data is None:
        with open("notebook.json", "r") as f:
            data = load(f)
        note = Note("root")
        build_notebook(note, data[0].get("children"))
        return note

    # Otherwise recursively build the notebook from data
    else:
        for child_d in data:
            child = Note(child_d.get("title"), child_d.get("content"), child_d.get("tags"))
            note.add_child(child)
            build_notebook(child, child_d.get("children"))

def save_notebook(note: Note):
    with open("notebook.json", "w") as f:
        dump(note.json, f)
    return note

def display_notebook(note: Note):
    print(f"\nNotebook: ")
    print(note.node_display())
    
def display_commands(note: Note):
    try:
        print(f"\nCommands (current note {note.path}): ")
    except AttributeError:
        return None
    else:
        options = {
            "Note Commands": note_commands,
            "Navigate Commands": navigate_commands,
            "Quit": "quit"
        }
        return options_menu(options, note)
    

def note_commands(note: Note):
    print(f"\nCommands (current note {note.path}): ")
    options = {
        "New": note.new_note,
        "Open": note.open_note,
        "Show Tree": note.node_display,
        "Edit": note.edit_note,
        "Delete": note.delete_note,
        "Back": note
    }
    options_menu(options)
    return note

def navigate_commands(note: Note):
    print(f"\nNavigation commands (current note {note.path}): ")
    options = {
        "Up": note.parent,
        "Down": note.select_child,
        "Back": note
    }
    return options_menu(options)