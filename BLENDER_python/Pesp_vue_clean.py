import bpy

def vue_perspective():
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            area.spaces[0].region_3d.view_perspective = 'PERSP'
            break

def main():
    vue_perspective()
      
if __name__ == "__main__":
    main()

