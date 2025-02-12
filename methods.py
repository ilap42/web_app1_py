FILEPATH = "TO_DO.txt"
def readonfile(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as file:
        lines = file.readlines()
        return lines
        #new_lines = [item.strip("\n") for item in lines]
        #return new_lines

def writeonfile(lista:list, filepath=FILEPATH):
    """ Write the to-do in the text file.
    """
    with open(filepath, "w") as file:
        file.writelines(lista)