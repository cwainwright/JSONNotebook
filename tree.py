class Node:
    def __init__(self, data):
        self.data = data
        self.children = {}
        self.parent = None
    
    @property
    def childless(self) -> bool:
        return not bool(len(self.children))
    
    @property
    def path(self) -> str:
        if self.parent is None:
            return self.data
        else:
            return self.parent.path + "/" + self.data

    @property
    def json(self) -> dict:
        data = {"title": self.data, "content": self.content, "tags": self.tags}
        if not self.childless:
            data.update({"children": []})
            for child in self.children.values():
                data.get("children").append(child.json)
        return data
        
    def __str__(self) -> str:
        return str(self.data)
    
    def __repr__(self) -> str:
        return str(self.path)
    
    def set_parent(self, parent) -> bool:
        self.parent = parent
        return True
    
    def add_child(self, child) -> bool:
        if child in self.children:
            return False
        child.set_parent(self)
        self.children.update({child.data: child})
        return True
        
    def get_child(self, child):
        return self.children.get(child, None)
        
    def remove_child(self, child):
        try:
            self.children.pop(child.data)
        except KeyError:
            return False
        else:
            return True
        
    def node_display(self, indent = 0) -> str:
        if not indent:
            display_string = str(self)
        else:
            display_string = "\n" + indent * " " + "\u2514" + str(self)
        for child in self.children.values():
            display_string += child.node_display(indent + 1)

        return display_string