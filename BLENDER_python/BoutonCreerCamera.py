import bpy
import os

class RenameCamOperator(bpy.types.Operator):
    bl_idname = "test.rename_cameras"
    bl_label  = "Renomme Cam en Shot"
    
    def execute(self, context):
        textentry="shot"
        
        for obj in bpy.context.selected_objects:
            obj.name = textentry
            return{'FINISHED'}




class RenderPngOperator(bpy.types.Operator):
    bl_idname = "test.render_png"
    bl_label  = "Render PNG"
    
    
    def execute(self,context):
        
        scene  = bpy.context.scene
        
        # Enregistre direct les rendus au format qu'on veut
        #for i in row.operator:
            
        scene.render.image_settings.file_format ="PNG"
        scene.render.filepath =r"D:\3D\SMURFS\shot.png"#.format(str(i).zfill(2)) 
        
        bpy.ops.render.render(write_still=1)
        
        
        return{'FINISHED'}
    
class RenderJpegOperator(bpy.types.Operator):
    bl_idname = "test.render_jpeg"
    bl_label  = "Render JPEG"
    
    def execute(self,context):
        
        scene  = bpy.context.scene
        scene.render.image_settings.file_format ="JPEG"
        scene.render.filepath = r"D:\3D\SMURFS\shot.jpeg"
        
        bpy.ops.render.render(write_still=1)

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
        
        
        
        
        col.prop(context.scene.camera.data, "lens")
        
        
      

# Enregistre direct les rendus au format qu'on veut
#        scene.render.image_settings.file_format ="PNG"
#        scene.render.filepath = r"D:\3D\SMURFS\shot.png"
#        bpy.ops.render.render(write_still=1)
        
        col.prop(cam.data.dof, "aperture_fstop", slider=True)
        
        col.separator()
        col.prop(context.scene, "camera")
        col.separator()
        
        
        
        row = layout.row()
        row.label(text= "Create Board", icon='AXIS_SIDE')
        row.operator("object.gpencil_add")
        
        row = layout.row()
        row.label(text= "Export en FBX", icon='FILE_BLANK')
        row.operator("export_scene.fbx")
        
        row = layout.row()
        row.label(text= "Export en OBJ", icon='FILE_BLANK')
        row.operator("export_scene.obj")
        
        row = layout.row()
        #row.label(text= "Render", icon='RENDER_STILL')
        row.operator("test.render_png")
        
        row = layout.row()
        
        row.operator("test.render_jpeg")




def register():
    
    bpy.utils.register_class(RenameCamOperator)
    bpy.utils.register_class(RenderPngOperator)
    bpy.utils.register_class(RenderJpegOperator)
    bpy.utils.register_class(StoryboardPanel)




def unregister():
    
    bpy.utils.unregister_class(RenameCamOperator)
    bpy.utils.unregister_class(RenderPngOperator)
    bpy.utils.unregister_class(RenderJpegOperator)
    bpy.utils.unregister_class(StoryboardPanel)
    


if __name__ == "__main__":
    register()


             