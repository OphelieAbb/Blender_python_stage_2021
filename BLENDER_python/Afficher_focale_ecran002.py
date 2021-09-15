import bpy
import blf
import bgl


# -> BASED ON: https://blender.stackexchange.com/a/14746/31447
def view3d_find(context):
    # returns first 3d view, normally we get from context
    for area in context.window.screen.areas:
        if area.type == 'VIEW_3D':
            v3d = area.spaces[0]
            rv3d = v3d.region_3d
            for region in area.regions:
                if region.type == 'WINDOW':
                    return region, rv3d
    return None, None

def view3d_camera_border(context):
    obj = context.scene.camera
    cam = obj.data

    frame = cam.view_frame(scene=context.scene)
    # move from object-space into world-space 
    frame = [obj.matrix_world @ v for v in frame]

    # move into pixelspace
    from bpy_extras.view3d_utils import location_3d_to_region_2d
    region, rv3d = view3d_find(context)
    frame_px = [location_3d_to_region_2d(region, rv3d, v) for v in frame]
    return frame_px

# -> BASED ON: https://blender.stackexchange.com/a/31799/31447
def draw_string(x, y, packed_strings):
    font_id = 0
    blf.size(font_id, 18, 72) 
    x_offset = 0
    y_offset = 0
    line_height = (blf.dimensions(font_id, "M")[1] * 1.45)
    for command in packed_strings:
        if len(command) == 2:
            pstr, pcol = command
            blf.color(font_id, pcol[0], pcol[1], pcol[2], pcol[3]) # #bgl.glColor4f(pcol)
            text_width, text_height = blf.dimensions(font_id, pstr)
            blf.position(font_id, (x + x_offset), (y + y_offset), 0)
            blf.draw(font_id, pstr)
            x_offset += text_width
        else:
            x_offset = 0
            y_offset -= line_height

def draw_callback_px(self, context):
    
    WHITE = (1, 1, 1, .7)
    CR = "Carriage Return"
    
    x, y = view3d_camera_border(context)[3]
    cam_ob = context.scene.camera
    
    if cam_ob is not None:
        ps = [
            ("{} {}mm".format(cam_ob.name, cam_ob.data.lens), WHITE)] 
        
    
    draw_string(x+10, y-20, ps)
    # restore opengl defaults
    bgl.glLineWidth(1)
    bgl.glDisable(bgl.GL_BLEND)

# -> MODAL OPERATOR TEMPLATE
class ModalDrawOperator(bpy.types.Operator):
    """Draw a line with the mouse"""
    bl_idname = "view3d.modal_operator"
    bl_label = "Display Focal"

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'
    
    def modal(self, context, event):
        context.area.tag_redraw()
        
        if event.type in {'RIGHTMOUSE', 'ESC'}:
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'CANCELLED'}
        
        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        if context.space_data.region_3d.view_perspective == 'CAMERA':
            # the arguments we pass the the callback
            args = (self, context)
            # Add the region OpenGL drawing callback
            # draw in view space with 'POST_VIEW' and 'PRE_VIEW'
            self._handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback_px, args, 'WINDOW', 'POST_PIXEL')

            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "Switch into Camera View")
            return {'CANCELLED'}

class StoryboardPanel(bpy.types.Panel):
    bl_label = "Camera_Panel"
    bl_idname = "PT_Cameras"
    bl_space_type ='VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Create Cameras'
    
    
    
    
    def draw(self, context):
        layout = self.layout
        col    = layout.column(align=True)
        scene  = bpy.context.scene
        cam = context.scene.camera
        
        row = layout.row() 
        row.operator("view3d.modal_operator") 



def register():
    bpy.utils.register_class(ModalDrawOperator)
    bpy.utils.register_class(StoryboardPanel)

def unregister():
    bpy.utils.unregister_class(ModalDrawOperator)
    bpy.utils.unregister_class(StoryboardPanel)

if __name__ == "__main__":
    register()