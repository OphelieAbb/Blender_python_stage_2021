import bpy
import os
import glob



class LibraryMesh (bpy.types.Operator):
    bl_idname = "test.file_browser"
    bl_label  = "Open library"
    bl_description = "ouvre librairie 3d pour import mesh"
    
    def execute(self,context):
                # Call user prefs window
        bpy.ops.screen.userpref_show("INVOKE_DEFAULT")

        # Change area type
        area = bpy.context.window_manager.windows[-1].screen.areas[0]
        area.type = 'FILE_BROWSER'




class RenameCamOperator(bpy.types.Operator):
    bl_idname = "test.rename_cameras"
    bl_label  = "Renomme Cam en Shot"
    bl_description = "Renomme la camera en shot et l'incrémente"
    
    def execute(self, context):
        textentry="shot"
        
        for obj in bpy.context.selected_objects:
            obj.name = textentry
        return{'FINISHED'}




class RenderPngOperator(bpy.types.Operator):
    bl_idname = "test.render_png"
    bl_label  = "Render PNG"
    bl_description = "Rendu d'image PNG et incrémentation"
    
    def execute(self,context):
        
        scene  = bpy.context.scene
        #for i in range(scene.frame_start, scene.frame_end):
            
        list_files = glob.glob(r"C:\Users\ophelie.abbonato\Documents\SMURFS\shot*.png")
        iteration = len(list_files)+1
        scene.render.image_settings.file_format ="PNG"
        scene.render.filepath =r"C:\Users\ophelie.abbonato\Documents\SMURFS\shot{:03}.png".format(iteration)
        
        bpy.ops.render.opengl(write_still=1)

                    
        return{'FINISHED'}


            
    
class RenderJpegOperator(bpy.types.Operator):
    bl_idname = "test.render_jpeg"
    bl_label  = "Render JPEG"
    bl_description = "Rendu d'image JPEG et incrémentation"
    
    def execute(self,context):
        
        scene  = bpy.context.scene
        list_files = glob.glob(r"C:\Users\ophelie.abbonato\Documents\SMURFS\shot*.jpeg")
        iteration = len(list_files)+1
        scene.render.image_settings.file_format ="JPEG"
        scene.render.filepath =r"C:\Users\ophelie.abbonato\Documents\SMURFS\shot{:03}.jpeg".format(iteration)
        
        bpy.ops.render.opengl(write_still=1)
        return{'FINISHED'}

#Rendre une video mp4    
#class RenderAnimation(bpy.types.Operator):
#    bl_idname = "test.render_animation"
#    bl_label= "render animation"
#    
#    def execute(self,context):
#        for iteration in range(scene.frame_start, scene.frame_end):
#            scene.render.image_settings.file_format ="FFMPEG"
#            scene.render.filepath =r"C:\Users\ophelie.abbonato\Documents\SMURFS\shot{:03}.ffmpeg".format(iteration)
#            
#            bpy.ops.render.opengl(write_still=1)
        

        
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
    bl_label  = " split area"
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
        row.label(text= "Create Camera", icon='VIEW_CAMERA')
        row.operator("object.camera_add")
        row.operator("view3d.camera_to_view")
        
        row = layout.row()
        row.label(text= "Slectionne Cameras")
        row.operator("test.rename_cameras")
        
        
        row = layout.row()
        row.label(text="Choose focal")
        row = layout.row()
        row.operator("test.focal_value24")
        row.operator("test.focal_value28")
        row.operator("test.focal_value35")

        row.operator("test.focal_value50")
        row.operator("test.focal_value70")
        row.operator("test.focal_value100")
        
        #col.prop(context.scene.camera.data, "lens")  


        col.separator()
        col.prop(context.scene, "camera")
        col.separator()
        
        
        row = layout.row()
        row.operator("test.render_png")
        
        
        
        row = layout.row() 
        row.operator("test.render_jpeg")
        
        row = layout.row()
        row.operator("test.navigation")
        
        
        
        row = layout.row()
        row.label(text= "Lock Cam", icon = "LOCKED")
        row.operator("test.lock_camera")
        row.operator("test.unlock_camera")
        
        row = layout.row()
        row.label(text= "Split Area", icon='IMGDISPLAY')
        row.operator("screen.split_area")
        
        row = layout.row()
        row.operator("test.file_browser",icon='FILE_FOLDER')
        
#        col.separator()
#        col.prop(context.scene,"frame_start")
#        col.prop(context.scene,"frame_end")
#        col.separator()


def register():
    
    bpy.utils.register_class(focal100)
    bpy.utils.register_class(focal70)
    bpy.utils.register_class(focal50)
    bpy.utils.register_class(focal35)
    bpy.utils.register_class(focal28)
    bpy.utils.register_class(focal24)
    
    bpy.utils.register_class(RenameCamOperator)
    bpy.utils.register_class(RenderPngOperator)
    bpy.utils.register_class(RenderJpegOperator)
    bpy.utils.register_class(NavigationSimplifiee)
    bpy.utils.register_class(LockCamera)
    bpy.utils.register_class(UnlockCamera)
    bpy.utils.register_class(SplitArea)
    bpy.utils.register_class(LibraryMesh)
    
    bpy.utils.register_class(StoryboardPanel)




def unregister():
    
    bpy.utils.unregister_class(focal100)
    bpy.utils.unregister_class(focal70)
    bpy.utils.unregister_class(focal50)
    bpy.utils.unregister_class(focal35)
    bpy.utils.unregister_class(focal28)
    bpy.utils.unregister_class(focal24)
    
    bpy.utils.unregister_class(RenameCamOperator)
    bpy.utils.unregister_class(RenderPngOperator)
    bpy.utils.unregister_class(RenderJpegOperator)
    bpy.utils.unregister_class(NavigationSimplifiee)
    bpy.utils.unregister_class(LockCamera)
    bpy.utils.unregister_class(UnlockCamera)
    bpy.utils.unregister_class(SplitAreaPanel)
    bpy.utils.unregister_class(LibraryMesh)
    
    bpy.utils.unregister_class(StoryboardPanel)
    


if __name__ == "__main__":
    register()


             