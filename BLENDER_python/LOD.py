import bpy

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

                
            print("*"*20)
            print("")
                
#        mesh_objs = [obj for obj in bpy.data.objects if obj.type =="MESH"]
#        for i, obj in enumerate(mesh_objs):
#            print(i, obj.name)

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
          
        
    
class ExemplePanel(bpy.types.Panel):
    
    bl_label       = "Camera_Panel"
    bl_idname      = "PT_Camera"
    bl_space_type  = "VIEW_3D"
    bl_region_type = "UI"

    
    def draw(self,context):
        layout = self.layout
        scene = bpy.context.scene
        
        row = layout.row()
        
        row.operator("object.decimate_mesh")
        row.operator("object.decimate_delete")
        
        
def register():
    bpy.utils.register_class(DesimateDelete)
    bpy.utils.register_class(DesimateMesh)
    bpy.utils.register_class(ExemplePanel)
    
def unregister():
    bpy.utils.unregister_class(DesimateDelete)    
    bpy.utils.unregister_class(DesimateMesh)
    bpy.utils.unregister_class(ExemplePanel)
    
if __name__ == "__main__":
    register()