import bpy



class StoryboardPanel(bpy.types.Panel):
    bl_label = "Storyboard_Panel"
    bl_idname = "PT_StoryPanel"
    bl_space_type ='VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'StoryBoard'
    
    def draw(self, context):
        layout = self.layout
        scene = bpy.context.scene
        
        row = layout.row()
        row.label(text= "Create Camera", icon='VIEW_CAMERA')
        row.operator("object.camera_add")
        row.operator("view3d.camera_to_view")
         
        
        row = layout.row()
        row.label(text= "Create Board", icon='AXIS_SIDE')
        row.operator("object.gpencil_add")
        
        row = layout.row()
        row.label(text= "Export en FBX", icon='FILE_BLANK')
        row.operator("export_scene.fbx")
        

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



"""
        #row("launch_qt_win")
        
#        row = layout.row()
#        row.label(text= "Create Commentaire", icon='FILE_TEXT')
#        
#        btnCommentaire = QPushButton("Comment", self)
#        btnCommentaire.move(50,100)
#        btnCommentaire.clicked.connect(launch_qt_window)

"""
             