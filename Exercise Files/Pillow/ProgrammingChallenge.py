from PIL import Image
from fs.osfs import OSFS

ActiveDir = "ImagesArchive"

with OSFS(ActiveDir) as fileimgs:
    for file, info in fileimgs.walk.info(namespaces=['details']):
        with Image.open(ActiveDir+"/"+info.name) as img:
            img.thumbnail((128,128))
            extLen = 0
            if info.name[len(info.name)-4] == ".":
                extLen = 4
            else:
                extLen = 5
            newFileName = str(info.name[0:len(info.name)-extLen]) + ".thumb" + str(info.name[len(info.name)-extLen:len(info.name)])
            if ".thumb" in info.name or fileimgs.exists(newFileName):
                print(info.name, "already exists or has a thumbnail made for it.")
            else:
                img.save(ActiveDir + "/" + newFileName)
                print("Saved {0}".format(newFileName))