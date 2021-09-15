import bpy
import os
import sys
import glob
import blf
import bgl
from bpy.props import BoolProperty# import bool property

# Authoriser import local pour le moment
my_script_path = r"C:\Users\ophelie.abbonato\Documents\SMURFS\Script_Python\BLENDER_python"

if not my_script_path in sys.path:
    print("Adding :D")
    sys.path.append(my_script_path)

import Camera_position_by_frame as cam_pos

################################################################################
#                              VARIABLES
################################################################################


cam_object = bpy.context.scene.camera
scene = bpy.context.scene
ma_pass_des_familles = r"C:\Users\ophelie.abbonato\Documents\SMURFS"


################################################################################
#                                OPERATORS
################################################################################

################################# SCENE ##################################

class SCENE_SMF_EXPORT(bpy.types.Operator):
    bl_label  = "Export Scene"
    bl_idname = "export.all_scene"
    
    def execute(self,context):
        
        filepath = r"C:\Users\ophelie.abbonato\Documents\SMURFS\Scenes\FBX_all_scene\WholeScene.fbx"
        bpy.ops.export_scene.fbx(filepath=filepath)
        
        return{'FINISHED'}
    
class SCENE_SMF_IMPORT(bpy.types.Operator):
    bl_label  = "Import Scene"
    bl_idname = "import.all_scene"
    
    def execute(self,context):
        
        filepath = r"C:\Users\ophelie.abbonato\Documents\SMURFS\Scenes\FBX_all_scene\WholeScene.fbx"
        bpy.ops.import_scene.fbx(filepath=filepath)
        
        return{'FINISHED'}


class FileSave(bpy.types.Operator):
    bl_idname = "test.save_file"
    bl_label  = "Save Scene"
    bl_description = "Sauve ta scene"
    
    def execute(self,context):
        bpy.ops.wm.save_as_mainfile('INVOKE_AREA')
        return{'FINISHED'}
#Ne sort pas la fenêtre file save       
#        filepath =r"C:\Users\ophelie.abbonato\Documents\SMURFS\Scene_Smurf.blend"
#        bpy.ops.wm.save_as_mainfile(filepath=filepath)

 

################################# ASSETS ################################## 

class DECOR_SMF_IMPORT(bpy.types.Operator):
    bl_label  = "import"
    bl_idname = "decor.library_assets"
    
    def execute(self,context):
        pcoll = preview_collections["thumbnail_previews"]
        if bpy.context.scene.my_thumbnails == "Preview_Decor01.png":
            filepath =r"C:\Users\ophelie.abbonato\Documents\SMURFS\Decors\Scene_Smurf_Decor01.fbx"
            bpy.ops.import_scene.fbx(filepath = filepath)
        
        if bpy.context.scene.my_thumbnails == "Preview_Decor02.png":
            filepath =r"C:\Users\ophelie.abbonato\Documents\SMURFS\Decors\Scene_Smurf_Decor02.fbx"
            bpy.ops.import_scene.fbx(filepath = filepath)                

        return{'FINISHED'}
    

class DELETE_FBX(bpy.types.Operator):
    bl_label = "Delete Decor"
    bl_idname = "delete.decor"
    
    def execute(self,context):
        for obj in bpy.context.scene.objects:
            if obj.type == "MESH":
                bpy.ops.object.select_all(action='DESELECT')
                obj.select_set(True)
                bpy.ops.object.delete()
            elif obj.type == "EMPTY":
                bpy.ops.object.select_all(action='DESELECT')
                obj.select_set(True)
                bpy.ops.object.delete()
                     
                
        return{'FINISHED'}
    
class DesimateMesh(bpy.types.Operator):

    bl_idname = "object.decimate_mesh"
    bl_label  = "Version LOD"
    bl_option = {"REGISTER,UNDO"}

    def execute(self,context):
        for i in range(50):
            print("")
                
        for obj in bpy.data.objects:
    #            obj.select_set(True)

            if obj.type == "MESH":
                
                bpy.context.view_layer.objects.active = obj
                bpy.ops.object.modifier_add(type='DECIMATE')
                bpy.ops.object.modifier_move_to_index(modifier="Decimate", index=0)

                bpy.context.object.modifiers["Decimate"].ratio = 0.02
                
                
                for mod in obj.modifiers:
                    print(mod.name)
        return{"FINISHED"}

    
    
class DesimateDelete(bpy.types.Operator):
    
    bl_idname = "object.decimate_delete"
    bl_label  = " Back to HD"
    bl_option = {"REGISTER,UNDO"}
    
    def execute(self,context):
        for i in range(50):
            print("")
                
        for obj in bpy.data.objects:

            if obj.type == "MESH":
                
                bpy.context.view_layer.objects.active = obj
                bpy.ops.object.modifier_remove(modifier="Decimate")

        return{"FINISHED"}

################################# CAMERAS ################################## 

class ImportCamerasList(bpy.types.Operator):
    bl_idname = "test.import_cameras"
    bl_label  = "Import Cameras List"
    bl_description = "Import la list des cameras"
   

    def execute(self,context):
        filepath =r"C:\Users\ophelie.abbonato\Documents\SMURFS\Cameras\liste_shots\SMF_List_Cameras.fbx"
        bpy.ops.import_scene.fbx(filepath = filepath)

        return{'FINISHED'}



class SaveListCameras(bpy.types.Operator):
    bl_idname = "test.save_list_cameras"
    bl_label  = "Export Cameras List"
    bl_description = "Sauve la list des cameras"
    
    def execute(self,context):

#        cam_object.select_set(True)
        for obj in bpy.context.scene.objects:
            obj.select_set(False)
            if obj.type == "CAMERA":
                obj.select_set(True) 
                
        filepath =r"C:\Users\ophelie.abbonato\Documents\SMURFS\Cameras\liste_shots\SMF_List_Cameras.fbx"

        bpy.ops.export_scene.fbx(filepath = filepath, use_selection=True)
        
        return{'FINISHED'}



    
class FileSaveCameras(bpy.types.Operator):
    bl_idname = "test.save_cameras"
    bl_label  = "Save Camera"
    bl_description = "Sauve une cameras"
    
    cam_object = bpy.context.scene.camera
    
    def execute(self,context):
        
        if not cam_object:
            print("YOLO CAMO y a pas de cam!!!!")
            return{'FINISHED'}
        
        cam_object.select_set(True)
        

                
        filepath =r"C:\Users\ophelie.abbonato\Documents\SMURFS\Cameras\Shots\Sh_{}".format(cam_object.name)

        bpy.ops.export_scene.fbx(filepath = filepath, use_selection=True)

        scene.render.image_settings.file_format ="PNG"
        scene.render.filepath =r"C:\Users\ophelie.abbonato\Documents\SMURFS\Decors\icon_cam\Sh_{}".format(cam_object.name)
        bpy.ops.render.opengl(write_still=1)
            
        return{'FINISHED'}
#        
#         for obj in bpy.context.scene.objects:
#            if obj.type == "CAMERA":    



class DELETE_CAMERA(bpy.types.Operator):
    bl_label = "Delete Camera"
    bl_idname = "delete.camera"
    
    def execute(self,context):

        camera_preview_path ="{}\Decors\icon_cam\Sh_{}.png".format(ma_pass_des_familles, cam_object.name)
       
        for obj in bpy.context.scene.objects:
            if obj.type == "CAMERA":
                bpy.ops.object.select_all(action='DESELECT')
                obj.select_set(True)
                bpy.ops.object.delete()
                
                os.remove(camera_preview_path)

        
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
    
class SimpleOperator(bpy.types.Operator):
    bl_label = "Lock / Unlock focal"
    bl_idname = "wm.simple_operator"
    
    @classmethod
    def poll(cls, context):
        print("Poll called")
        return True
    
    def execute(self, context):
       #switch bool property to opposite. if you don't toggle just set to False
        context.scene.my_bool_property = not context.scene.my_bool_property
        self.report({'INFO'}, "Simple Operator executed.")
        return {'FINISHED'}
    
    
################################# FOCAL #######################################


def view3d_find(context):
    # returns first 3d view, normally we get from context
    for area in context.window.screen.areas:
        if area.type == 'VIEW_3D':
            v3d = area.spaces[0]
            rv3d = v3d.region_3d
            for region in area.regions:
                if region.type == 'WINDOW':
                    return region, rv3d
    return None, None

def view3d_camera_border(context):
    obj = context.scene.camera
    cam = obj.data

    frame = cam.view_frame(scene=context.scene)
    # move from object-space into world-space 
    frame = [obj.matrix_world @ v for v in frame]

    # move into pixelspace
    from bpy_extras.view3d_utils import location_3d_to_region_2d
    region, rv3d = view3d_find(context)
    frame_px = [location_3d_to_region_2d(region, rv3d, v) for v in frame]
    return frame_px

def draw_string(x, y, packed_strings):
    font_id = 0
    blf.size(font_id, 18, 72) 
    x_offset = 0
    y_offset = 0
    line_height = (blf.dimensions(font_id, "M")[1] * 1.45)
    for command in packed_strings:
        if len(command) == 2:
            pstr, pcol = command
            blf.color(font_id, pcol[0], pcol[1], pcol[2], pcol[3]) # #bgl.glColor4f(pcol)
            text_width, text_height = blf.dimensions(font_id, pstr)
            blf.position(font_id, (x + x_offset), (y + y_offset), 0)
            blf.draw(font_id, pstr)
            x_offset += text_width
        else:
            x_offset = 0
            y_offset -= line_height


def draw_callback_px(self, context):
    
    WHITE = (1, 1, 1, .7)
    CR = "Carriage Return"
    
    x, y = view3d_camera_border(context)[3]
    cam_ob = context.scene.camera
    
    if cam_ob is not None:
        ps = [
            ("{} {}mm".format(cam_ob.name, cam_ob.data.lens), WHITE)] 
        
    
    draw_string(x+10, y-20, ps)
    # restore opengl defaults
    bgl.glLineWidth(1)
    bgl.glDisable(bgl.GL_BLEND)
    

class ModalDrawOperator(bpy.types.Operator):
    """Draw a line with the mouse"""
    bl_idname = "view3d.modal_operator"
    bl_label = "Display Focal"

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'
    
    def modal(self, context, event):
        context.area.tag_redraw()
        
        if event.type in {'RIGHTMOUSE', 'ESC'}:
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'CANCELLED'}
        
        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        if context.space_data.region_3d.view_perspective == 'CAMERA':
            # the arguments we pass the the callback
            args = (self, context)
            # Add the region OpenGL drawing callback
            # draw in view space with 'POST_VIEW' and 'PRE_VIEW'
            self._handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback_px, args, 'WINDOW', 'POST_PIXEL')

            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "Switch into Camera View")
            return {'CANCELLED'}


################################# NAVIGATION ##################################

class Focus(bpy.types.Operator):
    bl_idname = "screen.focus"
    bl_label  = " Focus Window"
    bl_description = "Focus l'objet selectionné"
    
    def execute(self, context):
        bpy.ops.view3d.view_selected(use_all_regions=False)
        return{'FINISHED'}

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
    
class JoinArea(bpy.types.Operator):
    bl_idname = "screen.join_area"
    bl_label  = "Join Window"
    bl_description = "Reuni la fenêtre en une vue"
    
    def execute(self, context):
        
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

################################# PANORAMA ##################################


class PanoCamera(bpy.types.Operator):
    bl_idname = "test.panorama_camera"
    bl_label  = "Panoramic Camera"
    bl_description = "Change ta camera en camera panoramique"
    

    def execute(self,context):
        #CHANGE IN CYSLE RENDER

        bpy.context.scene.render.engine = 'CYCLES'

        

        #CHAnGE CAMERA IN PANO

        bpy.context.object.data.type = 'PANO'
        bpy.context.object.data.cycles.panorama_type = 'EQUIRECTANGULAR'


        #IMPORT HDRI

        C = bpy.context
        scn = C.scene

        # Get the environment node tree of the current scene
        node_tree = scn.world.node_tree
        tree_nodes = node_tree.nodes

        # Clear all nodes
        tree_nodes.clear()

        # Add Background node
        node_background = tree_nodes.new(type='ShaderNodeBackground')

        # Add Environment Texture node
        node_environment = tree_nodes.new('ShaderNodeTexEnvironment')
        # Load and assign the image to the node property
        node_environment.image = bpy.data.images.load("//phalzer_forest_01_1k.exr") # Relative path
        node_environment.location = -300,0

        # Add Output node
        node_output = tree_nodes.new(type='ShaderNodeOutputWorld')   
        node_output.location = 200,0

        # Link all nodes
        links = node_tree.links
        link = links.new(node_environment.outputs["Color"], node_background.inputs["Color"])
        link = links.new(node_background.outputs["Background"], node_output.inputs["Surface"])
        
        #SUPPRIME OUTLINE SOLT

        for obj in bpy.data.objects:
            print(obj.name)
            
            if obj.type == "MESH":

                bpy.context.view_layer.objects.active = obj
                bpy.ops.object.material_slot_remove('INVOKE_DEFAULT')
        return{'FINISHED'}


class PanoRender(bpy.types.Operator):
    bl_idname = "test.panorama"
    bl_label  = "Render Panorama"
    bl_description = "Fait un rendu Panoramique / sauvegarde en png / incrémente à chaque sauvegarde"
    

    def execute(self,context):
        # RENDER
        scene = bpy.context.scene

        list_files = glob.glob(r"C:\Users\ophelie.abbonato\Documents\SMURFS\Rendu_Panorama\SMF_PANO*.png")

        iteration = len(list_files)+1

        scene.render.image_settings.file_format = "PNG"

        scene.render.filepath = r"C:\Users\ophelie.abbonato\Documents\SMURFS\Rendu_Panorama\SMF_PANO{:03}.png".format(iteration)

        bpy.ops.render.render(write_still=1)
        
        #tout redevient comme avant c'est à dire rendu EEVEE et on remet les bons solts mat
        
        bpy.context.scene.render.engine = 'BLENDER_EEVEE'
        
        for obj in bpy.data.objects:
            print(obj.name)
            
            if obj.type == "MESH":

                bpy.context.view_layer.objects.active = obj
                mat = bpy.data.materials.get("Outline")
                if mat is None:
                    # create material
                    mat = bpy.data.materials.new(name="Material")
        return{'FINISHED'}

################################# ANIMATION ##################################

class InsertKeyframe(bpy.types.Operator):
    bl_idname = "test.insert_keyframes"
    bl_label  = "Insert Keyframes"
    bl_description = "Insert clé animation sur Location/Rotation/focal"
    

    def execute(self,context):
    
        cam = bpy.data.cameras
        bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocRot')
        cam.keyframe_insert(data_path = 'lens', frame = (timeline_frame))
        return{'FINISHED'}

class DeleteKeyframe(bpy.types.Operator):
    bl_idname = "test.delete_keyframe"
    bl_label  = "Delete keyframe"
    
    def execute(self,context):
        bpy.context.active_object.keyframe_delete("location")
        bpy.context.active_object.keyframe_delete("rotation_euler")

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
        
        return{'FINISHED'}


################################################################################
#                                INTERFACES
################################################################################
#SCENE
class ParametersScenePanel(bpy.types.Panel):

    bl_label       = "Scene Parameters"
    bl_idname      = "SCENE_PT_parameters"
    bl_space_type  = 'VIEW_3D'
    bl_region_type = "UI"
    bl_category    = "Bank Set"
    

    def draw(self, context):
        
        layout = self.layout
        row = layout.row()
        row.operator("export.all_scene", icon='EXPORT')
        row.operator("import.all_scene",icon='IMPORT')
        row = layout.row()
        row.operator("test.save_file",icon='FILE_TICK')
        

#ASSETS
class PreviewsAssetPanel(bpy.types.Panel):

    bl_label       = "Bank Asets"
    bl_idname      = "OBJECT_PT_previews"
    bl_space_type  = 'VIEW_3D'
    bl_region_type = "UI"
    bl_category    = "Bank Set"
    

    def draw(self, context):
        
        layout = self.layout

        wm = context.window_manager
        row = layout.row()
        
        row.template_icon_view(context.scene, "my_thumbnails")
        
        # Just a way to access which one is selected
        row = layout.row()
        row.label(text="You selected: " + bpy.context.scene.my_thumbnails)
        row = layout.row()
        row.operator("decor.library_assets", icon='IMPORT')
        row.operator("delete.decor", icon= 'TRASH')
        row = layout.row()
        row.operator("object.decimate_mesh")
        row = layout.row()
        row.operator("object.decimate_delete")
        
#        col.template_icon_view(my_icon, "items", show_labels=True, scale=8)
preview_collections = {}


#CAMERAS
class PreviewsCamerasPanel(bpy.types.Panel):
        
    bl_label       = "Bank Cameras"
    bl_idname      = "CAMERAS_PT_previews"
    bl_space_type  = 'VIEW_3D'
    bl_region_type = "UI"
    bl_category    = "Bank Set"
    
    def draw(self,context):
        layout = self.layout
        row    = layout.row()
        wm     = context.window_manager
        col    = layout.column(align=True)
        
        obj = context.scene.camera
        
        
        
        row.template_icon_view(context.scene, "cam_thumbnails")
        row = layout.row()
        
        
        # Just a way to access which one is selected
        row = layout.row()
        row.label(text="You selected: " + bpy.context.scene.cam_thumbnails)
        row = layout.row()
        
        if scene.my_bool_property:#if bool property is true, lock foacl, else don't

            col.enabled = False
        
        row.operator("wm.simple_operator" , icon="LOCKED")
        
        row = layout.row()
        row.operator("test.save_cameras",icon='FILE_TICK')
        row.operator("delete.camera", icon= 'TRASH')
        
        row = layout.row()
        row.operator("test.save_list_cameras",icon='PRESET')
        row.operator("test.import_cameras",icon='PRESET')
        
        row = layout.row()
        row.operator("test.render_png")
        row.operator("test.render_jpeg")
        
        row = layout.row()
        row.operator("test.lock_camera",icon = "LOCKED")
        row.operator("test.unlock_camera",icon = "UNLOCKED")
        
        #Display focal of cam
        
        row = layout.row() 
        row.operator("view3d.modal_operator") 
            
        #Voir la liste des cameras et rename
        
        layout.prop_search(data = context.scene,
            property = 'camera',
            search_data = bpy.context.scene,
            search_property = 'objects',
            text = 'Select Object',
            icon = 'CAMERA_DATA')


        row = layout.row()
        row.label(text="Active object is : " + obj.name)
        row = layout.row()
        row.prop(obj, "name")
        
        col.prop(context.scene.camera.data, "lens")
        

#NAVIGATION
class NavigationPanel(bpy.types.Panel):

    bl_label       = "Navigation"
    bl_idname      = "NAVIGATION_PT_previews"
    bl_space_type  = 'VIEW_3D'
    bl_region_type = "UI"
    bl_category    = "Bank Set"
    

    def draw(self, context):
        
        layout = self.layout
        
        row = layout.row()
        row.scale_y = 2.5
        row.operator("test.navigation")
        
        row = layout.row()
        row.operator("screen.split_area", icon='WINDOW')
        row.operator("screen.join_area", icon='TOPBAR')
        
        row = layout.row()
        row.operator("test.vue_persp", icon='VIEW3D')
        row.operator("test.vue_cam", icon='CON_CAMERASOLVER')
        
        
        
        row = layout.row()
        row.operator("screen.focus")


#PANO
class PanoramaPanel(bpy.types.Panel):

    bl_label       = "Panorama"
    bl_idname      = "PANO_PT_render"
    bl_space_type  = 'VIEW_3D'
    bl_region_type = "UI"
    bl_category    = "Bank Set"
    
    def draw(self, context):
        
        layout = self.layout
        
        row = layout.row()
        row.operator("test.panorama_camera",icon="VIEW_CAMERA")
        row.operator("test.panorama",icon="MOD_THICKNESS")

#ANIMATION
class AnimationPanel(bpy.types.Panel):

    bl_label       = "Animation"
    bl_idname      = "Animation_PT_cam"
    bl_space_type  = 'VIEW_3D'
    bl_region_type = "UI"
    bl_category    = "Bank Set"
    
    def draw(self, context):
        
        layout = self.layout
        col    = layout.column(align=True)
        
        col.separator()
        col.prop(context.scene,"frame_start")
        col.prop(context.scene,"frame_end")
        col.separator()
        
        row = layout.row()
        row.operator("test.insert_keyframes", icon = "KEYFRAME")
        row.operator("test.delete_keyframe", icon = "KEYFRAME")
        
        row = layout.row()
        row.operator("test.animation", icon = "TIME")
        
        row = layout.row() 
        row.operator("test.render_animation") 
        row = layout.row() 



def generate_previews():
    

    pcoll = preview_collections["thumbnail_previews"]
    image_location = pcoll.images_location
    VALID_EXTENSIONS = ('.png', '.jpg', '.jpeg')
    
    enum_items = []
    
    # Generate the thumbnails
    for i, image in enumerate(os.listdir(image_location)):
        if image.endswith(VALID_EXTENSIONS):
            filepath = os.path.join(image_location, image)
            thumb = pcoll.load(filepath, filepath, 'IMAGE')
            enum_items.append((image, image, "", thumb.icon_id, i))
            
    return enum_items




classes = (
    DECOR_SMF_IMPORT,
    DELETE_FBX,
    DELETE_CAMERA,
    PreviewsAssetPanel,
    PreviewsCamerasPanel,
    FileSaveCameras,
    SaveListCameras,
    ImportCamerasList,
    RenderPngOperator,
    RenderJpegOperator,
    LockCamera,
    UnlockCamera,
    NavigationPanel,
    NavigationSimplifiee,
    SplitArea,
    JoinArea,
    FileSave,
    VuePersp,
    VueCam,
    SimpleOperator,
    DesimateMesh,
    DesimateDelete,
    PanoramaPanel,
    PanoRender,
    PanoCamera,
    ModalDrawOperator,
    InsertKeyframe,
    DeleteKeyframe,
    Animation,
    RenderAnimation,
    AnimationPanel,
    Focus,
    SCENE_SMF_EXPORT,
    ParametersScenePanel,
    SCENE_SMF_IMPORT)

    
    
def register():
    
    

################################# ASSET ##################################    
    from bpy.types import Scene
    from bpy.props import StringProperty, EnumProperty
    
    
    import bpy.utils.previews
    pcoll = bpy.utils.previews.new()

    my_script_path = r"C:\Users\ophelie.abbonato\Documents\SMURFS\Decors"


    pcoll.images_location = os.path.join(my_script_path, "icons")

    print(pcoll.images_location)

    print(os.path.exists(pcoll.images_location))
    if not os.path.exists(pcoll.images_location):
        print("POPOPOOOOOOOOOOOOOOOOOOOOOOOO")
        #os.mkdir(my_icons_path)
    
#    pcoll.load("my_icon", os.path.join(pcoll.images_location, "Preview_Decor01.png"), 'IMAGE')
    
#    pcoll.load("my_icon2", os.path.join(my_icons_path, "Preview_Decor02.png"), 'IMAGE')

    preview_collections["thumbnail_previews"] = pcoll
    
    bpy.types.Scene.my_thumbnails = EnumProperty(
        items=generate_previews(),
        )
################################# CAMERAS ################################## 

    my_cam_path = r"C:\Users\ophelie.abbonato\Documents\SMURFS\Decors "     
    
    pcoll.images_location = os.path.join(my_script_path, "icon_cam")
    
    print(pcoll.images_location)

    print(os.path.exists(pcoll.images_location))
    if not os.path.exists(pcoll.images_location):
        print("POPOPOOOOOOOOOOOOOOOOOOOOOOOO")
        
        preview_collections["cameras_previews"] = pcoll
    
    bpy.types.Scene.cam_thumbnails = EnumProperty(
        items=generate_previews(),
        )
    
###################################################################################    
    
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
        
###################################################################################
    
    bpy.types.Scene.my_search = bpy.props.StringProperty()
    
###################################################################################

bpy.types.Scene.my_bool_property = BoolProperty(name='My Bool Property', default = True)# create bool property for switching    

def unregister():
    

###################################################################################
    from bpy.types import WindowManager
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()

###################################################################################
    
    from bpy.utils import unregister_class
    for cls in classes:
        unregister(cls)
        
###################################################################################

    del bpy.types.Scene.my_bool_property#remove property on unregister



if __name__ == "__main__":
    register()
    
    # The menu can also be called from scripts
#    bpy.ops.wm.call_menu(name=MESH_PREVIEW_menu.bl_idname)