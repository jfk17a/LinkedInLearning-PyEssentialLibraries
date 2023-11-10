from fs.osfs import OSFS

totalFilesSize = 0

with OSFS(".") as myfs:
    for path, info in myfs.walk.info(namespaces=['details'], filter=["*.txt"]):
        totalFilesSize += info.size
    print("Total size of files is:", totalFilesSize)