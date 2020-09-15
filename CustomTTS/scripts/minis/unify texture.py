import bpy
from bpy_extras.image_utils import load_image
from mathutils import Vector
import statistics
#import bmesh

#reimplement the grounding function
#reimplement autoscaling
#implement duplication and normal flipping of flat tris
#implement the texture combination into this script
#implement handling of UVs that are larger than a single texture

#put customTTS's path in the ""
#you will have to add a second '\' character wherever a single '\' character appears
customTTSPATH = ""

bpy.ops.import_scene.obj(filepath=customTTSPATH + "\\minis\\temp\\output.obj")

scale = float(open(customTTSPATH + '\\scripts\\minis\\wow_model_viewer_changer\\metadata.txt', 'r').read())

def Scale2D( v, s, p ):
    return ( p[0] + s[0]*(v[0] - p[0]), p[1] + s[1]*(v[1] - p[1]) )

def ScaleUV( uvMap, scale, pivot ):
    for x in range(len(uvMap.data)):
        uvMap.data[x].uv = Scale2D( uvMap.data[x].uv, scale, pivot )

def TransformUV(uvMap, x, y):
    for i in range(len(uvMap.data)):
        uvMap.data[i].uv.x += x
        uvMap.data[i].uv.y += y
		
def ScaleActiveToGrid():
	bpy.ops.object.mode_set(mode='EDIT')
	ob = bpy.context.scene.objects.active
	me = ob.data
	verts_loc = [v.co for v in me.vertices]
	verts_glb = [ob.matrix_world * v for v in verts_loc]
	verts_sel = verts_glb
	min_x = max([vert.x for vert in verts_sel])
	max_x = min([vert.x for vert in verts_sel])
	min_y = max([vert.y for vert in verts_sel])
	max_y = min([vert.y for vert in verts_sel])
	largest_bounds = max(abs(min_x), abs(max_x), abs(min_y), abs(max_y))
	if largest_bounds > 0.49:
		scale_factor = 0.49 / largest_bounds
		bpy.context.scene.objects.active.scale = (scale_factor, scale_factor, scale_factor)

def GroundActive():
	bpy.ops.object.mode_set(mode='EDIT')
	ob = bpy.context.scene.objects.active
	me = ob.data
	verts_loc = [v.co for v in me.vertices]
	verts_glb = [ob.matrix_world * v for v in verts_loc]
	verts_sel = verts_glb
	min_z = min([vert.z for vert in verts_sel])
	print("min_z:",min_z)
	bpy.ops.transform.translate(value=(0, 0, min_z * -1))
	
def CenterActive():
	bpy.ops.object.mode_set(mode='OBJECT')
	bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)
	bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
	bpy.ops.object.mode_set(mode='EDIT')
	ob = bpy.context.scene.objects.active
	me = ob.data
	verts_loc = [v.co for v in me.vertices]
	verts_glb = [ob.matrix_world * v for v in verts_loc]
	verts_sel = verts_glb
	min_x = min([vert.x for vert in verts_sel])
	max_x = max([vert.x for vert in verts_sel])
	mid_x = (max_x + min_x) / 2
	min_y = min([vert.y for vert in verts_sel])
	max_y = max([vert.y for vert in verts_sel])
	mid_y = (max_y + min_y) / 2
	min_z = min([vert.z for vert in verts_sel])
	max_z = max([vert.z for vert in verts_sel])
	mid_z = (max_z + min_z) / 2
	bpy.ops.object.mode_set(mode='OBJECT')
	bpy.ops.transform.translate(value=(mid_x, mid_y * -1, min_z * -1))

def RemoveActiveMaterials():
	bpy.ops.object.mode_set(mode='OBJECT')
	ob = bpy.context.scene.objects.active
	ob.active_material_index = 0
	for i in range(len(ob.material_slots)):
		bpy.ops.object.material_slot_remove({'object': ob})
	bpy.ops.material.new()
	mat = bpy.data.materials[-1]
	mat.name = "NAME"
	bpy.ops.object.material_slot_add()
	ob.active_material = mat
	
texture_dict = {}

print("")
print("")
print("[=== run ===]")

for ob in bpy.data.objects:
    print(ob.name)
    print(ob.type)
    if ob.type == "MESH":
        me = ob.data
        uv_layer = me.uv_textures[0]
        img = uv_layer.data.values()[0].image
        if img.name in texture_dict:
            texture_dict[img.name].append(ob)
        else:
            texture_dict[img.name] = [ob]

img_sizes = []
same_texture_objects = []

count = 0
for key in texture_dict:
    bpy.ops.object.select_all(action='DESELECT')
    print(key)
    print(bpy.data.images[key].size[0])
    img_sizes.append((bpy.data.images[key].size[0],bpy.data.images[key].size[1]))
    bpy.context.scene.objects.active = bpy.data.objects[texture_dict[key][0].name]
    for ob in texture_dict[key]:
        print(ob.name)
        ob.select = True
    bpy.ops.object.join()
    bpy.context.active_object.name = str(count)
    same_texture_objects.append(bpy.context.active_object)
    count += 1
    bpy.ops.object.select_all(action='DESELECT')

num_images = count

#unified_texture = bpy.ops.image.open(filepath="C:\\Users\\Keith Kelley.ThinkPad-Yoga12\\Desktop\\CustomTTS\\minis\\temp\\one.png"))
img = bpy.data.images.load(customTTSPATH + "\\minis\\temp\\one.png", check_existing=False)
img.name = "one.png"
print(img.size[0])
print(bpy.data.images['one.png'].name)

same_texture_objects.sort(key=lambda x: x.data.uv_textures.active.data[0].image.size[0], reverse=True)
img_sizes.sort(key=lambda x: x[0], reverse=True)

count = 0
top_line = 1
for ob in same_texture_objects:
    if ob.type == "MESH":
        uvmap = ob.data.uv_textures.active
        for uvface in uvmap.data:
            uvface.image = img
        uv_layer = ob.data.uv_layers.active
        scale_x = img_sizes[count][0]/img.size[0]
        scale_y = img_sizes[count][1]/img.size[1]
        ScaleUV(uv_layer, (scale_x, scale_y), (0.5,0.5))
        scale_y_half = scale_y / 2
        img_y_trans = top_line - (0.5 + scale_y_half)
        TransformUV(uv_layer, 0, img_y_trans)
        top_line -= scale_y
        count += 1

bpy.ops.object.select_all()
bpy.ops.object.join()
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.remove_doubles()
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.normals_make_consistent(inside=False)

RemoveActiveMaterials()
ScaleActiveToGrid()
CenterActive()
GroundActive()
#bpy.context.scene.objects.active.scale = (scale, scale, scale)
bpy.ops.export_scene.obj(filepath=customTTSPATH + "\\minis\\temp\\output_clean.obj")
