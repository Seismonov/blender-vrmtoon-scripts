import bpy

index = 0
object = bpy.context.view_layer.objects.active

for material in object.data.materials:
    if ("toon_solidify" not in material.name and material.vrm_addon_extension.mtoon1.enabled == False): material.vrm_addon_extension.mtoon1.enabled = True