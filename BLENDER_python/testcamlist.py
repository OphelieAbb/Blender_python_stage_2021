import os
import sys
import glob
from importlib import reload


import bpy
from bpy.types import PropertyGroup
from bpy.props import (
    CollectionProperty,
    IntProperty,
    BoolProperty,
    StringProperty,
    PointerProperty,
)

# Authoriser import local pour le moment
my_script_path = r"C:\Users\ophelie.abbonato\Documents\SMURFS\Script_Python\BLENDER_python"

if not my_script_path in sys.path:
    print("Adding :D")
    sys.path.append(my_script_path)

import Camera_position_by_frame as cam_pos
import SaveListCameras as cam_list
reload(cam_list)

################################################################################

class SaveListCameras(bpy.types.Operator):
    bl_idname = "test.list_camera"
    bl_label  = "Save list Camera"
    bl_description = "Save/Import ta list Cameras"
     
    def execute(self,context):
        for i in range(50):
            print("")
        cam_list.register()

        return {"FINISHED"}



class StoryboardPanel(bpy.types.Panel):
    bl_label = "Camera_Panel"
    bl_idname = "PT_Cameras"
    bl_space_type ='VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Create Cameras'
    
    
    
    
    def draw(self, context):
        layout = self.layout
        col    = layout.column(align=True)
        scene  = bpy.context.scene
        cam = context.scene.camera
        

        
        row = layout.row()
        row.operator("test.list_camera",icon='PRESET')
        



def register():
    

    bpy.utils.register_class(SaveListCameras)
    
    
    bpy.utils.register_class(StoryboardPanel)
    



def unregister():
    
    bpy.utils.unregister_class(SaveListCameras)
    
    bpy.utils.unregister_class(StoryboardPanel)
    
    

if __name__ == "__main__":
    register()
        
    SaveListCameras(self,context)
             