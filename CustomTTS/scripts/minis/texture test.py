import bpy

def Scale2D( v, s, p ):
    return ( p[0] + s[0]*(v[0] - p[0]), p[1] + s[1]*(v[1] - p[1]) )

def ScaleUV( uvMap, scale, pivot ):
    for x in range(len(uvMap.data)):
        uvMap.data[x].uv = Scale2D( uvMap.data[x].uv, scale, pivot )

def TransformUV(uvMap, x, y):
    for i in range(len(uvMap.data)):
        uvMap.data[i].uv.x += x
        uvMap.data[i].uv.y += y

ob = bpy.context.scene.objects.active
uv_layer = ob.data.uv_layers.active
scale_x = 1
scale_y = 0.25
ScaleUV(uv_layer, (scale_x, scale_y), (0.5,0.5))
