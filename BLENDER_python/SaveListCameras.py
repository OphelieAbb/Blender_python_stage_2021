import sys
import bpy
import os


class ImportCamerasList(bpy.types.Operator):
    bl_idname = "test.import_cameras"
    bl_label  = "Import Cameras List"
    bl_description = "Import la list des cameras"
   

    def execute(self,context):
        filepath =r"C:\Users\ophelie.abbonato\Documents\SMURFS\SMF_List_Cameras.fbx"
        bpy.ops.import_scene.fbx(filepath = filepath)

        return{'FINISHED'}



class FileSaveCameras(bpy.types.Operator):
    bl_idname = "test.save_cameras"
    bl_label  = "Save Cameras List"
    bl_description = "Sauve la list des cameras"


    def execute(self,context):

        for obj in bpy.context.scene.objects:
            if obj.type == "CAMERA":
                
                obj.select_set(True)
                
                filepath =r"C:\Users\ophelie.abbonato\Documents\SMURFS\SMF_List_Cameras.fbx"
                bpy.ops.export_scene.fbx(filepath = filepath, use_selection=True)
                

        return{'FINISHED'}



class ListCameras(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.list_cameras"
    bl_label = "List Cameras"
    cam = bpy.props.StringProperty(default="", options={'SKIP_SAVE'})


    @classmethod
    def poll(cls, context):
        return context.active_object is not None


    def execute(self, context):
        print("CAMERA", self.cam)
        cam = context.scene.objects.get(self.cam)
        context.scene.camera = cam
        return {'FINISHED'}
    
    
class SimpleCustomMenu(bpy.types.Menu):
    bl_label = "Cameras_Menu"
    bl_idname = "PT_Liste_Cameras"
    bl_space_type ='VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Save Cameras list'

    def draw(self, context):
        layout = self.layout
        scene  = bpy.context.scene
        
        cams = [c for c in context.scene.objects if c.type == 'CAMERA']
        #print(cams)
        for c in cams:
            op = layout.operator("object.list_cameras",text=c.name)
            op.cam = c.name
            
        
        row = layout.row()
        row.operator("test.save_cameras",icon='FILE_TICK')

        row = layout.row()
        row.operator("test.import_cameras",icon='IMPORT')



def register():
    
    bpy.utils.register_class(SimpleCustomMenu)
    bpy.utils.register_class(ListCameras)
    bpy.utils.register_class(FileSaveCameras)
    bpy.utils.register_class(ImportCamerasList)


def unregister():
    
    bpy.utils.unregister_class(SimpleCustomMenu)
    bpy.utils.unregister_class(ListCameras)
    bpy.utils.unregister_class(FileSaveCameras)
    bpy.utils.unregister_class(ImportCamerasList)
    

#def main():
#    scene = bpy.context.scene
#    SimpleCustomMenu()
#    SimpleCustomMenu()
#    creation_fichier_data_cameras = create_fichier_json(cameras_positions)
#    
#    profondeu_champ = profondeur_de_champ(cameras)

    
if __name__ == "__main__":
    register()


    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=SimpleCustomMenu.bl_idname)
    
