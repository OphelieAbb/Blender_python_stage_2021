import bpy

from bpy.types import PropertyGroup

from bpy.props import (
    CollectionProperty,
    IntProperty,
    BoolProperty,
    StringProperty,
    PointerProperty,
)


class OUTLINER_UI_extreme_cameras(bpy.types.UIList):
    
    

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        
        print(80*"#")
        print(item.type)
            
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
             
            layout.prop(item, "name", text="", emboss=False, icon_value=layout.icon(item))
            layout.prop(item, "hide_viewport", text="", emboss=False, icon = "HIDE_OFF")
            
            
class SCENE_PT_cameras(bpy.types.Panel):

    bl_label = "My label"
    bl_idname = "SCENE_PT_cameras"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "My Category"

    def draw(self, context):

        scn = context.scene
        layout = self.layout
        
        col = layout.column()
        col.template_list(
            "OUTLINER_UI_extreme_cameras",
            "",
            scn,
            "objects",
            scn,
            "active_object_index")


classes = (
           OUTLINER_UI_extreme_cameras,
           SCENE_PT_cameras)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.active_object_index = IntProperty()



def unregister():
    # fill this in.
    pass


if __name__ == "__main__":
    for i in range(50):
        print("")

    register()