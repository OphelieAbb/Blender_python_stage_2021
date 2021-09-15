import bpy
import blf
import sys


class DrawingClass:
    def __init__(self, context, prop):
        self.prop = prop
        self.context = context
        self.handle = bpy.types.SpaceView3D.draw_handler_add(
                   self.draw_text_callback,(self.context,),
                   'WINDOW', 'POST_PIXEL')

    def draw_text_callback(self, context):
        font_id = 0  # XXX, need to find out how best to get this.

        # draw some text
        blf.position(font_id, 15, 50, 0)
        blf.size(font_id, 20, 72)
        blf.draw(font_id, "%s %s" % (cam.name, self.prop))

    def remove_handle(self):
        bpy.types.SpaceView3D.draw_handler_remove(self.handle,'WINDOW')


dns = bpy.app.driver_namespace

if dns.get("dc"):

    dc = dns.get("dc")
    dc.remove_handle()


context = bpy.context
scene   = bpy.context.scene
cam     = scene.camera

dns = bpy.app.driver_namespace
drawer = DrawingClass(context, bpy.context.object.data.lens)
dns["dc"] = drawer