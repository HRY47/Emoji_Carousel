"""ASCII art helpers for the emoji carousel UI."""

def first_add():
    '''
        prints the first item adding sequence
        return: None
    '''
    print("                            |‾‾|")
    print("               |‾‾‾‾‾‾‾‾‾‾‾‾|  |‾‾‾‾‾‾‾‾‾‾‾‾|")
    print("               |            |  |            |")
    print("               |            |  |            |")
    print("               |           _|  |_           |")
    print("               |          \      /          |")
    print("               |           \    /           |")
    print("               |____________\  /____________|")
    print("                             \/")
    print("")


def last_del():
    '''
        prints the last item 
        deleting sequence
        return: None
    '''
    print("                             /\\")
    print("               |‾‾‾‾‾‾‾‾‾‾‾‾/  \‾‾‾‾‾‾‾‾‾‾‾‾|")
    print("               |           /    \           |")
    print("               |          /_    _\          |")
    print("               |            |  |            |")
    print("               |            |  |            |")
    print("               |            |  |            |")
    print("               |____________|  |____________|")
    print("                            |__|")
    print("")
    
    
def not_last_del(first: str,second: str):
    '''
        prints an item deleting sequence(not the last)
        return: None
    '''
    print("                             /\ ")
    print(" __________    |‾‾‾‾‾‾‾‾‾‾‾‾/  \‾‾‾‾‾‾‾‾‾‾‾‾|    __________")
    print("           |   |           /    \           |   |")
    print("           |   |          /_    _\          |   |")
    print(" ()        |   ".replace("()",first),end='')
    print("|            |  |            |   |        ()".replace("()",second))
    print("           |   |            |  |            |   |")
    print(" __________|   |            |  |            |   |__________")
    print("               |____________|  |____________|")
    print("                            |__|")
    

def one_item_print(item: str):
    '''
        prints the one item board
        return: None
    '''
    print("                             ↓↓")
    print("               |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    print("               |                            |")
    print("               |                            |")
    print("               |             ()             |".replace("()",item))
    print("               |                            |")
    print("               |                            |")
    print("               |____________________________|")
       

def three_item_print(first: str,current: str,second: str):
    '''
        prints the three item board
        return: None
    '''
    print("                             ↓↓")
    print(" __________    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    __________")
    print("           |   |                            |   |          ")
    print("           |   |                            |   |          ")
    print(" ()        |   ".replace("()",first),end='')
    print("|             ()             |   ".replace("()",current),end='')
    print("|        ()".replace("()",second))
    print("           |   |                            |   |          ")
    print(" __________|   |                            |   |__________")
    print("               |____________________________|")
    
    
def print_going_left(first: str,second: str):
    '''
        prints the going left sequence
        return: None
    '''
    print("                 /|                      ")
    print(" __________     / |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    __________")
    print("           |   /  |                         |   |")
    print("           |  /    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| |")
    print(" ()        | ".replace("()",first,1),end='')
    print("|              Left              | |        ()".replace("()",second,1))
    print("           |  \    ___________________________| |")
    print(" __________|   \  |                         |   |__________")
    print("                \ |_________________________|")
    print("                 \|")
   
   
def print_adding_left_one():
    '''
        prints the adding left sequence
        when we only have one item
        return: None
    '''
    print("                 /|")
    print("                / |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    print("               /  |                         |")
    print("              /    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    print("             |           Adding Left          |")
    print("              \    ___________________________|")
    print("               \  |                         |")
    print("                \ |_________________________|")
    print("                 \|")
    
    
def print_adding_left_two(first: str,second: str):
    '''
        prints the adding left sequence 
        when we have more than one item
        return: None
    '''
    print("                 /|                      ")
    print(" __________     / |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    __________")
    print("           |   /  |                         |   |")
    print("           |  /    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| |")
    print(" ()        | ".replace("()",first,1),end='')
    print("|           Adding Left          | |        ()".replace("()",second,1))
    print("           |  \    ___________________________| |")
    print(" __________|   \  |                         |   |__________")
    print("                \ |_________________________|")
    print("                 \|")
    
    
def print_going_right(first: str,second: str):
    '''
        prints the going right sequence
        return: None
    '''
    print("                                         |\\")
    print(" __________    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| \     __________")
    print("           |   |                         |  \   |")
    print("           | |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    \  |")
    print(" ()        | ".replace("()",first,1),end='')
    print("|            Right               | |        ()".replace("()",second,1))
    print("           | |___________________________    /  |")
    print(" __________|   |                         |  /   |__________")
    print("               |_________________________| /")
    print("                                         |/")
    
    
def print_adding_right_one():
    '''
        prints the adding right sequence
        when we only have one item
        return: None
    '''
    print("                                         |\\")
    print("               |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| \\")
    print("               |                         |  \\")
    print("             |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    \\")
    print("             |        Adding Right            |")
    print("             |___________________________    /")
    print("               |                         |  /")
    print("               |_________________________| /")
    print("                                         |/")
    print("")
    
    
def print_adding_right_two(first: str,second: str):
    '''
        prints the adding left sequence 
        when we have more than one item
        return: None
    '''
    print("                                         |\\")
    print(" __________    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| \     __________")
    print("           |   |                         |  \   |")
    print("           | |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    \  |")
    print(" ()        | ".replace("()",first,1),end='')
    print("|        Adding Right            | |        ()".replace("()",second,1))
    print("           | |___________________________    /  |")
    print(" __________|   |                         |  /   |__________")
    print("               |_________________________| /")
    print("                                         |/")
    print("")
    
