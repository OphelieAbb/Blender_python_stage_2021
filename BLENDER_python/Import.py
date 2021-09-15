from importlib import reload
import sys

my_path = r"C:\Users\artiste\Documents\Grase_Pencil"

if not my_path in sys.path:
    print("adding")
    sys.path.append(my_path)
    
import cam_position_by_frame_dict as toto
reload(toto)

position_by_frame = toto.get_cam_position_by_frame()

for cle, valeurs in position_by_frame.items():
    print(cle)
    for frame in valeurs:
        print("    \____ ", frame)
        print("")