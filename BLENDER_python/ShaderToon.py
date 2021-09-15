import bpy



material_toon = bpy.data.materials.get("Toon02")
material_outline = bpy.data.materials.get('Outline')

#Ajoouter plusieurs shaders à un object (ici shder toon)

objects_scene = []

for obj in bpy.data.objects :
    if obj.type == "MESH":
        obj.select_set(True)
#        bpy.ops.object.material_slot_remove()
        objects_scene.append(obj)


for o in objects_scene:
    bpy.ops.object.material_slot_add()
    o.data.materials.append(material_toon)
    bpy.ops.object.material_slot_add()
    o.data.materials.append(material_outline)