import bpy
import os
import sys


class DELETE_OBJ(bpy.types.Operator):
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
       
class DECOR_SMF_PREMIER(bpy.types.Operator):
    bl_label  = "Decor 01"
    bl_idname = "decor.library_asset01"
    
    def execute(self,context):
        
        filepath =r"C:\Users\ophelie.abbonato\Documents\SMURFS\Decors\Scene_Smurf_Decor01.fbx"
        bpy.ops.import_scene.fbx(filepath = filepath)
        
        

        return{'FINISHED'}
    
class DECOR_SMF_DEUXIEME(bpy.types.Operator):
    bl_label  = "Decor 02"
    bl_idname = "decor.library_asset02"
    
    def execute(self,context):
        
        filepath =r"C:\Users\ophelie.abbonato\Documents\SMURFS\Decors\Scene_Smurf_Decor02.fbx"
        bpy.ops.import_scene.fbx(filepath = filepath)

        return{'FINISHED'}
    

              
        
class AssetMainPanel(bpy.types.Panel):
    bl_label       = "Asset library"
    bl_idname      = "ASSET_PT_MAINPANEL"
    bl_space_type  = "VIEW_3D"
    bl_region_type = "UI"
    bl_category    = "Asset Library"
    
    def draw (self, context):
        layout = self.layout
        pcoll = preview_collections["main"]
        
        row = layout.row()
        row.label(text = "Select a asset to be added")
        row = layout.row()
        row.operator("decor.library_asset01")
        
        my_icon = pcoll["my_icon"]
        my_icon2 = pcoll["my_icon2"]
        
        
        self.layout.template_icon(icon_value=my_icon.icon_id,scale=10)


        row = layout.row()
        row.operator("decor.library_asset02")
        
        self.layout.template_icon(icon_value=my_icon2.icon_id,scale=10)
        
        
        row = layout.row()
        row.operator("delete.decor")
        
        
preview_collections = {}   
        
def register():
    
   

    import bpy.utils.previews
    pcoll = bpy.utils.previews.new()

    my_script_path = r"C:\Users\ophelie.abbonato\Documents\SMURFS\Decors"


    my_icons_path = os.path.join(my_script_path, "icons")

    print(my_icons_path)

    print(os.path.exists(my_icons_path))
    if not os.path.exists(my_icons_path):
        print("POPOPOOOOOOOOOOOOOOOOOOOOOOOO")
        #os.mkdir(my_icons_path)
    
    pcoll.load("my_icon", os.path.join(my_icons_path, "Preview_Decor01.png"), 'IMAGE')
    
    pcoll.load("my_icon2", os.path.join(my_icons_path, "Preview_Decor02.png"), 'IMAGE')

    preview_collections["main"] = pcoll
    
    bpy.utils.register_class(AssetMainPanel)
    bpy.utils.register_class(DECOR_SMF_PREMIER)
    bpy.utils.register_class(DECOR_SMF_DEUXIEME)
    bpy.utils.register_class(DELETE_OBJ)


def unregister():
    
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()
    
    bpy.utils.unregister_class(AssetMainPanel)
    bpy.utils.unregister_class(DECOR_SMF_PREMIER)
    bpy.utils.unregister_class(DECOR_SMF_DEUXIEME)
    bpy.utils.unregister_class(DELETE_OBJ)        
    
    
if __name__ == "__main__":
    register()
