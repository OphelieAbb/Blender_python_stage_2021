import bpy

import sys
import glob

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
#import SaveListCameras as cam_list
#reload(cam_list)

################################################################################

################################################################################

class ImportCamerasList(bpy.types.Operator):
    bl_idname = "test.import_cameras"
    bl_label  = "Import Cameras List"
    bl_description = "Import la list des cameras"
   

    def execute(self,context):
        filepath =r"C:\Users\ophelie.abbonato\Documents\SMURFS\SMF_List_Cameras.fbx"
        bpy.ops.import_scene.fbx(filepath = filepath)

        return{'FINISHED'}
    
class FileSaveCameras(bpy.types.Operator):
    bl_idname = "test.save_cameras"
    bl_label  = "Save Cameras List"
    bl_description = "Sauve la list des cameras"


    def execute(self,context):

        for obj in bpy.context.scene.objects:
            if obj.type == "CAMERA":
#                bpy.ops.object.select_all(action='DESELECT')
                obj.select_set(True)
                
                filepath =r"C:\Users\ophelie.abbonato\Documents\SMURFS\SMF_List_Cameras.fbx"
                bpy.ops.export_scene.fbx(filepath = filepath, use_selection=True)
                

        return{'FINISHED'}
    
class ListCameras(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.list_cameras"
    bl_label = "List Cameras"
    cam = bpy.props.StringProperty(default="", options={'SKIP_SAVE'})


    @classmethod
    def poll(cls, context):
        return context.active_object is not None


    def execute(self, context):
        print("CAMERA", self.cam)
        cam = context.scene.objects.get(self.cam)
        context.scene.camera = cam
        return {'FINISHED'}
    
class SaveListCameras(bpy.types.Operator):
    bl_idname = "test.list_camera"
    bl_label  = "Save list Camera"
    bl_description = "Save/Import ta list Cameras"
     
    def execute (self,context):
        
        bpy.ops.wm.call_menu(name=SimpleCustomMenu.bl_idname)
        
        return {"FINISHED"}
    
class SimpleCustomMenu(bpy.types.Menu):
    bl_label = "Cameras_Menu"
    bl_idname = "PT_Liste_Cameras"
    bl_space_type ='VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Save Cameras list'

    def draw(self, context):
        layout = self.layout
        scene  = bpy.context.scene
        
        cams = [c for c in context.scene.objects if c.type == 'CAMERA']
        #print(cams)
        for c in cams:
            op = layout.operator("object.list_cameras",text=c.name)
            op.cam = c.name
            
        
        row = layout.row()
        row.operator("test.save_cameras",icon='FILE_TICK')

        row = layout.row()
        row.operator("test.import_cameras",icon='IMPORT')
        
        return{'FINISHED'}

class OUTLINER_UI_extreme_cameras(bpy.types.UIList):
    
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
       
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
             
            layout.prop(item, "name", text="", emboss=False, icon_value=layout.icon(item))
            layout.prop(item, "hide_viewport", text="", emboss=False, icon = "HIDE_OFF")
            
class FileSave(bpy.types.Operator):
    bl_idname = "test.save_file"
    bl_label  = "Save Scene"
    bl_description = "Sauve ta scene"
    
    def execute(self,context):
        
        filepath =r"C:\Users\ophelie.abbonato\Documents\SMURFS\Scene_Smurf.blend"
        bpy.ops.wm.save_as_mainfile(filepath=filepath)

        return{'FINISHED'}
    
class RenderPngOperator(bpy.types.Operator):
    bl_idname = "test.render_png"
    bl_label  = "Render PNG"
    bl_description = "Rendu d'image PNG et incrémentation"
    
    def execute(self,context):
        
        scene  = bpy.context.scene
        #for i in range(scene.frame_start, scene.frame_end):
            
        list_files = glob.glob(r"C:\Users\ophelie.abbonato\Documents\SMURFS\SMF_112_Sq0001_Sh0001_image*.png")
        iteration = len(list_files)+1
        scene.render.image_settings.file_format ="PNG"
#        scene.render.filepath =r"C:\Users\ophelie.abbonato\Documents\SMURFS\shot{:03}.png".format(iteration)
        scene.render.filepath =r"C:\Users\ophelie.abbonato\Documents\SMURFS\SMF_112_Sq0001_Sh0001_image{:03}.png".format(iteration)
        bpy.ops.render.opengl(write_still=1)
        
        cam_pos.main()

                    
        return{'FINISHED'}


            
    
class RenderJpegOperator(bpy.types.Operator):
    bl_idname = "test.render_jpeg"
    bl_label  = "Render JPEG"
    bl_description = "Rendu d'image JPEG et incrémentation"
    
    def execute(self,context):
        
        scene  = bpy.context.scene
        cam = context.scene.camera
        
        list_files = glob.glob(r"C:\Users\ophelie.abbonato\Documents\SMURFS\SMF_112_Sq0001_Sh0001_image*.jpeg")
        iteration = len(list_files)+1
        scene.render.image_settings.file_format ="JPEG"
        scene.render.filepath =r"C:\Users\ophelie.abbonato\Documents\SMURFS\SMF_112_Sq0001_Sh0001_image{:03}.jpeg".format(iteration)
        
        bpy.ops.render.opengl(write_still=1)
        
        cam_pos.main()
        
        return{'FINISHED'}
    
    
class LockCamera (bpy.types.Operator):
    bl_idname = "test.lock_camera"
    bl_label  = "Camera locked"
    bl_description = "Verrouille la camera"
    
    def execute (self,context):
        bpy.context.object.lock_location[0] = True
        bpy.context.object.lock_location[1] = True
        bpy.context.object.lock_location[2] = True
        bpy.context.object.lock_rotation[0] = True
        bpy.context.object.lock_rotation[1] = True
        bpy.context.object.lock_rotation[2] = True
        bpy.context.object.lock_scale[0] = True
        bpy.context.object.lock_scale[1] = True
        bpy.context.object.lock_scale[2] = True
        return{'FINISHED'}

class UnlockCamera (bpy.types.Operator):
    bl_idname = "test.unlock_camera"
    bl_label  = "Camera unlocked"
    bl_description = "Déverrouille la camera"
    
    def execute (self,context):
        bpy.context.object.lock_location[0] = False
        bpy.context.object.lock_location[1] = False
        bpy.context.object.lock_location[2] = False
        bpy.context.object.lock_rotation[0] = False
        bpy.context.object.lock_rotation[1] = False
        bpy.context.object.lock_rotation[2] = False
        bpy.context.object.lock_scale[0] = False
        bpy.context.object.lock_scale[1] = False
        bpy.context.object.lock_scale[2] = False
        return{'FINISHED'}
    
################################################################################

################################################################################

class CamerasPanel(bpy.types.Panel):
    bl_label = "Camera_Panel"
    bl_idname = "PT_Cameras"
    bl_space_type ='VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Panel Cameras'
    
    def draw(self, context):
        layout = self.layout
        col    = layout.column(align=True)
        scene  = bpy.context.scene
        cam = context.scene.camera
        
        row = layout.row()
        row.label(text= "Create Camera", icon='VIEW_CAMERA')
        row.operator("object.camera_add")
        row.operator("view3d.camera_to_view")
        row = layout.row()
        
        row = layout.row()
        row.label(text= "Lock Cam", icon = "LOCKED")
        row.operator("test.lock_camera")
        row.operator("test.unlock_camera")
        row = layout.row()
        
        col.prop(context.scene.camera.data, "lens") 
        
        col.separator()
        col.prop(context.scene, "camera")
        col.separator()

        row = layout.row()
        row.operator("test.render_png")

        row = layout.row() 
        row.operator("test.render_jpeg")
        row = layout.row()
        
        
        row = layout.row()
        row.operator("test.list_camera",icon='PRESET')
        row = layout.row()
        
        col = layout.column()
        col.template_list(
            "OUTLINER_UI_extreme_cameras",
            "",
            scene,
            "objects",
            scene,
            "active_object_index")
            

def register():
    
    bpy.utils.register_class(RenderPngOperator)
    bpy.utils.register_class(RenderJpegOperator)
    bpy.utils.register_class(LockCamera)
    bpy.utils.register_class(UnlockCamera)

    bpy.utils.register_class(OUTLINER_UI_extreme_cameras)
    
    bpy.utils.register_class(SaveListCameras)
    bpy.utils.register_class(SimpleCustomMenu)
    bpy.utils.register_class(ListCameras)
    bpy.utils.register_class(FileSaveCameras)
    bpy.utils.register_class(ImportCamerasList)
    
    bpy.utils.register_class(CamerasPanel)
    
    bpy.types.Scene.active_object_index = IntProperty()
    
def unregister():
    
    bpy.utils.unregister_class(RenderPngOperator)
    bpy.utils.unregister_class(RenderJpegOperator)
    bpy.utils.unregister_class(LockCamera)
    bpy.utils.unregister_class(UnlockCamera)
    bpy.utils.unregister_class(OUTLINER_UI_extreme_cameras)
    
    bpy.utils.unregister_class(SaveListCameras)
    
    bpy.utils.unregister_class(SimpleCustomMenu)
    bpy.utils.unregister_class(ListCameras)
    bpy.utils.unregister_class(FileSaveCameras)
    bpy.utils.unregister_class(ImportCamerasList)
    
    bpy.utils.unregister_class(CamerasPanel)
    
if __name__ == "__main__":
    register()
    


