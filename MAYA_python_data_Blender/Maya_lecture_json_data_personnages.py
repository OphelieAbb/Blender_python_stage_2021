import maya.cmds as cmds
import json
import sys

def read_fichier_json(filepath):
    with open(filepath) as f :
        data_personnage = json.load(f)
        
    return data_personnage
    
filepath = r"C:\Users\ophelie.abbonato\Documents\SMURFS\Json\data_personnage.json"
position_data = read_fichier_json(filepath)


for board_name, informations in position_data.iteritems():
    personnage = cmds.polyCube(name=board_name)
    personnage = cmds.ls(sl = True)[0]
    personnage_shape = cmds.listRelatives(personnage, children=True)[0]

    for frame, value in informations.iteritems():
        print("#"*80)
        print(frame)
        print(value)

        if type(value) == dict:
        
            for frame , position in value.iteritems():
                print("#"*80)
                print("frame    : ", frame)
                print("position : ", position)
                
                cmds.move(position["location"][0], position["location"][2], position["location"][1], board_name)
                cmds.rotate(position["rotation"][0],position["rotation"][1],position["rotation"][2],board_name)
                cmds.scale(position["scale"][0],position["scale"][1],position["scale"][2])


    