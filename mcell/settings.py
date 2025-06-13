# Set performance settings

import bpy, _cycles

for scene in bpy.data.scenes:
    bpy.context.scene.render.fps = 12
    bpy.context.scene.render.engine = "CYCLES"
    bpy.data.scenes["Scene"].cycles.device = "GPU"
    bpy.context.scene.cycles.device = "GPU"

bpy.context.preferences.addons["cycles"].preferences.compute_device_type = "CUDA"
bpy.context.preferences.addons["cycles"].preferences.peer_memory = True

devices = bpy.context.preferences.addons["cycles"].preferences.devices

for device in devices:
    if device.type == "CPU":
        device.use = False
    else:
        device.use = True

# enable addons

bpy.ops.preferences.addon_enable(module="bl_ext.system.cellblender")
bpy.ops.extensions.package_install_files(
    filepath="/app/neuropil_tools.zip", enable_on_install=True, repo="user_default"
)
