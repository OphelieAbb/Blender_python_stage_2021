import bpy

#Ajoouter plusieurs shaders à un object

material_toon = bpy.data.materials.get("Toon02")
for o in bpy.context.selected_objects:
  if o.data.materials:
    o.data.materials[0] = material_toon
  else:
    o.data.materials.append(material_toon)

    
bpy.ops.object.material_slot_add()
material_outline = bpy.data.materials.get('Outline')
for o in bpy.context.selected_objects:
  if o.data.materials:
    o.data.materials[1] = material_outline
  else:
    o.data.materials.append(material_outline)