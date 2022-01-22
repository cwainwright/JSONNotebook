def node_display(node, indent = 0) -> str:
    if not indent:
        display_string = str(node)
    else:
        display_string = "\n" + indent * " " + "\u2514" + str(node)
    for child in node.children.values():
        display_string += node_display(child, indent + 1)

    return display_string
