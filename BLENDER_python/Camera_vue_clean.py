import bpy

def vue_camera():
    for obj in bpy.context.scene.objects:
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                area.spaces[0].region_3d.view_perspective = 'CAMERA'
                break

def main():
    vue_camera()
      
if __name__ == "__main__":
    main()

