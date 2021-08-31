import os
import sys
import glob
#from importlib import reload


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


class OUTLINER_UI_extreme_cameras(bpy.types.UIList):
    
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
       
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
             
            layout.prop(item, "name", text="", emboss=False, icon_value=layout.icon(item))
            layout.prop(item, "hide_viewport", text="", emboss=False, icon = "HIDE_OFF")
        



class JoinArea(bpy.types.Operator):
    bl_idname = "screen.join_area"
    bl_label  = "Join Window"
    bl_description = "Reuni la fenêtre en une vue"
    
    def execute(self, context):
        
#        area1 = bpy.context.screen.areas[3]
#        area2 = bpy.context.screen.areas[-1]
        

        bpy.ops.screen.screen_full_area()

        
        return {"FINISHED"}


class VuePersp(bpy.types.Operator):
    bl_idname = "test.vue_persp"
    bl_label  = "Vue Persp"
    bl_description = "Retourne en vue Perspective"
    

    def execute(self,context):
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                area.spaces[0].region_3d.view_perspective = 'PERSP'
                break

        return{'FINISHED'}
    
class VueCam(bpy.types.Operator):
    bl_idname = "test.vue_cam"
    bl_label  = "Vue Cam"
    bl_description = "Retourne en vue Camera"
    

    def execute(self,context):
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                area.spaces[0].region_3d.view_perspective = 'CAMERA'
                break

        return{'FINISHED'}




class InsertKeyframe(bpy.types.Operator):
    bl_idname = "test.insert_keyframes"
    bl_label  = "Insert Keyframes"
    bl_description = "Insert clé animation sur Location/Rotation/focal"
    

    def execute(self,context):
    
        cam = bpy.data.cameras
        bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocRot')
        cam.keyframe_insert(data_path = 'lens', frame = (timeline_frame))
        return{'FINISHED'}

class Animation(bpy.types.Operator):
    bl_idname = "test.animation"
    bl_label  = "Open Timeline"
    bl_description = "ouvre la timeline pour l'aniamtion"
    
    def execute(self,context):
        
        scene  = bpy.context.scene

        bpy.ops.screen.area_split(direction="HORIZONTAL", factor=0.2)
        new_area = bpy.context.screen.areas[-1]
        new_area.type= 'DOPESHEET_EDITOR'

        return{'FINISHED'}



class FileSave(bpy.types.Operator):
    bl_idname = "test.save_file"
    bl_label  = "Save Scene"
    bl_description = "Sauve ta scene"
    
    def execute(self,context):
        
        filepath =r"C:\Users\ophelie.abbonato\Documents\SMURFS\Scene_Smurf.blend"
        bpy.ops.wm.save_as_mainfile(filepath=filepath)

        return{'FINISHED'}


class LibraryMesh(bpy.types.Operator):
    bl_idname = "test.file_browser"
    bl_label  = "Import File"
    bl_description = "ouvre librairie 3d pour import mesh"
    
    def execute(self,context):
        # Call user prefs window
        bpy.ops.screen.userpref_show("INVOKE_DEFAULT")

        # Change area type
        area = bpy.context.window_manager.windows[-1].screen.areas[0]
        area.type = 'FILE_BROWSER'
        return{'FINISHED'}



#class RenameCamOperator(bpy.types.Operator):
#    bl_idname = "test.rename_cameras"
#    bl_label  = "Renomme Cam en Shot"
#    bl_description = "Renomme la camera en shot et l'incrémente"
#    
#    def execute(self, context):
#        textentry="shot"
#        
#        for obj in bpy.context.selected_objects:
#            obj.name = textentry
#        return{'FINISHED'}




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

#Rendre une video mp4    
class RenderAnimation(bpy.types.Operator):
    bl_idname = "test.render_animation"
    bl_label  = "Render Animation"
    
    def execute(self,context):
        scene  = bpy.context.scene
        #for iteration in range(scene.frame_start, scene.frame_end):
        scene.render.image_settings.file_format ="FFMPEG"
        
        
        scene.render.filepath =r"C:\Users\ophelie.abbonato\Documents\SMURFS\animation.ffmpeg"
        
        bpy.ops.render.opengl(animation=True)
        bpy.ops.render.opengl(write_still=1)
        

        
class NavigationSimplifiee (bpy.types.Operator):
    bl_idname = "test.navigation"
    bl_label   = "Navigation Simple"
    bl_description = "Navigation simplifiée avec les flèches pour se déplacer et la souris pour diriger le regard"
    
    
    
    def execute(self,context):
        
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        override = {'area': area, 'region': region}
                        bpy.ops.view3d.walk(override, 'INVOKE_DEFAULT')  
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

    

class SplitArea(bpy.types.Operator):
    bl_idname = "screen.split_area"
    bl_label  = " Split Window"
    bl_description = "Divise la fenêtre en vue camera et perspective"
    
    def execute(self, context):

        bpy.ops.screen.area_split(direction="VERTICAL", factor=0.3)

        if context.region_data.view_perspective == 'PERSP':
            context.region_data.view_perspective = 'CAMERA'
            
        else:
            context.region_data.view_perspective = 'PERSP'

        return {"FINISHED"}
    
class focal24 (bpy.types.Operator):
    bl_idname = "test.focal_value24"
    bl_label  = "24"
    bl_description = "Focal camera à 24 mm"
    
    dir(bl_description)
    
    def execute (self,context):
        bpy.context.object.data.lens = 24
   
        return{'FINISHED'}
    
class focal28 (bpy.types.Operator):
    bl_idname = "test.focal_value28"
    bl_label  = "28"
    bl_description = "Focal camera à 28 mm"
    
    def execute (self,context):
        bpy.context.object.data.lens = 28
   
        return{'FINISHED'}
    
class focal35 (bpy.types.Operator):
    bl_idname = "test.focal_value35"
    bl_label  = "35"
    bl_description = "Focal camera à 35 mm"
    
    def execute (self,context):
        bpy.context.object.data.lens = 35
   
        return{'FINISHED'}
    
class focal50 (bpy.types.Operator):
    bl_idname = "test.focal_value50"
    bl_label  = "50"
    bl_description = "Focal camera à 50 mm"
    
    def execute (self,context):
        bpy.context.object.data.lens = 50
   
        return{'FINISHED'}
    
class focal70 (bpy.types.Operator):
    bl_idname = "test.focal_value70"
    bl_label  = "70"
    bl_description = "Focal camera à 70 mm"
    
    def execute (self,context):
        bpy.context.object.data.lens = 70
   
        return{'FINISHED'}
    
class focal100 (bpy.types.Operator):
    bl_idname = "test.focal_value100"
    bl_label  = "100"
    bl_description = "Focal camera à 100 mm"
    
    def execute (self,context):
        bpy.context.object.data.lens = 100
   
        return{'FINISHED'}

class DeleteKeyframe(bpy.types.Operator):
    bl_idname = "test.delete_keyframe"
    bl_label  = "Delete keyframe"
    
    def execute(self,context):
        bpy.context.active_object.keyframe_delete("location")
        bpy.context.active_object.keyframe_delete("rotation_euler")

        return{'FINISHED'}

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

################################################################################

################################################################################
            

class StoryboardPanel(bpy.types.Panel):
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
#        pcoll = preview_collections["main"]
        
        row = layout.row() 
        row.operator("test.animation", icon = "TIME") 

        
        row = layout.row() 
        row.operator("test.insert_keyframes", icon = "KEYFRAME") 
        row.operator("test.delete_keyframe", icon = "KEYFRAME")
        
        row = layout.row() 
        row.operator("test.render_animation") 
        row = layout.row() 
        
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
        
#        row = layout.row()
#        row.label(text= "Slectionne Cameras")
#        row.operator("test.rename_cameras")
        
        
        row = layout.row()
        row.label(text="Choose focal")
        row = layout.row()
        row.operator("test.focal_value24")
        row.operator("test.focal_value28")
        row.operator("test.focal_value35")

        row.operator("test.focal_value50")
        row.operator("test.focal_value70")
        row.operator("test.focal_value100")
        row = layout.row()
        #col.prop(context.scene.camera.data, "lens")  

        col.separator()
        col.prop(context.scene, "camera")
        col.separator()

        row = layout.row()
        row.operator("test.render_png")

        row = layout.row() 
        row.operator("test.render_jpeg")
        row = layout.row()
        
#        my_logo = pcoll["my_logo"]
        
        
        row = layout.row()
        row.scale_y = 2.5
  
#        row.operator("test.navigation", icon_value=my_logo.icon_id)
        row.operator("test.navigation")

        row = layout.row()
        
        row = layout.row()
        row.label(text= "Split Window", icon='WINDOW')
        row.operator("screen.split_area")
        
        row = layout.row()
        row.label(text= "Join Window", icon='TOPBAR')
        row.operator("screen.join_area")
        row = layout.row()
        
        
        row = layout.row()
        row.operator("test.vue_persp", icon='VIEW3D')
        
        row = layout.row()
        row.operator("test.vue_cam", icon='CON_CAMERASOLVER')
        row = layout.row()

        col.separator()
        col.prop(context.scene,"frame_start")
        col.prop(context.scene,"frame_end")
        col.separator()
            
        row = layout.row()
        row.operator("test.save_file",icon='FILE_TICK')
        
        row = layout.row()
        row.operator("test.list_camera",icon='PRESET')
        row = layout.row()
        
        row = layout.row()
        row.operator("test.file_browser",icon='FILE_FOLDER')
        row = layout.row()
        
        col = layout.column()
        col.template_list(
            "OUTLINER_UI_extreme_cameras",
            "",
            scene,
            "objects",
            scene,
            "active_object_index")
            
   
preview_collections = {}  

def register():
    
#    import bpy.utils.previews
#    pcoll = bpy.utils.previews.new()

#    my_logo_script_path = r"C:\Users\ophelie.abbonato\Documents\SMURFS"


#    my_logo_path = os.path.join(my_logo_script_path, "icon_interface")

#    print(my_logo_path)

#    print(os.path.exists(my_logo_path))
#    if not os.path.exists(my_logo_path):
#        print("POPOPOOOOOOOOOOOOOOOOOOOOOOOO")
#        #os.mkdir(my_icons_path)
#    
#    pcoll.load("my_logo", os.path.join(my_logo_path, "MouseNavig.png"), 'IMAGE')
#    

#    preview_collections["main"] = pcoll
    
    
    bpy.utils.register_class(focal100)
    bpy.utils.register_class(focal70)
    bpy.utils.register_class(focal50)
    bpy.utils.register_class(focal35)
    bpy.utils.register_class(focal28)
    bpy.utils.register_class(focal24)
    
    bpy.utils.register_class(RenderAnimation)
    
#    bpy.utils.register_class(RenameCamOperator)
    bpy.utils.register_class(RenderPngOperator)
    bpy.utils.register_class(RenderJpegOperator)
    bpy.utils.register_class(NavigationSimplifiee)
    bpy.utils.register_class(LockCamera)
    bpy.utils.register_class(UnlockCamera)
    bpy.utils.register_class(SplitArea)
    bpy.utils.register_class(JoinArea)
    bpy.utils.register_class(LibraryMesh)
    bpy.utils.register_class(FileSave)
    bpy.utils.register_class(Animation)
    bpy.utils.register_class(InsertKeyframe)
    bpy.utils.register_class(VuePersp)
    bpy.utils.register_class(VueCam)
    bpy.utils.register_class(DeleteKeyframe)
    
    bpy.utils.register_class(OUTLINER_UI_extreme_cameras)
    
    bpy.utils.register_class(SaveListCameras)
    
    bpy.utils.register_class(SimpleCustomMenu)
    bpy.utils.register_class(ListCameras)
    bpy.utils.register_class(FileSaveCameras)
    bpy.utils.register_class(ImportCamerasList)

    
    
    bpy.utils.register_class(StoryboardPanel)
    
    bpy.types.Scene.active_object_index = IntProperty()


def unregister():
    
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()
    
    
    
    bpy.utils.unregister_class(focal100)
    bpy.utils.unregister_class(focal70)
    bpy.utils.unregister_class(focal50)
    bpy.utils.unregister_class(focal35)
    bpy.utils.unregister_class(focal28)
    bpy.utils.unregister_class(focal24)
    
    bpy.utils.unregister_class(RenderAnimation)
    
    bpy.utils.unregister_class(RenameCamOperator)
    bpy.utils.unregister_class(RenderPngOperator)
    bpy.utils.unregister_class(RenderJpegOperator)
    bpy.utils.unregister_class(NavigationSimplifiee)
    bpy.utils.unregister_class(LockCamera)
    bpy.utils.unregister_class(UnlockCamera)
    bpy.utils.unregister_class(SplitAreaPanel)
    bpy.utils.unregister_class(JoinArea)
    bpy.utils.unregister_class(LibraryMesh)
    bpy.utils.unregister_class(FileSave)
    bpy.utils.unregister_class(Animation)
    bpy.utils.unregister_class(InsertKeyframe)
    bpy.utils.unregister_class(VuePersp)
    bpy.utils.unregister_class(VueCam)
    
    bpy.utils.unregister_class(DeleteKeyframe)
    
    bpy.utils.unregister_class(OUTLINER_UI_extreme_cameras)
    
    bpy.utils.unregister_class(SaveListCameras)
    
    bpy.utils.unregister_class(SimpleCustomMenu)
    bpy.utils.unregister_class(ListCameras)
    bpy.utils.unregister_class(FileSaveCameras)
    bpy.utils.unregister_class(ImportCamerasList)
    
    bpy.utils.unregister_class(StoryboardPanel)
    
    

if __name__ == "__main__":
    register()

#    bpy.ops.wm.call_menu(name=SimpleCustomMenu.bl_idname)
             