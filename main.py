import os
from os import walk
from datetime import datetime

if __name__ == "__main__":
    WORK_DIR = input("Input a working dir: ")

    if not os.path.isdir(WORK_DIR):
        print("Cannot lock onto directory.\nAborting.")
        exit(-1)

    start = datetime.now()
    dirpath, dirnames, filenames = next(walk(WORK_DIR), (None, None, []))
    fileCount = len(filenames)

    print(f"Dir locked. {fileCount} files found.")
    input("\nPress enter to begin...\n")

    for i in range(fileCount):
        curtime = datetime.now().strftime("%H:%M")
        newname = "{itr:04d}.{ext}".format(itr=i, ext=filenames[i].split('.', 2)[1])
        os.rename(os.path.join(dirpath, filenames[i]), os.path.join(dirpath, newname))

        print(f"[{curtime}][{i:04d}/{fileCount:04d}]: {filenames[i]} -> {newname}")
    
    print(f"\nFinished in {str(datetime.now() - start).split('.', 2)[0]}")