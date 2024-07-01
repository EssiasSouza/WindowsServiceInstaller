import os
import shutil

def copy_files(source_dir, dest_dir, exceptions):
    
    try:
        if not os.path.exists(source_dir):
            print(f"Source directory does not exist: {source_dir}")
            return

        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        for root, dirs, files in os.walk(source_dir):
            relative_path = os.path.relpath(root, source_dir)
            dest_path = os.path.join(dest_dir, relative_path)

            if not os.path.exists(dest_path):
                os.makedirs(dest_path)

            for file in files:
                source_file = os.path.join(root, file)
                dest_file = os.path.join(dest_path, file)

                if any(os.path.abspath(source_file).startswith(os.path.abspath(exc)) for exc in exceptions):
                    continue

                shutil.copy2(source_file, dest_file)

            dirs[:] = [d for d in dirs if not any(os.path.abspath(os.path.join(root, d)).startswith(os.path.abspath(exc)) for exc in exceptions)]

    except Exception as e:
        print(f"Error copying files: {e}")

