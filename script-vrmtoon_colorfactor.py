import bpy

# change these two values to your preferred color, shade color preferably darker than base color
# must be 4 input
base_color_factor = [1.000000, 1.000000, 1.000000, 1.000000]
# must be 3 input
shade_color_factor = [0.195962, 0.195962, 0.195962]

#index = 0
#object = bpy.context.view_layer.objects.active

for material in bpy.data.materials:
    if material.vrm_addon_extension.mtoon1.enabled == True:
        material.vrm_addon_extension.mtoon1.pbr_metallic_roughness.base_color_factor = base_color_factor
        material.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.shade_color_factor = shade_color_factor