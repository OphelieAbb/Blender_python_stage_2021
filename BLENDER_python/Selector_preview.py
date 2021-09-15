import bpy
import os



scene = bpy.context.scene
ma_pass_des_familles = r"C:\Users\ophelie.abbonato\Documents\SMURFS"


class DECOR_SMF_IMPORT(bpy.types.Operator):
    bl_label  = "import"
    bl_idname = "decor.library_assets"
    
    def execute(self,context):
        pcoll = preview_collections["thumbnail_previews"]
        if bpy.context.scene.my_thumbnails == "Preview_Decor01.png":
            filepath =r"C:\Users\ophelie.abbonato\Documents\SMURFS\Decors\Scene_Smurf_Decor01.fbx"
            bpy.ops.import_scene.fbx(filepath = filepath)
        
        if bpy.context.scene.my_thumbnails == "Preview_Decor02.png":
            filepath =r"C:\Users\ophelie.abbonato\Documents\SMURFS\Decors\Scene_Smurf_Decor02.fbx"
            bpy.ops.import_scene.fbx(filepath = filepath)                

        return{'FINISHED'}
    




class PreviewsAssetPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label       = "Bank Set"
    bl_idname      = "OBJECT_PT_previews"
    bl_space_type  = 'VIEW_3D'
    bl_region_type = "UI"
    bl_category    = "Bank Set"


    def draw(self, context):
        
        layout = self.layout

        wm = context.window_manager
        row = layout.row()
        
        row.template_icon_view(context.scene, "my_thumbnails")
        

        row = layout.row()
        row.label(text="You selected: " + bpy.context.scene.my_thumbnails)
        row = layout.row()
        row.operator("decor.library_assets")
  
        

preview_collections = {}


classes = (PreviewsAssetPanel,)


def generate_previews():
    

    pcoll = preview_collections["thumbnail_previews"]
    image_location = pcoll.images_location
    VALID_EXTENSIONS = ('.png', '.jpg', '.jpeg')
    
    enum_items = []
    
    # Generate the thumbnails
    for i, image in enumerate(os.listdir(image_location)):
        if image.endswith(VALID_EXTENSIONS):
            filepath = os.path.join(image_location, image)
            thumb = pcoll.load(filepath, filepath, 'IMAGE')
            enum_items.append((image, image, "", thumb.icon_id, i))
            
    return enum_items


    
def register():
    
    

################################# ASSET ##################################    
    from bpy.types import Scene
    from bpy.props import StringProperty, EnumProperty
    
    
    import bpy.utils.previews
    pcoll = bpy.utils.previews.new()

    my_script_path = r"C:\Users\ophelie.abbonato\Documents\SMURFS\Decors"


    pcoll.images_location = os.path.join(my_script_path, "icons")

    print(pcoll.images_location)

    print(os.path.exists(pcoll.images_location))
    if not os.path.exists(pcoll.images_location):
        print("POPOPOOOOOOOOOOOOOOOOOOOOOOOO")
        #os.mkdir(my_icons_path)
    
    preview_collections["thumbnail_previews"] = pcoll
    
    bpy.types.Scene.my_thumbnails = EnumProperty(
        items=generate_previews(),
        )

    
###################################################################################    
    
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
        
###################################################################################
    

def unregister():
    

###################################################################################
    from bpy.types import WindowManager
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()

###################################################################################
    
    from bpy.utils import unregister_class
    for cls in classes:
        unregister(cls)
        
###################################################################################
#    pass

if __name__ == "__main__":
    register()
