import bpy
import json
import os
import numpy as np
from mathutils import Matrix



################################################################################

def get_cameras():
    
    cameras = []
    
    for obj in bpy.data.objects :
        if obj.type == "CAMERA":
            cameras.append(obj)

    return cameras
################################################################################

def profondeur_de_champ(cameras):
    
    for camera in cameras:
        if camera.data.dof.use_dof:
            print(camera)
            print("#"*80, "          profondeu_champ")
            print("La profondeur de champ est activé")

    

################################################################################

def get_camera_position_by_frame(cameras, scene):

    cam_position_by_frame = {}

    for cam in cameras:
        print("#"*80)
        
        cam_position_by_frame[cam.name] = {}
        
        
        for frame in range(scene.frame_start, scene.frame_end):
            bpy.context.scene.frame_set(frame)
            orig_loc, orig_rot, orig_sca = cam.matrix_world.decompose()
            cam_position_by_frame[cam.name][frame] = {"Translation": [], "Rotation":[], "Focal":[],"Focus_Distance":[]}
            
            orig_loc_mat   = Matrix.Translation(orig_loc)
            orig_rot_mat   = orig_rot.to_euler()
            print("#"*80)
            print("orig_rot_mat: ", orig_rot_mat)
            print("")


            cam_position_by_frame[cam.name][frame]["Translation"] = [
                                                                    [x for x in orig_loc_mat[0]],
                                                                    [z for z in orig_loc_mat[2]],
                                                                    [-y for y in orig_loc_mat[1]]
                                                                    ]


            #original_rotation_matrix = [orig_rot_mat.x, orig_rot_mat.y, orig_rot_mat.z]

            cam_position_by_frame[cam.name][frame]["Rotation"] = rotation_matrix_tranform(orig_rot_mat)

            # Dstance focal
            cam_position_by_frame[cam.name][frame]["Focal"] = cam.data.lens
            print("#"*80)
            print(cam.data.lens)
            
            #Profondeur de champ mettre du flou ou pas 
            cam_position_by_frame[cam.name][frame]["Focus_Distance"] = cam.data.dof.focus_distance
            print("#"*80)
            print(cam.data.dof.focus_distance)
            
#            cam_position_by_frame[cam.name][frame]["Scale"] = [orig_sca_mat.x,
#            orig_sca_mat.y,
#            orig_sca_mat.z]
            
    return cam_position_by_frame

################################################################################

def rotation_matrix_tranform(original_rotation_matrix):
    """
    Roll:
        blender: Y
        maya   : Z
    
    Pitch:
        blender: X
        maya   : X
    
    Yaw:
       blender : Z
       maya    : Y
    """

    original_rotation_matrix_filtered = [
                                [original_rotation_matrix.x],
                                [ original_rotation_matrix.y],
                                [original_rotation_matrix.z]
                                ]

    print("#"*80, "     ICI")
    print(original_rotation_matrix.x)
    print("")


    transformation_matrix = [
                            [1, 0, 0],
                            [0, 0, 1],
                            [0, 1, 0]
                            ]
    
    tranformed_rotation_matrix =  np.dot(transformation_matrix, original_rotation_matrix)
        
    print(tranformed_rotation_matrix)
    
    print("#"*80, " COUCOU")
    print(" ------> ", tranformed_rotation_matrix)
    tranformed_rotation_matrix[0] = tranformed_rotation_matrix[0] - 1.5708
    print(" ------> ", tranformed_rotation_matrix)
    
    return tranformed_rotation_matrix

################################################################################
"""
def applatit_la_matrix(matrix_world):

    flattened_matrix = []

    for each_vector in matrix_world:

        for value in each_vector:
            flattened_matrix.append(value)
            
    return flattened_matrix
"""

################################################################################

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)



################################################################################

def create_fichier_json(argument_des_positions_de_camera):
    
    
    #data = json.dumps(argument_des_positions_de_camera)
    
    file_path = r"C:\Users\ophelie.abbonato\Documents\SMURFS\Json\data_camera_position.json"

    print(argument_des_positions_de_camera)

    with open(file_path, 'w') as fp:
        #json.dump(argument_des_positions_de_camera, fp )
        json.dump(argument_des_positions_de_camera, fp , cls=NumpyEncoder)

################################################################################

def main():
    scene = bpy.context.scene
    cameras = get_cameras()
    cameras_positions = get_camera_position_by_frame(cameras, scene)
    creation_fichier_data_cameras = create_fichier_json(cameras_positions)
    
    profondeu_champ = profondeur_de_champ(cameras)

################################################################################

if __name__ == "__main__":
    
    main()


"""
            # Roll:
            #    blender: Y
            #    maya   : Z
            
            # Pitch:
            #    blender: X
            #    maya   : X
            
            # Yaw:
            #   blender : Z
            #   maya    : Y

            cam_position_by_frame[cam.name][frame]["RotationYaw"] = [orig_rot_mat.x, 
            orig_rot_mat.y,
            orig_rot_mat.z]
            
            cam_position_by_frame[cam.name][frame]["RotationRoll"] = [orig_rot_mat.y, 
            orig_rot_mat.x,
            orig_rot_mat.z]
            
            cam_position_by_frame[cam.name][frame]["RotationPitch"] = [orig_rot_mat.x, 
            orig_rot_mat.y,
            orig_rot_mat.z]
"""