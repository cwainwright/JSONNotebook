from json import dump, load

from objects import Note, clear_screen, options_menu


def build_notebook(note: Note = None, data: list = None):
    # If no data is provided, load from file
    if note is None:
        with open("notebook.json", "r") as f:
            data = load(f)
        note = Note(data[0].get("title"))
        build_notebook(note, data[0].get("children", []))
        return note
    # Otherwise recursively build the notebook from data
    else:
        for child_d in data:
            child = Note(child_d.get("title", ""), child_d.get("content", ""), child_d.get("tags", []))
            note.add_child(child)
            build_notebook(child, child_d.get("children", []))

def save_notebook(note: Note):
    with open("notebook.json", "w") as f:
        dump([note.json], f, indent=4)
    return note

def create_notebook():
    template_notebook = Note("root")
    save_notebook(template_notebook)

def display_notebook(note: Note):
    # Clear screen
    clear_screen()
    print(f"\nNotebook: {note}")
    print(note.node_display())
    
def display_commands(note: Note):
    clear_screen()
    display_notebook(note)
    try:
        print(f"\nCommands (current note {note.path}): ")
    except AttributeError:
        return None
    else:
        options = {
            "Note Commands": note_commands,
            "Navigation Commands": navigate_commands,
            "Quit": "quit"
        }
        return options_menu(options, note)
    

def note_commands(note: Note):
    clear_screen()
    print(f"\nNote Commands (current note {note.path}): ")
    options = {
        "New": note.new_note,
        "Open": note.open_note,
        "Edit": note.edit_note,
        "Delete": note.delete_note,
        "Back": note
    }
    return options_menu(options)

def navigate_commands(note: Note):
    clear_screen()
    print(f"\nNavigation Commands (current note {note.path}): ")
    options = {
        "Up": note.parent,
        "Down": note.select_child,
        "Back": note
    }
    return options_menu(options)
