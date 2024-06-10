import os
import stat

def is_executable(filepath):
    """
    Check if a file is executable.
    """
    try:
        st = os.stat(filepath)
        return (st.st_mode & stat.S_IEXEC) and os.path.isfile(filepath)
    except OSError:
        return False

def list_executables(root_dir):
    """
    List all executable files in the specified directory.
    """
    executable_files = []
    try:
        with os.scandir(root_dir) as it:
            for entry in it:
                if entry.is_file() and is_executable(entry.path):
                    executable_files.append(entry.path)
    except PermissionError:
        print(f"Permission denied: {root_dir}")
    return executable_files

def choose_executable(dest_dir):
    """
    List executable files and prompt the user to choose one.
    Returns the selected executable file name.
    """
    print('Executables found below:')
    executables = list_executables(dest_dir)
    
    if not executables:
        print("No executable files found.")
        return None
    
    for index, executable in enumerate(executables, start=1):
        print(f"{index} - {executable}")

    while True:
        try:
            choice = int(input("Enter the number of the executable you want to choose: "))
            if 1 <= choice <= len(executables):
                # Return the filename without the directory path
                return os.path.basename(executables[choice - 1])
            else:
                print("Invalid choice. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# For testing purposes, if the script is run directly
if __name__ == '__main__':
    dest_dir = r'C:\automacoes_sem_parar\01'  # Use a raw string literal for Windows paths
    selected_executable = choose_executable(dest_dir)
    if selected_executable:
        print(f"You selected: {selected_executable}")
    else:
        print("No executable selected.")
