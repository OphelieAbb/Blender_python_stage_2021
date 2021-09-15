import json
import sys
import maya.cmds as cmds
import pprint
import math
################################################################################

def read_fichier_json(my_path):
        
    with open (my_path) as f:
        data = json.load(f)

    return data

################################################################################  

my_path = r"C:\Users\ophelie.abbonato\Documents\SMURFS\Json\data_camera_position.json"
position_data = read_fichier_json(my_path)

for camera_name, informations in position_data.iteritems():
    cam = cmds.camera(name=camera_name)
    cam = cmds.ls(sl = True)[0]
    cam_shape = cmds.listRelatives(cam, children=True)[0]

    for frame, value in informations.iteritems():
        cmds.xform(cam, t=[value["Translation"][0][3], value["Translation"][1][3], value["Translation"][2][3]])
        cmds.xform(cam, ro=[math.degrees(value["Rotation"][0]), math.degrees(value["Rotation"][1]), math.degrees(value["Rotation"][2])])
        cmds.setAttr("{}.focalLength".format(cam_shape), value["Focal"])
        cmds.setKeyframe(cam, time=int(frame))
        
        #cmds.setAttr(focusDistance)

          
     




"""
for camera_name, informations in position_data.iteritems():
    cam = cmds.camera(name=camera_name)
    print(cam)
    cam = cmds.ls(sl = True)[0]
    print(cam)
    for key, values in informations.items():
        new_matrix = []
        for value in values:
            print(key, " : ", value)
            new_matrix.append(float(value))
        print(new_matrix)
        cmds.xform(cam, matrix=world_matrix)
        
        cmds.setKeyframe(cam, time=int(key))
"""
#cmds.xform(cam, matrix=world_matrix)

#cmds.move(world_matrix[0], world_matrix[1], world_matrix[2])
#cmds.setKeyframe()

#cameras = cmds.ls(sl=True)[0]

#cmds.xform(cameras, matrix=flatten_matrix)

#cmds.move(world_matrix[3], 0.0, 0.0, absolute=True)  #world_matrix[0], world_matrix[0])
"""

    print camera_name
    cam = cmds.camera(name=camera_name)
    cam = cmds.ls(sl = True)[0]
    
    for frame, world_matrix in informations.iteritems():
        #print world_matrix[3]
        
        print(frame)
        int_frame = int(frame)
        print "#"*20, " ", world_matrix[7]
        xform.setRotation(world_matrix[5], world_matrix[6], world_matrix[7], cam)
        cmds.setKeyframe(cam, time=int_frame)

"""