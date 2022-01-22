from typing import Union


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



if __name__ == "__main__":
    
    # Standard data selection menu
    options = ["option 1", "option 2", "option 3", "option 4"]
    print(options_menu(options))
    
    # Function selection demonstration
    def lol_one():
        print("we are number one")
        
    def lol_two():
        print("we are number two")

    options = {"option 1": lol_one, "option 2": lol_two}
    options_menu(options)()
