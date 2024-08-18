import instream
import stdio
from handin1api import *
from compass import Compass
import stdrandom #random movement of the bees
import sys 
import stdarray
#--------------------------------------------------GLOBAL VARIABLES--------------------------------------------------#
file_content = stdio.readAllLines()
file_content = [arg.split() for arg in file_content]
mapsize = file_content[0][0]
duration = file_content[0][1]
type_pollen = file_content[0][2]
action_pollen = file_content[0][3]
coords = {} # dictionary that stores board objects and their respecitve x-y coordinates.
board_entities = []
v_board_obj = ['B','D','H','W','F'] #valid letters that represent the games board objects.
#--------------------------------------------------------------------------------------------------------------------#
def valid_GUI(mode):
    
    '''Validates whether the command line argument provided is valid or invalid.
    This function should be executed before the simulation is rendered. 
    '''
    # too many argments
    if len(sys.argv) > 2:
        stdio.write("ERROR: Too many arguments")
        sys.exit()      
    # correct integer values    
    elif not (int(mode) == 0 or int(mode) == 1):
        stdio.write(f"ERROR: Invalid argument: {mode}")
        sys.exit()
    else:
        pass

def valid_config_par(size, dur, _type, action) -> None:
    #add documentation
    #parameter type validation
    
    #mapsize.
    try:
        int(size)
    except ValueError:
        stdio.write("ERROR: Invalid configuration line")
        sys.exit()    
    size = int(size)
    if not (1 <= size <= 100):
        stdio.write("ERROR: Invalid configuration line")
        sys.exit()                     
    #game duration.
    try:
        int(dur)
        dur = int(dur)
    except ValueError:
        stdio.write("ERROR: Invalid configuration line")
        sys.exit()
        
    if dur < 0:
        stdio.write("ERROR: Invalid configuration line")
        sys.exit()
    #pollen type.
    if _type not in ('s','f'):
        stdio.write("ERROR: Invalid configuration line")
        sys.exit()
    #pollen action.
    if action not in ('max','min','sum','sort'):
        stdio.write("ERROR: Invalid configuration line")
        sys.exit()    
    return True

def coordinates():
    '''creates dictionary with (x,y) coordinates of the board objects. 
    The function creates empty strings for all coordinates.
    '''
    global mapsize
    
    for x in range(int(mapsize)):
        for y in range(int(mapsize)):
            coords[(x, y)] = ""
            
def valid_coords(coords: dict, x, y):
    '''vaidates whether coordinates of a given oject is within the range of the map
    and if there is any object currently occupying the position.
    '''
    if not (0 <=x<= int(mapsize) and 0 <=y<= int(mapsize)):
        return False
    if coords[(x,y)] != "":
        return False
    return True
    
def valid_board_obj(object, x, y, validobjects: list):
    pass
def read_map():
    global board_entities
    global coords
    global type_pollen
    global file_content
    # configuration parameters
    valid_config_par(mapsize, duration, type_pollen, action_pollen)
    # 2D list set up for board objects.
    rows = int(mapsize)
    cols = int(mapsize)
    gameMap = Map(int(mapsize))
    board_entities = [['' for obj in range(rows)] for obj in range(cols)]
    
    for line in range(1,len(file_content)):
        for char in range(len(file_content)):
            
            if file_content[line][0] in v_board_obj:
                if len(file_content[line]) != 4:
                    stdio.write(f"ERROR: Invalid object setup on line {line+1}")
                    sys.exit()
                if file_content[line][0] == 'F':
                    x_ent = file_content[line][1] # x coordinate of flower
                    y_ent = file_content[line][2] # y coordinate of flower
                    n_granules = file_content[line][3] # number of pollen granules in flower
                    for info in r
            else:
                stdio.write(f"ERROR: Invalid object setup on line {line+1}")
                sys.exit()
                     
                
    # board opjects
    pass 

def test_compass(row: int, col: int, speed: int, size: int, moves: int):
    pass
def main():
    # too few arguments. 
    if len(sys.argv) == 1:
        stdio.write(f"ERROR: too few arguments")
        sys.exit()
        
    # 0: non-GUI mode; 1: GUI mode.
    indiGUI = sys.argv[1]
    # validate whether given GUI argument is of int data type.
    try:
        int(indiGUI)
    except ValueError:
        stdio.write(f"ERROR: invalid argument: {indiGUI}")
        sys.exit()

    valid_GUI(indiGUI)
    read_map()
if __name__ == "__main__": 
    main()

