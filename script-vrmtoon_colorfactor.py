import bpy

# change these two values to your preferred color, shade color preferably darker than base color
# must be 4 input
base_color_factor = [1.000000, 1.000000, 1.000000, 1.000000]
# must be 3 input
shade_color_factor = [0.500000, 0.500000, 0.500000]

#index = 0
#object = bpy.context.view_layer.objects.active

for material in bpy.data.materials:
    if material.vrm_addon_extension.mtoon1.enabled:
        if material.vrm_addon_extension.mtoon1.pbr_metallic_roughness.base_color_texture.index.source != None and material.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.shade_multiply_texture.index.source != None:
            material.vrm_addon_extension.mtoon1.pbr_metallic_roughness.base_color_factor = base_color_factor
            material.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.shade_color_factor = shade_color_factor