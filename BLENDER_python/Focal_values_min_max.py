import bpy
from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       EnumProperty,
                       PointerProperty,
                       )



#def initprop():
#   
#    bpy.types.Camera.lens = bpy.props.IntProperty(
#    name="Focal",
#    description="Checkpoints to prevent skipping certain paths",
#    min=0, max=200,
#    default=50,
#    update = focalCam) #-1 disables a check!
#    


#class get_focal(bpy.types.Operator):
#    bl_idname = "test.focal"
#    bl_labal  = "Change focal"
#    
#    def execute(self,context):
#        bpy.context.object.data.lens 
#        return{"FINISHED"}

def focal_cam(self,context):
    bpy.context.object.data.lens = lens_cam

lens_cam = FloatProperty(
    name ="Distance Focale",
    description = "Distance focale",
    min = 1.0,
    max = 200.0,
    update = focal_cam,
    default = 50.0)
    
 


class ParametersCamerasPanel(bpy.types.Panel):
        
    bl_label       = "Parameters Cameras"
    bl_idname      = "CAMERAS_PT_parameters"
    bl_space_type  = 'VIEW_3D'
    bl_region_type = "UI"
    bl_category    = "Camera"
    
    def draw(self,context):
        layout = self.layout
        row    = layout.row()
        wm     = context.window_manager
        col    = layout.column(align=True)
        
#        obj = context.scene.camera
#        col.prop(context.scene.camera.data, "lens",slider =True)
        col.prop(lens_cam, "lens",slider =True) 
        
#        col.prop(context.scene.camera.data,"lens",slider =True)
   
#IntCheckpoint

classes = (
    ParametersCamerasPanel,
)
    
def register():
    
###################################################################################    
    
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

        
###################################################################################
 

def unregister():

###################################################################################
    
    from bpy.utils import unregister_class
    for cls in classes:
        unregister(cls)

        
###################################################################################



if __name__ == "__main__":
    register()
    