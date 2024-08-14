import stdio
from handin1api import *
from compass import Compass
import stdrandom #random movement of the bees
import sys 

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
    #parameter type validation
    
    #mapsize.
    try:
        int(size)
        size = int(size)
    except ValueError:
        stdio.write("ERROR: Invalid configuration line")
        sys.exit()    
    
    if size < 0:
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

def read_map():
    # configuration parameters
    mapsize = stdio.readString()
    duration = stdio.readString()
    type_pollen = stdio.readString()
    action_pollen = stdio.readString()
    valid_config_par(mapsize, duration, type_pollen, action_pollen)
    # board opjects
    gameMap = Map(size=int)
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


