import bpy
import sys 
import glob

#CHANGE IN CYSLE RENDER

bpy.context.scene.render.engine = 'CYCLES'

#SUPPRIME OUTLINE SOLT

for obj in bpy.data.objects:
    print(obj.name)
    if obj.type == "MESH":

        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.material_slot_remove("Outline")


#CHAnGE CAMERA IN PANO

bpy.context.object.data.type = 'PANO'
bpy.context.object.data.cycles.panorama_type = 'EQUIRECTANGULAR'


#IMPORT HDRI

C = bpy.context
scn = C.scene

# Get the environment node tree of the current scene
node_tree = scn.world.node_tree
tree_nodes = node_tree.nodes

# Clear all nodes
tree_nodes.clear()

# Add Background node
node_background = tree_nodes.new(type='ShaderNodeBackground')

# Add Environment Texture node
node_environment = tree_nodes.new('ShaderNodeTexEnvironment')
# Load and assign the image to the node property
node_environment.image = bpy.data.images.load("//phalzer_forest_01_1k.exr") # Relative path
node_environment.location = -300,0

# Add Output node
node_output = tree_nodes.new(type='ShaderNodeOutputWorld')   
node_output.location = 200,0

# Link all nodes
links = node_tree.links
link = links.new(node_environment.outputs["Color"], node_background.inputs["Color"])
link = links.new(node_background.outputs["Background"], node_output.inputs["Surface"])

# RENDER



scene = bpy.context.scene

list_files = glob.glob(r"C:\Users\ophelie.abbonato\Documents\SMURFS\Rendu_Panorama\SMF_PANO*.png")

iteration = len(list_files)+1

scene.render.image_settings.file_format = "PNG"

scene.render.filepath = r"C:\Users\ophelie.abbonato\Documents\SMURFS\Rendu_Panorama\SMF_PANO{:03}.png".format(iteration)

bpy.ops.render.render(write_still=1)