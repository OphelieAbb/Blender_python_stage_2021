import bpy

class SplitArea(bpy.types.Operator):
    bl_idname = "screen.split_area"
    bl_label  = " split area"
    

    def execute(self, context):

        bpy.ops.screen.area_split(direction="VERTICAL", factor=0.3)

        if context.region_data.view_perspective == 'PERSP':
            context.region_data.view_perspective = 'CAMERA'
            
        else:
            context.region_data.view_perspective = 'PERSP'

        return {"FINISHED"}



class JoinArea(bpy.types.Operator):
    bl_idname = "screen.join_area"
    bl_label  = "join area"
    
    def execute(self, context):
        
        area1 = bpy.context.screen.areas[3]
        area2 = bpy.context.screen.areas[-1]
        

        bpy.ops.screen.screen_full_area()

        
        return {"FINISHED"}




class SplitAreaPanel(bpy.types.Panel):
    bl_label = "Area_Panel"
    bl_idname = "_PT_Areas"
    bl_space_type ='VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Create Split Area'
    
    
    
    
    def draw(self, context):
        layout = self.layout
        col    = layout.column(align=True)
        scene  = bpy.context.scene
        cam = context.scene.camera
        start_areas = bpy.context.screen.areas[:]
      
        row = layout.row()
        row.label(text= "Split Area", icon='WINDOW')
        row.operator("screen.split_area")
        
        row = layout.row()
        row.label(text= "Split Area", icon='TOPBAR')
        row.operator("screen.join_area")



def register():
    
    bpy.utils.register_class(SplitAreaPanel)
    bpy.utils.register_class(SplitArea)
    bpy.utils.register_class(JoinArea)


def unregister():
    
    bpy.utils.unregister_class(SplitAreaPanel)
    bpy.utils.unregister_class(SplitArea)
    bpy.utils.unregister_class(JoinArea)
    


if __name__ == "__main__":
    register()