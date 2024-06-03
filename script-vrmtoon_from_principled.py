import bpy

# parameter for toon edge processing, set to True if you want to use VRM MToon's toon edge
mtoon_edges = False

index = 0
object = bpy.context.view_layer.objects.active

for material in object.data.materials:
    try:
        texture_image_name = material.node_tree.nodes["Principled BSDF"].inputs[0].links[0].from_node.image.name
        if not material.vrm_addon_extension.mtoon1.enabled:
            material.vrm_addon_extension.mtoon1.enabled = True
            material.vrm_addon_extension.mtoon1.pbr_metallic_roughness.base_color_texture.index.source = bpy.data.images[texture_image_name]
            material.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.shade_multiply_texture.index.source = bpy.data.images[texture_image_name]
            material.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.shade_color_factor = [0.500000, 0.500000, 0.500000]
            if (mtoon_edges == True):
                material.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.outline_width_mode = "worldCoordinates"
                material.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.outline_width_factor = 0.0005
        else: print("material already has vrmtoon enabled, double check in the material tab")
    except:
        print("error on material {}, probably not a Principled BSDF material".format(material.name))
        0.0005