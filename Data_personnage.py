import bpy
import json
import os
import numpy as np

##################################################################################

def get_grease_pencil_boards():

    boards = []    

    for obj in bpy.data.objects :
        if obj.type == "GPENCIL":
            boards.append(obj)

    return boards

##################################################################################

def get_grease_pencil_layers(board): 
    """
    Get grease pencil layers
    """

    layers = []

    for layer in board.data.layers:
        layers.append(layer)
        
    return layers

##################################################################################
        
def get_location_rotation_scale(board):
    
    board_gp_position = {"location":[], "rotation" :[], "scale" :[]}

    board_gp_position["location"] = [board.location[0], board.location[1], board.location[2]] 
    board_gp_position["rotation"] = [board.rotation_euler[0], board.rotation_euler[1], board.rotation_euler[2]]
    board_gp_position["scale"]    = [board.scale[0], board.scale[1], board.scale[2]]

    return board_gp_position    

##################################################################################

def get_animation_grease_pencil_layers(dico, my_context):

    totla_dico_tout_plein_de_frame = {}

    # for frame in range(my_context.frame_start, my_context.frame_end):
    #     mini_dico = get_location_rotation_scale(dico)
    #     totla_dico_tout_plein_de_frame[frame] = mini_dico
        #my_context.frame_set(frame)



    

    # dico = bpy.context.object

    # if dico.animation_data is not None :#and dico.animation_data.action is not None:
    #     action = dico.animation_data.action
    #     print()
    #     print("Keyframes")
    #     print("---------")

    #     for fcu in action.fcurves:
    #         print( action.fcurves)
    #         print()
    #         print(fcu.data_path, fcu.array_index)
    #         for kp in fcu.keyframe_points:
    #             print("  Frame %s: %s" % (kp.co[:]))#kp=un entier
    #             for i in range(my_context.frame_start, my_context.frame_end):
    #                 print("  Frame %i: %.6f" % (i, fcu.evaluate(i)))


################################################################################

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

##################################################################################
            
def create_fichier_json(positions_des_calques_story_board):
    
    
    #data = json.dumps(argument_des_positions_de_camera)
    
    file_path = r"C:\Users\ophelie.abbonato\Documents\SMURFS\Json\data_personnage.json"

    print(positions_des_calques_story_board)

    with open(file_path, 'w') as fp:
        #json.dump(argument_des_positions_de_camera, fp )
        json.dump(positions_des_calques_story_board, fp , cls=NumpyEncoder)




##################################################################################

def main():

    for i in range(100):
        print("")

    my_context = bpy.context.scene
    my_scene   = bpy.context.scene.grease_pencil
    GP_boards  = get_grease_pencil_boards()

    dico_board_layer_pos_par_frame = {}

    for board in GP_boards:

        GP_layers = get_grease_pencil_layers(board)
        dico_board_layer_pos_par_frame[board.name] = {}

        for layer in GP_layers:

            dico_board_layer_pos_par_frame[board.name][layer.info] = []
            dico_board_layer_pos_par_frame[board.name]["frames"] = {}

            #for layer in get_grease_pencil_layers(board):
            dico_board_layer_pos_par_frame[board.name][layer.info].append(layer.info)

            for frame in range(my_context.frame_start, my_context.frame_end):
                my_context.frame_set(frame)
                board_situation = get_location_rotation_scale(board)
                dico_board_layer_pos_par_frame[board.name]["frames"][frame] = board_situation
 
    print("#"*80)


    for board_name, layers in dico_board_layer_pos_par_frame.items():

        print(board_name)

        for layer in layers:
            print("    \____ ", layer)


        for frame, situations in layers["frames"].items():
            print("    \____", frame)
            for transformation, value in situations.items():
                print("     \___ ", transformation)
                print("        _ ", value)

        print("")
        print("#"*80)
        
    create_fichier_json(dico_board_layer_pos_par_frame)
 
    print("COUCOU MICHELE!!!!")

##################################################################################

if __name__ == "__main__":
    
    main()



    # for layer in GP_layers:
    #     GP_layers

    # for frame in range(my_context.frame_start, my_context.frame_end):
    #     print(frame)
    #     my_context.frame_set(frame)
    #     mini_dico = get_location_rotation_scale(dico)
    #     totla_dico_tout_plein_de_frame[frame] = mini_dico
        #  

    #position_rotation_scale = get_location_rotation_scale(GP_boards)

    # get_animation_grease_pencil_layers(position_rotation_scale, my_context)