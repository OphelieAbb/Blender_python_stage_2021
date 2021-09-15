import bpy
from bpy.props import *

class focal24 (bpy.types.Operator):
    bl_idname = "test.focal_value24"
    bl_label  = "24"
    
    def execute (self,context):
        bpy.context.object.data.lens = 24
   
        return{'FINISHED'}
    
class focal28 (bpy.types.Operator):
    bl_idname = "test.focal_value28"
    bl_label  = "28"
    
    def execute (self,context):
        bpy.context.object.data.lens = 28
   
        return{'FINISHED'}
    
class focal35 (bpy.types.Operator):
    bl_idname = "test.focal_value35"
    bl_label  = "35"
    
    def execute (self,context):
        bpy.context.object.data.lens = 35
   
        return{'FINISHED'}
    
class focal50 (bpy.types.Operator):
    bl_idname = "test.focal_value50"
    bl_label  = "50"
    
    def execute (self,context):
        bpy.context.object.data.lens = 50
   
        return{'FINISHED'}
    
class focal70 (bpy.types.Operator):
    bl_idname = "test.focal_value70"
    bl_label  = "70"
    
    def execute (self,context):
        bpy.context.object.data.lens = 70
   
        return{'FINISHED'}
    
class focal100 (bpy.types.Operator):
    bl_idname = "test.focal_value100"
    bl_label  = "100"
    
    def execute (self,context):
        bpy.context.object.data.lens = 100
   
        return{'FINISHED'}

class FocalPanel(bpy.types.Panel):
    bl_label = "Focal_Panel"
    bl_idname = "PT_Focal"
    bl_space_type ='VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Create variation focal'
    
    
    
    
    def draw(self, context):

        
        layout = self.layout
        col    = layout.column(align=True)
        scene  = bpy.context.scene
        
        row = layout.row()
        row.operator("test.focal_value24")
        row.operator("test.focal_value28")
        row.operator("test.focal_value35")
        row = layout.row()
        row.operator("test.focal_value50")
        row.operator("test.focal_value70")
        row.operator("test.focal_value100")
        
        #layout.prop(scene, "MyInt", slider=True)
        
#        layout.prop(context.scene.camera.data, "lens")
#24 - 28 - 35 - 50 - 70 - 100        
        
def register():
    
    bpy.utils.register_class(focal100)
    bpy.utils.register_class(focal70)
    bpy.utils.register_class(focal50)
    bpy.utils.register_class(focal35)
    bpy.utils.register_class(focal28)
    bpy.utils.register_class(focal24)
    bpy.utils.register_class(FocalPanel)
    
    

def unregister():
    
    bpy.utils.unregister_class(focal100)
    bpy.utils.unregister_class(focal70)
    bpy.utils.unregister_class(focal50)
    bpy.utils.unregister_class(focal35)
    bpy.utils.unregister_class(focal28)
    bpy.utils.unregister_class(focal24)
    bpy.utils.unregister_class(FocalPanel)
    


if __name__ == "__main__":
    register()