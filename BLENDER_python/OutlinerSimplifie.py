import bpy


class SCENE_PT_cameras(bpy.types.Panel):

    bl_label = "My label"
    bl_idname = "SCENE_PT_cameras"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "My Category"



    def draw(self, context):
        scene  = context.scene
        layout = self.layout
        col    = layout.column(align=True)

        obj = context.scene.camera
        


        layout.prop_search(data = context.scene,
            property = 'camera',
            search_data = bpy.context.scene,
            search_property = 'objects',
            text = 'Select Object',
            icon = 'CAMERA_DATA')


        row = layout.row()
        row.label(text="Active object is : " + obj.name)
        row = layout.row()
        row.prop(obj, "name")






def register():
    bpy.types.Scene.my_search = bpy.props.StringProperty()
    bpy.utils.register_class(SCENE_PT_cameras)




def unregister():
    bpy.utils.unregister_class(SCENE_PT_cameras)




if __name__ == "__main__":
    register()