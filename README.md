# Blender - VRMToon Scripts
Collection of scripts to automate converting materials in Blender into VRM's MToon shader.

### Requirements :
Install these addons to your Blender (Tested on Blender 3.6LTS)
   1. [VRM-Addon-For-Blender](https://vrm-addon-for-blender.info/en/material-mtoon/)
   2. [mmd-tools](https://github.com/UuuNyaa/blender_mmd_tools) (Only for script-vrmtoon_from_mmdshader.py)

### How to use :
   1. Launch Blender
    
   2. On one of the windows, click on the top-left dropdown icon and select **'Text Editor'** below **Scripting** column.
    
   3. Click **'Open'** on the top-middle of the window.
    
   4. Navigate to the script files' location and open the .py files.

   5. Then for each scripts :

   6. **script-vrmtoon_from_mmdshader.py**
      1. Import an MMD model
      2. Click on the MMD model's **mesh** (**do not select all**, just the mesh)
      3. (Optional) if you want to use MToon's edge instead of mmd-tools's, set **mtoon_edges = True** in the text editor
      4. Run the script, and wait until finish
     
   7. **script-vrmtoon_from_principled.py**
      1. Import a model, check the material and make sure it's Principled BSDF with an Image Texture connected to it
      2. Click on the model's **mesh**
      3. (Optional) if you want to use MToon's edge, set **mtoon_edges = True** in the text editor
      4. Run the script, and wait until finish
     
   8. **script-vrmtoon_colorfactor.py** (to change the color and shadings for **all** VRM MToon shaded materials)
      1. Navigate to one of your model's material's VRM MToon tab (have to scroll down quite a bit)
      2. See the **Lighting** tab, there should be two color parameters; **Lit Color** and **Shade Color**.
      3. Set both of them to the color you want, preferably use material on part that is nicely visible so you can see how the color looks.
      4. Copy the value (Ctrl + C on the color) on **Lit Color** and replace **base_color_factor** value in the script to it. (Example : ```base_color_factor = [0.000000, 1.000000, 0.975493, 1.000000]```
      5. Copy the value (Ctrl + C on the color) on **Shade Color** and replace **shade_color_factor** value in the script to it, delete the right-most value inside the bracket. (Example : ```shade_color_factor = [0.200718, 0.045194, 0.500000, ]```
      6. Run the script, and wait until finish
     
   9. **script-vrmtoon_reenabler.py** (to re-enable VRMToon MToon shader when you copy a saved model from another Blender project to a scene that already have a model that uses VRMtoon MToon shader too
      1. Select a model and check if it has VRMToon MToon enabled from how it looks and see if **Enable VRMToon MToon Material** in the material's tab is enabled.
      2. If not Enabled, run the script, and wait until finish.

   10. For running the script, on the **Text Editor** window, click the **'Run Script'** button (the button with a triangle facing right as its icon) and wait until the process completes.

These scripts are mostly for my own personal use and I share in case someone needs it too.
