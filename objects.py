from tree import Node
from toolset import options_menu

deletable_paths = []

class Note(Node):
    def __init__(self, title, content = None, tags = None):
        super().__init__(title)
        self.content = content
        if content is None: self.content = ""
        self.tags = tags
        if tags is None: self.tags = []
        
    def new_note(self):
        title = input("Enter a title for the new note: ")
        while title in self.children:
            print("Title already in use.")
            title = input("Enter a title for the new note: ")
        content = input("Enter the content for the new note: ")
        if content == "": content = None
        tags = input("Enter the tags for the new note (separated by commas): ")
        tags = tags.split(",")
        map(lambda x: x.strip(" ").replace(" ", "-"), tags)
        self.add_child(Note(title, content, tags))
    
    def select_child(self):
        if self.childless:
            print(f"{self.data} has no children to select")
            return self
        print(f"\nSelect child from {self.data}: ")
        return options_menu(self.children)
    
    def open_note(self):
        print(f"Title: {self.data}")
        print(f"Content:\n{self.content}")
        print(f"Tags: {self.tags}")
        return self
     
    def edit_note(self):
        print(f"Edit Note: ({self.data})")
        options = {
            "title": self.change_title,
            "content": self.change_content,
            "tags": self.change_tags
        }
        options_menu(options)
        return self
        
    def change_title(self):
        self.data = input(f"Old:{self.data}\nNew: ")
        return self
        
    def change_content(self):
        self.content = input(f"Old:\n{self.content}\nNew: ")
        return self
        
    def change_tags(self):
        tags = input(f"Old:\n{self.tags}\nNew: ")
        tags = tags.split(",")
        map(lambda x: x.strip(" ").replace(" ", "-"), tags)
        self.tags = tags
        return self
        
    def delete_note(self):
        self.parent.remove_child(self)
        return self

if __name__ == "__main__":
    root = Note("root", "root content", ["root", "tag"])
    root.add_child(Note("child 1", "child 1 content", ["child", "tag"]))
    root.add_child(Note("child 2", "child 2 content", ["child", "tag"]))
    root.get_child("child 1").add_child(Note("grandchild 1", "grandchild 1 content", ["grandchild", "tag"]))
    root.get_child("child 1").get_child("grandchild 1").add_child(Note("great grandchild 1", "great grandchild 1 content", ["great grandchild", "tag"]))
    # display_notebook(root)
    root.get_child("child 1").get_child("grandchild 1").get_child("great grandchild 1").delete_note()
    root.get_child("child 2").delete_note()
    print(deletable_paths)
    print(root.node_display())