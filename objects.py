from inspect import Attribute
from toolset import options_menu, Node, clear_screen

class Note(Node):
    """Note, inherits from Node"""
    def __init__(self, title, content = None, tags = None):
        """Initialize a new note"""
        super().__init__(title)
        self.content = content
        if content is None: self.content = ""
        self.tags = tags
        if tags is None: self.tags = []
        
    def new_note(self):
        """Create a new child note"""
        title = input("Enter a title for the new note: ")
        while title in self.children:
            print("Title already in use.")
            title = input("Enter a title for the new note: ")
        content = input("Enter the content for the new note: ")
        if content == "": content = None
        tags = input("Enter the tags for the new note (separated by commas): ")
        tags = tags.split(",")
        map(lambda x: x.strip(" ").replace(" ", "-"), tags)
        child = Note(title, content, tags)
        self.add_child(child)
        return child
    
    def select_child(self):
        """Select a child note"""
        clear_screen()
        if self.childless:
            print(f"{self.data} has no children to select")
            return self
        print(f"\nSelect child from {self.data}: ")
        return options_menu(self.children)
    
    def open_note(self):
        """Display contents of note"""
        clear_screen()
        print(f"\nTitle: {self.data}")
        print(f"Content:\n{self.content}")
        print(f"Tags: {self.tags}")
        return self
     
    def edit_note(self):
        """Edit note contents"""
        clear_screen()
        print(f"Edit Note: ({self.data})")
        options = {
            "title": self.change_title,
            "content": self.change_content,
            "tags": self.change_tags
        }
        options_menu(options)
        return self
        
    def change_title(self):
        """Change the title of the note"""
        self.data = input(f"Old:{self.data}\nNew: ")
        return self
        
    def change_content(self):
        """Change the content of the note"""
        self.content = input(f"Old:\n{self.content}\nNew: ")
        return self
        
    def change_tags(self):
        """Change the tags of the note"""
        tags = input(f"Old:\n{self.tags}\nNew: ")
        tags = tags.split(",")
        map(lambda x: x.strip(" ").replace(" ", "-"), tags)
        self.tags = tags
        return self
        
    def delete_note(self):
        """"Delete the note (get the parent to delete the child)"""
        try:
            self.parent.remove_child(self)
            return self.parent
        except AttributeError:
            return self

if __name__ == "__main__":
    root = Note("root", "root content", ["root", "tag"])
    root.add_child(Note("child 1", "child 1 content", ["child", "tag"]))
    child = Note("child 2", "child 2 content", ["child", "tag"])
    child.add_child(Note("grandchild 1", "grandchild 1 content", ["grandchild", "tag"]))
    child.add_child(Note("grandchild 2", "grandchild 2 content", ["grandchild", "tag"]))
    root.add_child(
        child
    )
    print(root.node_display())