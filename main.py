import os
from datetime import datetime

countOffset = 0

def truncateFileName(name):
    newFileLen = 20
    if len(name) > newFileLen:
        ext = name.split('.')[-1]
        name = name[:newFileLen - 5 - len(ext)] + "... ." + ext
    return name

if __name__ == "__main__":
    WORK_DIR = input("Input a working dir: ")

    if not os.path.isdir(WORK_DIR):
        print("Cannot lock onto directory.\nAborting.")
        exit(-1)

    start = datetime.now()
    dirpath, dirnames, filenames = next(os.walk(WORK_DIR), (None, None, []))
    fileCount = len(filenames)

    print(f"Dir locked. {fileCount} files found.")
    input("\nPress enter to begin...\n")
    print("Started at", datetime.now().strftime("%H:%M:%S"), "\n")

    for i in range(fileCount):
        curFileNum = i + countOffset
        maxFileNum = fileCount + countOffset
        curtime = datetime.now().strftime("%H:%M")
        newname = f"{curFileNum:04d}.{filenames[i].split('.')[-1]}"

        os.rename(os.path.join(dirpath, filenames[i]), os.path.join(dirpath, newname))

        print(f"[{curtime}][{i:04d}/{fileCount:04d}]: {truncateFileName(filenames[i]):>18}  ->  {truncateFileName(newname):>18}")

    print("\nFinished in", str(datetime.now() - start).split('.', 2)[0], "since", datetime.now().strftime("%H:%M:%S"), "\n")