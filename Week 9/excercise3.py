import os

def main():
    cwd = os.getcwd()
    print("Current working directory:", cwd)

    lab_dir = os.path.join(cwd, "lab_files")
    created_dir = False

    if not os.path.exists(lab_dir):
        os.mkdir(lab_dir)
        created_dir = True
        print("Created folder:", lab_dir)
    else:
        print("Folder already exists:", lab_dir)

    filenames = ["file1.txt", "file2.txt", "file3.txt"]
    created_files = []
    for name in filenames:
        path = os.path.join(lab_dir, name)
        if not os.path.exists(path):
            open(path, "w").close()
            created_files.append(name)
            print("Created file:", path)
        else:
            print("File already exists (skipped):", path)

    try:
        files_in_dir = os.listdir(lab_dir)
        print("Files in folder:", files_in_dir)
    except Exception as e:
        print("Error listing folder contents:", e)
        files_in_dir = []

    src = os.path.join(lab_dir, "file1.txt")
    dst = os.path.join(lab_dir, "renamed_file1.txt")
    if os.path.exists(src):
        if not os.path.exists(dst):
            os.rename(src, dst)
            print(f"Renamed {src} -> {dst}")
        else:
            print("Destination file already exists, cannot rename:", dst)
    else:
        print("Source file to rename does not exist (skipped):", src)

    print("Files after rename:", os.listdir(lab_dir))

    if created_dir:
        for entry in os.listdir(lab_dir):
            entry_path = os.path.join(lab_dir, entry)
            if os.path.isfile(entry_path):
                try:
                    os.remove(entry_path)
                    print("Removed file:", entry_path)
                except Exception as e:
                    print("Error removing file:", entry_path, e)
            else:
                print("Skipping non-file entry:", entry_path)
        try:
            os.rmdir(lab_dir)
            print("Removed folder:", lab_dir)
        except Exception as e:
            print("Error removing folder:", lab_dir, e)
    else:
    
        for name in ["renamed_file1.txt", "file2.txt", "file3.txt"]:
            path = os.path.join(lab_dir, name)
            if os.path.exists(path) and os.path.isfile(path):
                try:
                    os.remove(path)
                    print("Removed file:", path)
                except Exception as e:
                    print("Error removing file:", path, e)
            else:
                print("No cleanup needed for (missing or not a file):", path)
        print("Folder was not created by this script; folder removal skipped:", lab_dir)

    print("All operations complete.")

if __name__ == "__main__":
    main()