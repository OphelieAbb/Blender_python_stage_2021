import bpy



class StoryboardPanel(bpy.types.Panel):
    bl_label = "Create_Cam"
    bl_idname = "Create_CAM"
    bl_space_type ='VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Cameras'
    
    def draw(self, context):
        layout = self.layout
        scene  = bpy.context.scene
        #render = bpy.scene.render
        
        row = layout.row()
        row.label(text= "Create Camera", icon='VIEW_CAMERA')
        row.operator("object.camera_add")
        row.operator("view3d.camera_to_view")
         
         
        row = layout.row()
        row.label(text= "Render Scene", icon='RENDER_STILL')
        row.operator("render.render")
        

CLASSES = [
    StoryboardPanel

]



def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)



def unregister():
    for cls in CLASSES:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()

#bpy.context.scene.render.image_settings.file_format = 'PNG'
#bpy.context.scene.render.image_settings.file_format = 'JPEG'
