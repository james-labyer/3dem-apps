import os
from ij import IJ
from ini.trakem2 import Project
from ini.trakem2.display import Display, Patch

# Script based on examples in TrakEM2 documentation found at:
# https://imagej.net/plugins/trakem2/scripting#import-images-montage-them-blend-them-and-save-as-xml
# https://imagej.net/imagej-wiki-static/Jython_Scripting_Examples.html#Jython_tutorials_for_ImageJ
# https://imagej.net/plugins/trakem2/scripting#adding-images

folder = "/path/to/folder/with/all/images/"

# for i in range(3):
for i in range(450):
    # create new project in TrakEM2
    project = Project.newFSProject("blank", None, folder)

    # open image stack
    filename = "name-{}.tif".format(i + 1)
    filepath = os.path.join(folder, filename)
    imp = IJ.openImage(filepath)
    patch = Patch(project, imp.title, 0, 0, imp)
    patch.project.loader.addedPatchFrom(filepath, patch)

    # Add it to a layer
    layerset = project.getRootLayerSet()
    layer = layerset.getLayer(0, 1, True)
    layer.add(patch)
