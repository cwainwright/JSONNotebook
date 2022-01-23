from typing import Union
from os import system, name

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
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
        data = {"title": self.data, "content": self.content, "tags": self.tags, "children": []}
        for child in self.children:
            data.get("children").append(child.json)
        return data
        
    def __str__(self) -> str:
        return str(self.data)
    
    def __repr__(self) -> str:
        return str(self.path)
    
    def node_display(self, indent = 0) -> str:
        if not indent:
            display_string = str(self)
        else:
            display_string = "\n" + indent * " " + "\u2514" + str(self)
        for child in self.children:
            display_string += child.node_display(indent + 1)
        return display_string
    
    def set_parent(self, parent) -> bool:
        self.parent = parent
        return True
    
    def add_child(self, child) -> bool:
        if child in self.children:
            return False
        child.set_parent(self)
        self.children.append(child)
        return True
        
    def remove_child(self, child):
        try:
            self.children.remove(child)
        except KeyError:
            return False
        else:
            return True

def node_display(node, indent = 0) -> str:
    """Display node and its children"""
    if not indent:
        display_string = str(node)
    else:
        display_string = "\n" + indent * " " + "\u2514" + str(node)
    for child in node.children:
        display_string += node_display(child, indent + 1)

    return display_string

def options_menu(menu: Union[list, dict], arguments = None):
    option_list = []
    selection = None

    print("Please select one of the following options:")
    for number, item in enumerate(menu):
        print(f"{number + 1}. {item}")
        option_list.append(str(number+1))
        option_list.append(item)

    print("Please select an option:", end=" ")
    while selection not in option_list:
        selection = input()
        if selection not in option_list:
            print("Please select a valid option:", end=" ")

    try:
        selection = int(selection)
    except ValueError:
        return selection
    else:
        if isinstance(menu, list):
            value = menu[selection - 1]
        elif isinstance(menu, dict):
            value = list(menu.values())[selection - 1]
        try:
            if arguments is None:
                return value()
            else:
                return value(arguments)
        except TypeError:
            return value

def clear_screen():
    """Clear screen for Windows and Linux"""
    system('cls' if name == 'nt' else 'clear')
