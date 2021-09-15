import bpy


def afficheCameraVue():
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            area.spaces[0].region_3d.view_perspective = 'PERSP'
            break
    

def affichePerspVue():
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            area.spaces[0].region_3d.view_perspective = 'CAMERA'
            break

def main():
    afficheCameraVue()
    affichePerspVue()   
    
if __name__ == "__main__":
    main()

