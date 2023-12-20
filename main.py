import os
from datetime import datetime


EXEC_PATH = os.path.dirname(os.path.abspath(__file__))
FILE_NAME_PREFIX = ""


def establish_file(file_name):
    full_path = os.path.join(EXEC_PATH, file_name)
    with open(full_path, 'w') as f:
        f.seek(0)
        f.truncate(0)
        f.close()
    return open(full_path, 'w')


def rename_file(old_file_path, file_name, i, prefix=""):
    root, ext = os.path.splitext(file_name)
    new_file_name = f"{prefix}{i:04d}{ext}"
    new_file_path = os.path.join(WORK_PATH, new_file_name)
    
    if new_file_path == old_file_path:
        raise FileExistsError("ERROR: File name already in correct format.")
    
    if not os.path.isfile(old_file_path):
        raise FileNotFoundError("ERROR: Not a file.")
    
    if os.path.isfile(new_file_path):
        raise FileExistsError("ERROR: File already exists.")
    
    os.rename(old_file_path, new_file_path)
    return new_file_name
        

if __name__ == "__main__":
    try:
        log_file = establish_file("log.csv")
        log_file.write("Time, File #, Old Name, New Name\n")
        
        WORK_PATH = input("--Bulk file renamer--\nInput target folder full path: ")
        if not os.path.exists(WORK_PATH):
            raise FileNotFoundError(f"The directory \'{WORK_PATH}\' does not exist.")
        files = os.listdir(WORK_PATH)
        file_count = len(files)
        
        print(f"Dir found. {file_count} files located.")
        input("\nPress enter to begin...\n")
        start_timestamp = datetime.now()
        print("Started at", start_timestamp.strftime("%H:%M:%S"), "\n")
        
        list_dir = os.listdir(WORK_PATH)
        for i, file_name in enumerate(list_dir, 1):
            curtime = datetime.now().strftime("%H:%M")
            old_file_path = os.path.join(WORK_PATH, file_name)
            log_text = f"[{curtime}][{i:04d}/{file_count:04d}]: {file_name:20}  ->  "
            
            try:
                new_file_name = rename_file(old_file_path, file_name, i, FILE_NAME_PREFIX)
            except Exception as e:
                rename_status = str(e)
                if rename_status == "ERROR: File already exists.":
                    target = list_dir.index(file_name)
                    list_dir[i - 1], list_dir[target] = list_dir[target], list_dir[i - 1]
            else:
                rename_status = new_file_name
                
            print(log_text + rename_status)
            log_file.write(', '.join([curtime, str(i), file_name, rename_status]) + '\n')
                
    except KeyboardInterrupt:
        print("\nAborted.")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        print("\nFinished in", str(datetime.now() - start_timestamp).split('.', 2)[0], "at", datetime.now().strftime("%H:%M:%S"), "\n")
        print("Log file saved to: ", log_file.name)
    finally:
        log_file.close()
        print("Exiting...")